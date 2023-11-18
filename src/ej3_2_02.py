"""Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde en un diccionario. Después debe mostrar por pantalla el mensaje <nombre> tiene <edad> años, vive en <dirección> y su número de teléfono es <teléfono>."""


def info():
    nom = input("Dime tu nombre: ")
    ed = input("Dime tu edad: ")
    direc = input("Dime tu dirección: ")
    tel = input("Dime tu teléfono: ")
    return dict(nombre=nom, edad=ed, direccion=direc, telefono=tel)


def main():
    datos = info()
    print(f"{datos["nombre"]} tienes {datos["edad"]} años, vive en {datos["direccion"]} y su número de teléfono es {datos["telefono"]}.")


if __name__ == "__main__":
    main()