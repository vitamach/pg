def operace(typ, a, b):
    if typ == "+":
        vysledek = a + b
    elif typ == "-":
        vysledek = a - b
    elif typ == "*":
        vysledek = a * b
    elif typ == "/":
        if b == 0:
            vysledek = "Nelze dělit nulou!"
        else:
            vysledek = a / b
    else:
        vysledek = "Neplatná operace"
    return vysledek

if __name__ == "__main__":
    try:
        typ = input("Zadej operaci (+, -, *, /): ")
        a = float(input("Zadej první číslo: "))
        b = float(input("Zadej druhé číslo: "))
        
        vysledek = operace(typ, a, b)
        print(f"Výsledek: {vysledek}")
        
    except ValueError:
        print("Zadej prosím platná čísla")