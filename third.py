def je_prvocislo(cislo):
    if cislo < 2:
        return False
    for i in range(2, int(cislo**0.5) + 1):
        if cislo % i == 0:
            return False
    return True

def vrat_prvocisla(maximum):
    seznam = []
    for i in range(2, maximum + 1):
        if je_prvocislo(i):
            seznam.append(i)
    return seznam

if __name__ == "__main__":
    print(je_prvocislo(100)) 
    print(vrat_prvocisla(100))