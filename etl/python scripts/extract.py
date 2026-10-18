import pandas as pd
import requests

base_url = "https://fakestoreapi.com/"


def extract_product():
    url = f"{base_url}/products"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    product_df = pd.DataFrame(data)
    return product_df


def extract_users():
    url = f"{base_url}/users"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    user_df = pd.DataFrame(data)
    return user_df


def extract_carts():
    url = f"{base_url}/carts"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    carts_df = pd.DataFrame(data)
    return carts_df
