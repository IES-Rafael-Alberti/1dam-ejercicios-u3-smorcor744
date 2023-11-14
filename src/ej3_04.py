"""
Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.
"""


def pedir_numero(lista):
    while True:
        try:
            num = int(input("Introduce los números: "))

            if not 1 <= num <= 49:
                raise ValueError
            if num in lista:
                raise ValueError
            return num
        except ValueError:
            print("**Error**")


def crear_lista():
    lista = []
    for i in range(6):
        lista.append(pedir_numero(lista))
    return lista


def main():
    lista = crear_lista()
    lista.sort()
    print("Los números ganadores ordenados de menor a mayor son:", lista)


if __name__ == "__main__":
    main()