"""Escribir un programa que pida al usuario una palabra y muestre por pantalla el número de veces que contiene cada vocal."""


def pedir_palabra() -> list:
    palabra = input("Introduce una palabra: ").strip().lower()
    palabra = palabra.replace("á", "a").replace("é", "e").replace("í", "i").replace("ó", "o").replace("ú", "u")
    return tuple(palabra)


def cont_vocales(palabra: tuple) -> tuple:
    vocales = (["a",0],["e",0],["i",0],["o",0],["u",0])

    for vocal in vocales:
        vocal[1] = palabra.count(vocal[0])
        print(vocal[0] + " = " + str(vocal[1]))

    return vocales


def main():
    palabra = pedir_palabra()
    vocales = cont_vocales(palabra)
    print(vocales)


if __name__ == "__main__":
    main()