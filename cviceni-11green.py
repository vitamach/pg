def je_sude(cislo):
    return cislo % 2 == 0

def test_sudy_lichy():
    # Test sudých čísel
    assert je_sude(0) == True
    assert je_sude(2) == True
    assert je_sude(4) == True
    assert je_sude(100) == True
    
    # Test lichých čísel
    assert je_sude(1) == False
    assert je_sude(3) == False
    assert je_sude(99) == False

if __name__ == '__main__':
    test_sudy_lichy()
    print("Všechny testy prošly!")