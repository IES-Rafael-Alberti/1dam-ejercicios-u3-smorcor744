"""Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, pregunte al usuario por una fruta, un número de kilos y muestre por pantalla el precio de ese número de kilos de fruta. Si la fruta no está en el diccionario debe mostrar un mensaje informando de ello."""

def pedir_fruta(frutas: dict):
    fruta = input("Dime una fruta: ")
    if fruta in frutas:
        peso = float(input("Dime el número de kilos de esa fruta: "))
        for fruta in frutas:
            coste = frutas[fruta] * peso
        return print(f"{coste}€")
    else:
        return print("No tenemos esa fruta")


def main():
    fruta = {"platano":1.35,"manzana":0.80,"pera":0.85,"naranja":0.70}
    pedir_fruta(fruta)


if __name__ == "__main__":
    main()