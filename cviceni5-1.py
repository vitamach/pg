import sys
import csv

def nacti_csv(soubor): 
    seznam = []
    with open(soubor, "r") as file:
        reader = csv.reader(file)
        for radek in reader:
            seznam.append(radek)

    return seznam

if __name__ == "__main__": 
    try:
        soubor1 = sys.argv[1]
        soubor2 = sys.argv[2]
        csv_data1 = nacti_csv(soubor1)
        csv_data2 = nacti_csv(soubor2)
        print(csv_data1, csv_data2)
    except Exception:
        raise