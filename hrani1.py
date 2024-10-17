def my_zip(*seznam):
    seznam = [list(it) for it in seznam]

    min_len = min(len(it) for it in seznam)

    vysledky = []

    for i in range(min_len):
      
        vysledky.append(tuple(it[i] for it in seznam))

    return vysledky

result = my_zip([1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12])
print(result)  


def podle_pismen(vysledky):
    abeceda = ["a", "b", "c", "d"]
    vysledek_slovnik = {}
  
    for i, pismeno in enumerate(abeceda):
        if i < len(vysledky): 
            vysledek_slovnik[pismeno] = vysledky[i]

    return vysledek_slovnik 

print(podle_pismen(result))
