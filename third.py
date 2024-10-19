def je_prvocislo(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

def vrat_prvocisla(maximum):
    seznam = []
    for i in range (2, maximum + 1):
        if je_prvocislo(i):
            seznam.append(i)
    return seznam

if __name__ == "__main__":
    n = int(input("Zadej číslo: "))
    maximum = int(input("Zadej maximální číslo: "))

    if je_prvocislo(n):
        print("True")
    else:
        print("False")

    print(f"Prvočísla do {maximum}: {",".join(map(str,vrat_prvocisla(maximum)))}")

