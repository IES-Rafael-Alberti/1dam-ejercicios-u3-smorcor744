"""Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla el mensaje Yo estudio <asignatura>, donde <asignatura> sobre cada una de las asignaturas de la lista."""

def pedir_lista():
    print("Dime las asignaturas (separadas por comas): ")
    asignaturas = input()
    return asignaturas


def hacer_lista(asignaturas: str) -> list:
    return list(asignaturas.split(','))


def yo(asignatura):
    for i in range(len(asignatura)):
        print("To estudio " + asignatura[i])
    
    return ""


def main():
    asignatura = pedir_lista()
    lista = hacer_lista(asignatura)
    print(yo(lista))


if __name__ == "__main__":
    main()