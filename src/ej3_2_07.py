"""Escribir un programa que cree un diccionario simulando una cesta de la compra. El programa debe preguntar el artículo y su precio y añadir el par al diccionario, hasta que el usuario decida terminar. Después se debe mostrar por pantalla la lista de la compra y el coste total, con el siguiente formato"""

def compra(lista: dict):
    continuar = True
    while continuar:
        articulo = input("Dime un articulo que hallas comprado: ")
        if articulo == "":
            continuar = False
        else:
            precio = float(input("Dime su precio:"))
            lista[articulo] = precio
    return lista

def main():
    lista = {}
    compra(lista)
    total = sum(lista.values())
    print("Lista de la compra:")
    i = 1
    for articulo, precio in lista.items():
        print(f"Artículo {i}: {articulo}, Precio: {precio}€")
        i += 1
    print(f"Coste total: {total}")

if __name__ == "__main__":
    main()
