import sys 
import csv

def nacti_csv(soubor):
    data = []
    with open(soubor, "r") as fp:
        reader = csv.reader(fp)
        for row in reader:
            data.append(row)
    return data 

if __name__ == "__main__":
    try:
        soubor1 = sys.argv[1]
        soubor2 = sys.argv[2]
        csv_data1 = nacti_csv(soubor1)
        csv_data2 = nacti_csv(soubor2)

    except Exception:
        