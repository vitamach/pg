import json
import requests

url = "https://db.carnewschina.com/suggest?q="

def download_json_and_parse_brands(prefix):

    response = requests.get(url + prefix)

    if response.status_code != 200:
        print(f"Error: Failed to fetch data. Status code: {response.status_code}")
        return []
    
    try:
        json_data = response.json()
        
        brands = []
        if "brands" in json_data:
            brands = [brand["name"] for brand in json_data["brands"]]
        
        return brands
        
    except json.JSONDecodeError as e:
        print(f"Error: Failed to parse JSON response: {e}")
        return []
    except KeyError as e:
        print(f"Error: Unexpected JSON structure: {e}")
        return []

if __name__ == "__main__":
    prefix = input("Zadej prefix: ")
    brands = download_json_and_parse_brands(prefix)
    for brand in brands:
        print(brand)