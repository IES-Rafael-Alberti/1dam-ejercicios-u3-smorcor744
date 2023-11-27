"""Dado el conjunto de números enteros:

numeros = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
Crea un conjunto pares que contenga los números pares del conjunto numeros.
Crea un conjunto multiplos_de_tres que contenga los números que son múltiplos de tres del conjunto numeros.
Encuentra la intersección entre los conjuntos pares y multiplos_de_tres y guárdala en un conjunto llamado pares_y_multiplos_de_tres."""

def par(numeros:set) -> set:
    pares = set()
    for numero in numeros:
        if numero % 2 == 0:
            pares.add(numero)
    return pares


def multiplo3(numeros:set) -> set:
    impar = set()
    for numero in numeros:
        if numero % 3 == 0:
            impar.add(numero)
    return impar


def main():
    numeros = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
    pares = par(numeros)
    print(pares)
    multiplos_de_tres = multiplo3(numeros)
    print(multiplos_de_tres)
    pares_y_multiplos_de_tres = pares.intersection(multiplos_de_tres)
    print(pares_y_multiplos_de_tres)

if __name__ == "__main__":
    main()