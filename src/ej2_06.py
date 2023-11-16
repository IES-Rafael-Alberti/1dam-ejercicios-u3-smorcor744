"""
Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura y elimine de la lista las asignaturas aprobadas. Al final el programa debe mostrar por pantalla las asignaturas que el usuario tiene que repetir.
"""
def pedir_lista():
    print("Dime las asignaturas (separadas por comas): ")
    asignaturas = input()
    return list(asignaturas.split(',')) 

def nota(asignaturas):
    notas = []
    for asignatura in asignaturas:
        print("Dime tu nota en " + asignatura)
        nota = float(input())
        notas.append(nota)
    return notas

def asignaturas_a_repetir(asignaturas, notas):
    asignaturas_a_repetir = []
    for i in range(len(asignaturas)):
        if notas[i] < 5.0:
            asignaturas_a_repetir.append(asignaturas[i])
    return asignaturas_a_repetir

def main():
    asignaturas = pedir_lista()
    notas = nota(asignaturas)
    asignaturas_repetir = asignaturas_a_repetir(asignaturas, notas)
    print("Tienes que repetir las siguientes asignaturas: " + ', '.join(asignaturas_repetir))

if __name__ == "__main__":
    main()
