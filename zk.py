def process_numbers(numbers):
    vysledek = []
    
    for cislo in numbers:
        if cislo == 10:
            break
        if cislo > 5:
            vysledek.append(cislo * 2)
            
    return vysledek

if __name__ == "__main__":
    print(process_numbers([1, 6, 3, 10, 8]))
    print(process_numbers([7, 8, 10, 12]))
    print(process_numbers([1, 2, 3, 4]))
    print(process_numbers([5, 6, 7, 15]))