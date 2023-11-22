"""Escribir un programa que gestione las facturas pendientes de cobro de una empresa. Las facturas se almacenarán en un diccionario donde la clave de cada factura será el número de factura y el valor el coste de la factura. El programa debe preguntar al usuario si quiere añadir una nueva factura, pagar una existente o terminar. Si desea añadir una nueva factura se preguntará por el número de factura y su coste y se añadirá al diccionario. Si se desea pagar una factura se preguntará por el número de factura y se eliminará del diccionario. Después de cada operación el programa debe mostrar por pantalla la cantidad cobrada hasta el momento y la cantidad pendiente de cobro."""

def agregar_factura(facturas):
    numero = input("Introduce el número de la factura: ")
    coste = float(input("Introduce el coste de la factura: "))
    facturas[numero] = coste
    return facturas

def pagar_factura(facturas):
    numero = input("Introduce el número de la factura que quieres pagar: ")
    if numero in facturas:
        print(facturas[numero])
        del facturas[numero]
    else:
        print("La factura no existe.")
    return facturas

def main():
    facturas = {}
    terminar = True
    while terminar:
        print("\n1. Añadir factura")
        print("2. Pagar factura")
        print("3. Ver facturas")
        print("4. Salir\n")
        opcion = input("Elige una opción: ")
        if opcion == '1':
            facturas = agregar_factura(facturas)
        elif opcion == '2':
            facturas = pagar_factura(facturas)
        elif opcion == '3':
            print(facturas)
        elif opcion == '4':
            terminar = False
        else:
            print("Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    main()
