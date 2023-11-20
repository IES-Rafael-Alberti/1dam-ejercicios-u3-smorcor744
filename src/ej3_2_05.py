"""Escribir un programa que almacene el diccionario con los créditos de las asignaturas de un curso {'Matemáticas': 6, 'Física': 4, 'Química': 5} y después muestre por pantalla los créditos de cada asignatura en el formato <asignatura> tiene <créditos> créditos, donde <asignatura> es cada una de las asignaturas del curso, y <créditos> son sus créditos. Al final debe mostrar también el número total de créditos del curso."""

def creditos(asignaturas:dict):
    clave = asignaturas.keys()
    for clave in asignaturas:
        print(f"{clave} tiene {asignaturas[clave]} créditos.")


def creditos_totales(asignaturas:dict):
    suma = 0
    clave = asignaturas.keys()
    for clave in asignaturas:
        suma = suma + asignaturas[clave]
    return suma

def main():
    asignaturas = {'Matemáticas': 6, 'Física': 4, 'Química': 5}
    creditos(asignaturas)
    print(f"Créditos totales: {creditos_totales(asignaturas)}.")


if __name__ == "__main__":
    main()