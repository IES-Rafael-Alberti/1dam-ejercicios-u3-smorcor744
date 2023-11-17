"""Escribir un programa que almacene en una lista los siguientes precios: 50, 75, 46, 22, 80, 65, 8 y muestre por pantalla el menor y el mayor de los precios."""

def main():
    precios = [50, 75, 46, 22, 80, 65, 8]
    precios.sort()
    print(f"El precio menor es {precios[0]}")
    print(f"El precio mayor es {precios[-1]}")


if __name__ == "__main__":
    main()