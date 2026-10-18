import pandas as pd


def transform_product(product_df):
    df = product_df.copy()
    df["rate"] = df["rating"].apply(lambda x: x["rate"])
    df["count"] = df["rating"].apply(lambda x: x["count"])
    df = df.rename(
        columns={
            "id": "product_id",
            "title": "product_name",
            "price": "product_price",
            "category": "product_category",
            "description": "description",
        }
    )
    df = df[
        [
            "product_id",
            "product_name",
            "product_price",
            "product_category",
            "description",
            "image",
            "rate",
            "count",
        ]
    ]

    df["product_price"] = df["product_price"].astype(float)

    return df


def transform_users(user_df):
    df = user_df.copy()
    df["first_name"] = df["name"].apply(lambda x: x["firstname"])
    df["last_name"] = df["name"].apply(lambda x: x["lastname"])
    df["street"] = df["address"].apply(lambda x: x["street"])
    df["city"] = df["address"].apply(lambda x: x["city"])
    df["zipcode"] = df["address"].apply(lambda x: x["zipcode"])

    df = df.rename(
        columns={"id": "user_id", "email": "user_email", "username": "username"}
    )

    df = df[
        [
            "user_id",
            "user_email",
            "username",
            "first_name",
            "last_name",
            "street",
            "city",
            "zipcode",
        ]
    ]

    return df


def transform_carts(carts_df):
    df = carts_df.copy()

    df = df.rename(columns={"id": "cart_id", "userId": "user_id"})

    df = df[["cart_id", "user_id"]]
    return df


def transform_cart_items(carts_df):
    df = carts_df[["id", "products"]].copy()

    df = df.explode("products", ignore_index=True)

    df["product_id"] = df["products"].apply(lambda x: x["productId"])
    df["quantity"] = df["products"].apply(lambda x: x["quantity"])

    df = df.rename(columns={"id": "cart_id"})

    df = df[["cart_id", "product_id", "quantity"]]

    return df
