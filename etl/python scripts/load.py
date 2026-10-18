import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, text
from sqlalchemy.engine import URL

load_dotenv()
print("DB_HOST:", repr(os.getenv("DB_HOST")))
print("DB_PORT:", repr(os.getenv("DB_PORT")))
print("DB_USER:", repr(os.getenv("DB_USER")))
print("DB_NAME:", repr(os.getenv("DB_NAME")))
print("Password loaded:", os.getenv("DB_PASSWORD") is not None)

connection_url = URL.create(
    drivername="postgresql+psycopg2",
    username=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    host=os.getenv("DB_HOST"),
    port=int(os.getenv("DB_PORT", "5432")),
    database=os.getenv("DB_NAME"),
)

engine = create_engine(connection_url)


def load_to_postgres(df, table_name):
    if table_name == "products":
        id_column = "product_id"
    elif table_name == "users":
        id_column = "user_id"
    elif table_name == "carts":
        id_column = "cart_id"
    elif table_name == "cart_items":
        id_column = ["cart_id", "product_id"]
    else:
        raise ValueError("Unknown table name")

    columns = list(df.columns)
    column_names = ", ".join(columns)
    values = ", ".join(f":{col}" for col in columns)

    if isinstance(id_column, list):
        conflict_columns = ", ".join(id_column)
        update_columns = [col for col in columns if col not in id_column]
    else:
        conflict_columns = id_column
        update_columns = [col for col in columns if col != id_column]

    updates = ", ".join(f"{col} = EXCLUDED.{col}" for col in update_columns)

    query = text(f"""
        INSERT INTO {table_name} ({column_names})
        VALUES ({values})
        ON CONFLICT ({conflict_columns})
        DO UPDATE SET {updates}
    """)

    records = df.to_dict(orient="records")

    with engine.begin() as connection:
        connection.execute(query, records)

    print(f"Loaded {len(records)} records into {table_name}")
