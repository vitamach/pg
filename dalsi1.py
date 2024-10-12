def naformatuj_text(student):
    Jmeno = student["jmeno"]  
    Prijmeni = student["prijmeni"]
    Vek = student["vek"]
    prumer = round(sum(student["znamky"]) / len(student["znamky"]),1)
    

    return f"Jmeno {Jmeno}, prijmeni {Prijmeni} ve věku {Vek} má průměr {prumer}"

if __name__ == "__main__":
    
    student = {
        "jmeno": "Matěj",
        "prijmeni": "Dvořák",
        "vek": 21,
        "znamky": [1, 2, 1, 1, 3, 2]
    }
    print(naformatuj_text(student))
