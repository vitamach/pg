import sys

def pozpatku(text):
    text_pozpatku = ""
    for pismeno in reversed(text):
        text_pozpatku += pismeno
    return text_pozpatku

if __name__ == "__main__":
    try:
            soubor = sys.argv[1]
            with open(soubor, "r") as fp:
                obsah = fp.read()
                print(obsah)
                obracene = pozpatku(obsah)
                print(obracene)

    except IndexError:
        print("Zadejte novaz souboru")

    except FileNotFoundError:
         print("Soubor neexistuje")
