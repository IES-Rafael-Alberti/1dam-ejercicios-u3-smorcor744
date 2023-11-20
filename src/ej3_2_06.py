"""Escribir un programa que cree un diccionario vacío y lo vaya llenado con información sobre una persona (por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.) que se le pida al usuario. Cada vez que se añada un nuevo dato debe imprimirse el contenido del diccionario."""

def info(datos: dict):
    nom = input("Dime tu nombre: ")
    datos["nombre"] = nom
    print(datos)
    ed = input("Dime tu edad: ")
    datos["edad"] = ed
    print(datos)
    sex = input("Dime tu sexo: ")
    datos["sexo"] = sex
    print(datos)
    tel = input("Dime tu teléfono: ")
    datos["telefono"] = tel
    print(datos)


def main():
    datos = {}
    info(datos)


if __name__ == "__main__":
    main()