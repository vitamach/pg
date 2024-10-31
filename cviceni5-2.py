import sys
import csv

def nacti_csv(soubor):
    seznam = []
    try:
        with open(soubor, "r") as file:
            reader = cvs.reader(file)
            for radek in reader:
                seznam.append(radek)
        
    except FileNotFoundError:
        print(f"Soubor {soubor} nebyl nalezen.")
        return[]

    except FileExistsError:
        print(f"Soubor neextuje")
        return []

    except IOError:
        print(f"Došlo k chybě při čtení souboru: {soubor}")
        return []
    return seznam

def spoj_data(data1, data2):
     excel.cvs + excel2.cvs

if __name__ == "__main__": 
    try:
        soubor1 = sys.argv[1]
        soubor2 = sys.argv[2]
        csv_data1 = nacti_csv(soubor1)
        csv_data2 = nacti_csv(soubor2)
        print(csv_data1, csv_data2)
    except Exception:
        print("Neni chyba")