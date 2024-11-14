import requests
from bs4 import BeautifulSoup

def stahni_url_a_vrat_nadpisy(url):
    nadpisy = []

    try:
        response = requests.get(url)

        if response.status_code != 200:
            print(f"Nastala chyba: {response.status_code}")
            return nadpisy

    except requests.exceptions.RequestException as e:
        print(f"Chyba při stahování stránky: {e}")
        return nadpisy

    soup = BeautifulSoup(response.text, 'html.parser')

    for nadpis in soup.find_all('h1'):
        text = nadpis.text.strip()
        if text: 
            nadpisy.append(text)

    return nadpisy

if __name__ == "__main__":
    url = input("Zadej url: ")
    nadpisy = stahni_url_a_vrat_nadpisy(url)
    
    for nadpis in nadpisy:
        print(nadpis)