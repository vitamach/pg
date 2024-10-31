import sys
import csv

def nacti_csv(soubor): 
    seznam = []
    with open(soubor, "r", encoding='utf-8') as file:
        reader = csv.DictReader(file)  
        for radek in reader:
            seznam.append(radek)
    return seznam

def spoj_data_od_gpt(data1, data2):
    # Získání všech unikátních klíčů (sloupců) z obou souborů
    vsechny_klice = list(set().union(*(d.keys() for d in data1 + data2)))
    
    # Spojení dat do jednoho seznamu
    spojena_data = []
    
    # Přidání hlavičky
    spojena_data.append(vsechny_klice)
    
    # Přidání dat z prvního souboru
    for radek in data1:
        nova_radka = [radek.get(klic, '') for klic in vsechny_klice]
        spojena_data.append(nova_radka)
    
    # Přidání dat z druhého souboru
    for radek in data2:
        nova_radka = [radek.get(klic, '') for klic in vsechny_klice]
        spojena_data.append(nova_radka)
    
    return spojena_data

def zapis_csv(soubor, data):
    with open(soubor, "w", encoding='utf-8', newline='') as fp:
        writer = csv.writer(fp)
        writer.writerows(data)

if __name__ == "__main__": 
    try:
        soubor1 = sys.argv[1]
        soubor2 = sys.argv[2]
        
        csv_data1 = nacti_csv(soubor1)
        csv_data2 = nacti_csv(soubor2)
        
        spojena_data = spoj_data_od_gpt(csv_data1, csv_data2)
        
        vystupni_soubor = "spojena_data.csv"
        zapis_csv(vystupni_soubor, spojena_data)
        
        print(f"Data byla úspěšně zapsána do souboru {vystupni_soubor}")

    except IndexError:
        print("Zadejte prosím dva názvy souborů jako argumenty.")
    except Exception as e:
        print("Nastala neočekávaná chyba:", e)