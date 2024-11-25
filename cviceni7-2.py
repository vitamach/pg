class ImutableInteger:
    def __init__(self, number):
        self.__number = number
        self.imutable = True  
         
    @property 
    def number(self):
        return self.__number
    
    @number.setter
    def number(self, new_number):
        if self.__imutable:
            raise ValueError("Nelze měnit hodnotu, když je imutable=True")
        self.__number = new_number
    
    @property
    def imutable(self):
        return self.__imutable
    
    @imutable.setter
    def imutable(self, value):
        if not isinstance(value, bool):
            raise TypeError("Hodnota imutable musí být boolean")
        self.__imutable = value

if __name__ == "__main__":
    # Test funkčnosti
    ii = ImutableInteger(5)
    print("Původní hodnota:", ii.number)  # Vypíše 5
    
    try:
        ii.number = 60  # Vyvolá výjimku, protože imutable je True
    except ValueError as e:
        print("Test 1 (očekávaná výjimka):", e)
    
    ii.imutable = False  # Vypneme zamykání
    ii.number = 60  # Teď už projde
    print("Nová hodnota po změně:", ii.number)  # Vypíše 60
    
    ii.imutable = True  # Znovu zamkneme
    try:
        ii.number = 100  # Opět vyvolá výjimku
    except ValueError as e:
        print("Test 2 (očekávaná výjimka):", e)