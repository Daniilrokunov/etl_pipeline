import requests
import json

url = "https://fakestoreapi.com/products"

response = requests.get(url, timeout=15)
response.raise_for_status()

data = response.json()

print("Количество товаров:", len(data))
print("\nПервый товар:")
print(json.dumps(data[0], indent=4, ensure_ascii=False))
