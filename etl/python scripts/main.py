from extract import extract_product, extract_users, extract_carts
from transform import (
    transform_product,
    transform_users,
    transform_carts,
    transform_cart_items,
)
from load import load_to_postgres


def run_pipeline():
    print("Starting pipeline")

    product_df = extract_product()
    users_df = extract_users()
    carts_df = extract_carts()

    print("Starting transformation")

    product_df = transform_product(product_df)
    users_df = transform_users(users_df)
    cart_items_df = transform_cart_items(carts_df)
    carts_df = transform_carts(carts_df)

    print("Loading to Postgres")

    load_to_postgres(product_df, "products")
    load_to_postgres(users_df, "users")
    load_to_postgres(carts_df, "carts")
    load_to_postgres(cart_items_df, "cart_items")


if __name__ == "__main__":
    run_pipeline()
