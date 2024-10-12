# funkce vrati treti prvek ze seznamu
def vrat_treti(seznam):
    if len(seznam) <= 2:
        print("Nejde")
    else:
        return seznam[2]


# funkce spocita prumer z hodnot v seznamu
def udelej_prumer(seznam):
    return None

# funkce naformatuje retezec, aby vratila text ve formatu:
# "Jmeno: Jan, Prijmeni: Novak, Vek: 20, Prumerna znamka: 2.5"
def naformatuj_text(slovnik):
    return ""


if __name__ == "__main__":
    print(vrat_treti([9,8,7,6]))
    print(udelej_prumer([9,8,7,6,5]))
    student = {
        "jmeno": "Matěj",
        "prijmeni": "Dvořák",
        "vek": 21,
        "znamky": [1, 2, 1, 1, 3, 2]
    }
    print(naformatuj_text(student))
