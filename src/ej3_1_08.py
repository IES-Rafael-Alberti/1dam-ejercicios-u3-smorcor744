"""Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un palíndromo."""


def pedir_palabra():
    return list(input("Introduce una palabra: "))


def palabra_alreves(palabra: str) -> list:
    palabra = list(palabra).reverse()
    return palabra


def comprobar_palidromo(palabra, palabra2) -> bool:
    return "".join(palabra) == "".join(palabra2)


def main():    
    palabra = pedir_palabra()
    palabra_original = tuple(palabra)
    palabra_alreves = [palabra]
    palabra_alreves.reverse()
    palabra_alreves(palabra)


if __name__ == "__main__":
    main()