"""Escribir un programa que pida al usuario una palabra y muestre por pantalla el número de veces que contiene cada vocal."""


def pedir_palabra() -> list:
    palabra = tuple(input("Introduce una palabra: "))
    return palabra


def cont_vocales(palabra: tuple) -> tuple:
    vocales = (["a",0],["e",0],["i",0],["o",0],["u",0])
    for vocal in vocales:
        vocal[1] = palabra.count(vocal[0])
    return vocales


def main():
    palabra = pedir_palabra()
    vocales = cont_vocales(palabra)
    print(vocales)


if __name__ == "__main__":
    main()