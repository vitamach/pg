import requests

# Nový endpoint pro API ČSÚ
base_url = "https://vdb.czso.cz/pll/eweb/v1"

# Příklad dotazu na metadata dostupných datasetů
response = requests.get(f"{base_url}/datasets")

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Chyba: {response.status_code}")