def fibonacci(maximum):
    if maximum < 1:
        return []
    if maximum == 1:
        return [1]
    sequence = [1, 1]
    
    # Dokud je součet posledních dvou čísel menší nebo roven maximu
    while True:
        # Vypočítáme další číslo v posloupnosti
        next_num = sequence[-1] + sequence[-2]

        if next_num > maximum:
            break
        # Přidáme číslo do posloupnosti
        sequence.append(next_num)
    
    return sequence

if __name__ == "__main__":
    print("Maximum:", fibonacci(13)) 
