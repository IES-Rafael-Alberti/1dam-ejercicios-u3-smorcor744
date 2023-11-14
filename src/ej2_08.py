def pedir_palabra():
    return list(input("Introduce una palabra: "))

def palabra_alreves(palabra):
    palabra = list(palabra)
    palabra.reverse()
    return palabra

def comprobar_palidromo(palabra, palabra2) -> bool:
    return "".join(palabra) == "".join(palabra2)


def main():


    
    palabra = pedir_palabra()
    palabra_original = tuple(palabra)
    palabra_alreves = [palabra]
    palabra_alreves.reverse()
    palabra_alreves(palabra)