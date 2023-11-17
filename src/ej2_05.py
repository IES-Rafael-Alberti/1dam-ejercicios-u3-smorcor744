"""
Escribir un programa que almacene en una lista los números del 1 al 10 y los muestre por pantalla en orden inverso separados por comas.
"""
def invertir_lista(lista: list):
    lista2 = lista.copy()
    lista2.reverse()
    return lista2


def main():
    lista = list(range(1,11))
    print(invertir_lista(lista))

if __name__ == "__main__":
    main()