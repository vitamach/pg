from paty import jaccardova_vzdalenost_mnozin
from paty1 import levensteinova_vzdalenost

def deduplikace_dotazu(dotazy):
    unikaty = []

    for i in range(len(dotazy)):
        je_unikatni = True

        for j in range(len(dotazy)):
            if i != j:
                jaccardova_vzdalenost = jaccardova_vzdalenost_mnozin(dotazy[i]["serp"], dotazy[j]["serp"])
                levensteinova = levensteinova_vzdalenost(dotazy[i]["dotaz"], dotazy[j]["dotaz"])

                if jaccardova_vzdalenost < 0.5 and levensteinova <= 1:
                    je_unikatni = False
                    break
        
        if je_unikatni:
            unikaty.append(dotazy[i])

    return unikaty


if __name__ == "__main__":

    dotaz1 = {
        "dotaz": "seznam",
        "serp": ["https://www.seznam.cz", "https://www.jcu.cz", "https://www.czu.cz", "https://www.cvut.cz", "https://www.uk.cz", "https://www.google.com"]
    }
    dotaz2 = {
        "dotaz": "seznamka",
        "serp": ["https://www.seznam.cz", "https://www.google.com", "https://www.novinky.cz", "https://www.idnes.cz", "https://www.zpravy.cz", "https://www.tn.cz"]
    }
    dotaz3 = {
        "dotaz": "sesnam",
        "serp": ["https://www.jcu.cz", "https://www.czu.cz", "https://www.cvut.cz", "https://www.uk.cz"]
    }
    vysledky = deduplikace_dotazu([dotaz1, dotaz2, dotaz3])

    for vysledek in vysledky:
        print(f"Dotaz: {vysledek['dotaz']}, SERP: {vysledek['serp']}")