"""Solicitar al usuario que introduzca los nombres de pila de los alumnos de primaria de una escuela, finalizando cuando se introduzca “x”. A continuación, solicitar que introduzca los nombres de los alumnos de secundaria, finalizando al introducir “x”.

Mostrar los nombres de todos los alumnos de primaria y los de secundaria, sin repeticiones.
Mostrar qué nombres se repiten entre los alumnos de primaria y secundaria.
Mostrar qué nombres de primaria no se repiten en los de nivel secundaria.
Mostrar si todos los nombres de primaria están incluidos en secundaria."""

def nombres_primaria():
    nombres1 = []
    continuar = True
    while continuar:
        nombre = input("Introduce un nombre de pila de los alumnos de primaria(x para pasar a los de secundaria): ")
        if nombre == "x":
            continuar = False
        else:
            nombres1.append(nombre)
    return nombres1

def nombres_secundaria():
    nombres2 = []
    continuar = True
    while continuar:
        nombre = input("Introduce un nombre de pila de los alumnos de secundaria(x para terminar): ")
        if nombre == "x":
            continuar = False
        else:
            nombres2.append(nombre)
    return nombres2

def nombres_totales_sinrep(nombres_secundaria: list, nombres_primaria:list) -> set:
    nombres_sinrep = set(nombres_primaria + nombres_secundaria)
    return nombres_sinrep 

def nombres_primaria_en_secundaria(nombres_secundaria: list, nombres_primaria:list):
    if set(nombres_primaria).issubset(set(nombres_secundaria)):
        print("Todos los nombres de primaria están incluidos en secundaria.")
    else:
        print("No estan todos los nombres de primaria están incluidos en secundaria.")

def nombres_primaria_norep(nombres_secundaria: list, nombres_primaria:list):
    nombres = set(nombres_primaria) - set(nombres_secundaria)
    return nombres

def nombres_rep(nombres_secundaria: list, nombres_primaria:list):
    nombres = set(nombres_primaria).intersection(set(nombres_secundaria))
    return nombres


def main():
    primaria = nombres_primaria()
    secundaria = nombres_secundaria()
    print("Nombres de primaria: ", primaria)
    print("Nombres de secundaria: ", secundaria)
    print("Nombres totales sin repeticiones: ", nombres_totales_sinrep(secundaria, primaria))
    print("Nombres que se repiten entre primaria y secundaria: ", nombres_rep(secundaria, primaria))
    print("Nombres de primaria que no se repiten en secundaria: ", nombres_primaria_norep(secundaria, primaria))
    nombres_primaria_en_secundaria(secundaria, primaria)

if __name__ == "__main__":
    main()
