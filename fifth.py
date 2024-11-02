import sys

class ChybaNeniObrazek(Exception):
    pass

def read_header(file_name, header_length):
    try:
        with open(file_name, "rb") as otevreny_soubor:
            return otevreny_soubor.read(header_length)
        
    except(FileNotFoundError, IOError):
        raise ChybaNeniObrazek("Nelze načíst soubor nebo neexistuje")

def detect_format(header):
    if header.startswith(b'\xff\xd8') and header.endswith(b'\xff\xd9'):
        return "JPEG"
    elif header.startswith(b'GIF87a') or header.startswith(b'GIF89a'):
        return "GIF"
    elif header.startswith(b'\x89PNG\r\n\x1a\n'):
        return "PNG"
    return "Neznámý formát"

if __name__ == "__main__":
    try: 
        file_name = sys.argv[1]
        header = read_header(file_name)

        format = detect_format

    except IndexError:
        raise ValueError("Zadej název souboru jako argument")
    
    except ChybaNeniObrazek as e:
        raise ChybaNeniObrazek(f"Chyba: {e}")
