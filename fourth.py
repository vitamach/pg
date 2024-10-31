def je_tah_mozny(figurka, cilova_pozice, obsazene_pozice):
    
    radek, sloupec = cilova_pozice
    
    if not (1 <= radek <= 8 and 1 <= sloupec <= 8):
        return False
    
    if cilova_pozice in obsazene_pozice:
        return False
    
    typ_figurky = figurka["typ"]
    aktualni_pozice = figurka["pozice"]
    
    delta_radek = cilova_pozice[0] - aktualni_pozice[0]
    delta_sloupec = cilova_pozice[1] - aktualni_pozice[1]

    pohyby = {
        "pěšec": [(1, 0), (2, 0)] if aktualni_pozice[0] == 2 else [(1, 0)],
        "jezdec": [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)],
        "věž": [(0, 1), (0, -1), (1, 0), (-1, 0)],
        "střelec": [(1, 1), (1, -1), (-1, 1), (-1, -1)],
        "dáma": [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)],
        "král": [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]
    }

    # Funkce pro kontrolu, zda je volná cesta pro věž, střelce nebo dámu
    def je_volna_cesta(start, cil):
        krok_radek = 0 if cil[0] - start[0] == 0 else (cil[0] - start[0]) // abs(cil[0] - start[0])
        krok_sloupec = 0 if cil[1] - start[1] == 0 else (cil[1] - start[1]) // abs(cil[1] - start[1])
        
        pozice = (start[0] + krok_radek, start[1] + krok_sloupec)
        while pozice != cil:
            if pozice in obsazene_pozice:
                return False
            pozice = (pozice[0] + krok_radek, pozice[1] + krok_sloupec)
        return True

    if typ_figurky == "pěšec":
        mozne_tahy = [(pozice[0] + aktualni_pozice[0], pozice[1] + aktualni_pozice[1]) 
                      for pozice in pohyby["pěšec"]]
        return cilova_pozice in mozne_tahy

    elif typ_figurky == "jezdec":
        mozne_tahy = [(pozice[0] + aktualni_pozice[0], pozice[1] + aktualni_pozice[1]) 
                      for pozice in pohyby["jezdec"]]
        return cilova_pozice in mozne_tahy

    elif typ_figurky == "věž":
        if delta_radek == 0 or delta_sloupec == 0:  
            return je_volna_cesta(aktualni_pozice, cilova_pozice)
        return False

    elif typ_figurky == "střelec":
        if abs(delta_radek) == abs(delta_sloupec):  
            return je_volna_cesta(aktualni_pozice, cilova_pozice)
        return False

    elif typ_figurky == "dáma":
        if delta_radek == 0 or delta_sloupec == 0 or abs(delta_radek) == abs(delta_sloupec):
            return je_volna_cesta(aktualni_pozice, cilova_pozice)
        return False

    elif typ_figurky == "král":
        return abs(delta_radek) <= 1 and abs(delta_sloupec) <= 1

    return False

if __name__ == "__main__":
    pesec = {"typ": "pěšec", "pozice": (2, 2)}
    jezdec = {"typ": "jezdec", "pozice": (3, 3)}
    vez = {"typ": "věž", "pozice": (8, 8)}
    strelec = {"typ": "střelec", "pozice": (6, 3)}
    dama = {"typ": "dáma", "pozice": (8, 3)}
    kral = {"typ": "král", "pozice": (1, 4)}
    obsazene_pozice = {(2, 2), (8, 2), (3, 3), (5, 4), (8, 3), (8, 8), (6, 3), (1, 4)}

    # Jednoduché testování vracející True nebo False
    print(je_tah_mozny(pesec, (3, 2), obsazene_pozice))  # True
    print(je_tah_mozny(pesec, (4, 2), obsazene_pozice))  # True
    print(je_tah_mozny(pesec, (5, 2), obsazene_pozice))  # False
    print(je_tah_mozny(pesec, (1, 2), obsazene_pozice))  # False

    print(je_tah_mozny(jezdec, (4, 4), obsazene_pozice))  # False
    print(je_tah_mozny(jezdec, (5, 4), obsazene_pozice))  # False
    print(je_tah_mozny(jezdec, (1, 2), obsazene_pozice))  # True
    print(je_tah_mozny(jezdec, (9, 3), obsazene_pozice))  # False

    print(je_tah_mozny(dama, (8, 1), obsazene_pozice))  # False
    print(je_tah_mozny(dama, (1, 3), obsazene_pozice))  # False
    print(je_tah_mozny(dama, (3, 8), obsazene_pozice))  # True