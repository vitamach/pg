if __name__ == "__main__":
    def cislo_text(cislo):
        jednotky = {
            0: "nula", 1: "jedna", 2: "dva", 3: "tři", 4: "čtyři", 5: "pět", 6: "šest", 7: "sedm", 
            8: "osm", 9: "devět", 10: "deset", 11: "jedenáct", 12: "dvanáct", 13: "třináct", 
            14: "čtrnáct", 15: "patnáct", 16: "šestnáct", 17: "sedmnáct", 18: "osmnáct", 19: "devatenáct"
        }

        desitky = {
            20: "dvacet", 30: "třicet", 40: "čtyřicet", 50: "padesát", 60: "šedesát", 
            70: "sedmdesát", 80: "osmdesát", 90: "devadesát"
        }

        stovky = {
            100: "sto", 200: "dvě stě", 300: "tři sta", 400: "čtyři sta", 
            500: "pět set", 600: "šest set", 700: "sedm set", 800: "osm set", 900: "devět set"
        }
        
        # Konvertujeme číslo na integer
        cislo = int(cislo)
        
        if cislo in jednotky:
            return jednotky[cislo]
        elif cislo in desitky:
            return desitky[cislo]
        elif cislo in stovky:
            return stovky[cislo]
        elif 20 < cislo < 100:
            desitka = (cislo // 10) * 10
            jednotka = cislo % 10
            return desitky[desitka] + " " + jednotky[jednotka]
        elif 100 < cislo < 1000:
            sto = (cislo // 100) * 100  # Získáme stovky (např. 300)
            zbytek = cislo % 100  # Získáme zbytek (např. 45)
            if zbytek == 0:
                return stovky[sto]
            else:
                return stovky[sto] + " " + cislo_text(zbytek)
        elif 1000 <= cislo < 2000:
            zbytek = cislo % 1000
            if zbytek == 0:
                return "tisíc"
            else:
                return "tisíc " + cislo_text(zbytek)
        elif 2000 <= cislo < 10000:
            tisice = (cislo // 1000)
            zbytek = cislo % 1000
            if zbytek == 0:
                return jednotky[tisice] + " tisíce"
            else:
                return jednotky[tisice] + " tisíce " + cislo_text(zbytek)
        else:
            return "Neplatné číslo"

    if __name__ == "__main__":
        cislo = input("Zadej číslo: ")
        text = cislo_text(cislo)
        print(text)
