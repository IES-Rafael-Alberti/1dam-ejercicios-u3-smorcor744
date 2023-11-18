"""Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla."""

def pedir_lista():
    print("Dime las asignaturas (separadas por comas): ")
    asignaturas = input()
    return asignaturas

def hacer_lista(asignaturas: str) -> list:
    return asignaturas.split(',')


def main():
    asignatura = pedir_lista()
    print(hacer_lista(asignatura))


if __name__ == "__main__":
    main()