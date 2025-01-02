import requests
import json

url = "https://jsonplaceholder.typicode.com/posts"
user_names = {
    1: "Leanne Graham",
    2: "Ervin Howell",
    3: "Clementine Bauch",
    4: "Patricia Lebsack",
    5: "Chelsey Dietrich",
    6: "Mrs. Dennis Schulist",
    7: "Kurtis Weissnat",
    8: "Nicholas Runolfsdottir V",
    9: "Glenna Reichert",
    10: "Clementina DuBuque"
}

def fetch_and_save_data():
    try:
        response = requests.get(url)
        
        if response.ok:
            data = response.json() #převod
            
            for post in data:
                user_id = post['userId']
                post['userName'] = user_names[user_id]
            
            with open('data.json', 'w', encoding='utf-8') as file:
                json.dump(data, file, indent=2)
            
            return True
        return False
        
    except Exception as e:
        print(f"Došlo k chybě: {e}")
        return False

if __name__ == "__main__":
    uspech = fetch_and_save_data()
    print("Data byla úspěšně stažena a uložena." if uspech else "Nastala chyba při zpracování dat.")