class BadDataError(Exception):
    pass

class Souradnice:
    def __init__(self, sirka, delka):
        # Použijeme předponu '_' pro označení private proměnných
        self._sirka = sirka
        self._delka = delka

    def __str__(self) -> str:
        return f'Souradnice: {self._sirka}, {self._delka}'
    
    # Property getter pro šířku
    @property
    def sirka(self):
        return self._sirka
    
    # Property setter pro šířku
    @sirka.setter
    def sirka(self, hodnota):
        if not isinstance(hodnota, (int, float)):
            raise TypeError("Šířka musí být číslo")
        if hodnota < 0:
            raise ValueError("Šířka nemůže být záporná")
        self._sirka = hodnota
    
    # Property getter pro délku
    @property
    def delka(self):
        return self._delka
    
    # Property setter pro délku
    @delka.setter
    def delka(self, hodnota):
        if not isinstance(hodnota, (int, float)):
            raise TypeError("Délka musí být číslo")
        if hodnota < 0:
            raise ValueError("Délka nemůže být záporná")
        self._delka = hodnota
    
    @classmethod
    def nacti_z_dat(cls, data):
        if "souradnice" not in data:
            raise BadDataError
        souradnice = data["souradnice"]
        if not isinstance(souradnice, dict):
            raise BadDataError
        if "sirka" not in souradnice or "delka" not in souradnice:
            raise BadDataError
        return cls(souradnice["sirka"], souradnice["delka"])

if __name__ == "__main__":
    # Příklad použití
    data = {"souradnice": {"sirka": 50, "delka": 50}}
    s = Souradnice.nacti_z_dat(data)
    print(s)
    
    # Ukázka použití getterů
    print(f"Původní šířka: {s.sirka}")
    print(f"Původní délka: {s.delka}")
    
    # Ukázka použití setterů
    s.sirka = 60  # Použije setter pro změnu šířky
    s.delka = 70  # Použije setter pro změnu délky
    print(f"Nová šířka: {s.sirka}")
    print(f"Nová délka: {s.delka}")
    