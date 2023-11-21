"""Escribir un programa que cree un diccionario de traducción español-inglés. El usuario introducirá las palabras en español e inglés separadas por dos puntos, y cada par <palabra>:<traducción> separados por comas. El programa debe crear un diccionario con las palabras y sus traducciones. Después pedirá una frase en español y utilizará el diccionario para traducirla palabra a palabra. Si una palabra no está en el diccionario debe dejarla sin traducir."""


def crear_diccionario(palabras:str) -> dict:
    diccionario = dict((par.split(":") for par in palabras.split(",")))
    return diccionario


def traducirFrase(frase:str,diccionario:dict):
    palabras = frase.split(" ")
    traducido = []
    for palabra in palabras:
        traducido.append(diccionario.get(palabra,palabra))
    frase_final = " ".join(traducido)
    return frase_final


def main():
    palabras = input("Dame la traducción español-inglés(separadas por dos puntos): ")
    diccionario = crear_diccionario(palabras)
    frase = input("Dame uan frase para traducirla: ")
    print(traducirFrase(frase,diccionario))


if __name__ == "__main__":
    main()