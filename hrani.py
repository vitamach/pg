#print(list(range(10,20,8)))

def my_cislo(start, stop, step):
    
    cislo = []

    if step > 0:
        while start < stop: 
            cislo.append(start)
            start += step
    
    elif step < 0:
        print(f"Zadej to znovu!")   

    return cislo 


start = int(input("Zadej start: "))
stop = int(input("Zadej stop: "))
step = int(input("zadej step"))

print(list(my_cislo(start, stop, step))) 