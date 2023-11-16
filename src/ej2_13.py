"""Escribir un programa que pregunte por una muestra de números, separados por comas, los guarde en una lista y muestre por pantalla su media y desviación típica."""

def pedir_lista():
    print("Dame números(separadas por comas): ")
    num = input()
    return list(num.split(',')) 


def media(num:list):
    suma = 0.0
    for i in range(len(num)):
        suma += float(num[i])
    return suma / len(num)

def desviacion_tipica(numeros):
    
    return 


def main():
    numeros = pedir_lista()
    print("La media es: ", media(numeros))
    #print("La desviación típica es: ", desviacion_tipica(numeros))

if __name__ == "__main__":
    main()