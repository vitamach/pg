def levensteinova_vzdalenost(dotaz1, dotaz2):
    rozdil = abs(len(dotaz1) - len(dotaz2))  # Rozdíl v délce řetězců

    # Projdeme znaky kratšího z obou řetězců a počítáme rozdíly
    for i in range(min(len(dotaz1), len(dotaz2))):
        if dotaz1[i] != dotaz2[i]:
            rozdil += 1  # Pokud jsou znaky rozdílné, zvýšíme rozdíl

    return rozdil

if __name__ == "__main__":
    query1 = "seznam"
    query2 = "seznamka"
    query3 = "sesnam"

    print(levensteinova_vzdalenost(query1, query2))  # Mělo by vrátit 2
    print(levensteinova_vzdalenost(query2, query3))  # Mělo by vrátit 3
    print(levensteinova_vzdalenost(query1, query3))  # Mělo by vrátit 1
