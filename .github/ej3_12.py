"""Escribir un programa que almacene las matrices A=(123456) y B=(−100111) en una lista y muestre por pantalla su producto. Nota: Para representar matrices mediante listas usar listas anidadas, representando cada vector fila en una lista."""


def producto(matriz1, matriz2):
    """ 
    fila =[]
    for i in range(len(matriz1)):
        for j in range(2)
            suma = 0
            
            suma +="""
    return tuple(multiplicar(matriz1[i],matriz2[i]) for i in range(len(matriz1)))


def multiplicar(matriz1, matriz2):
    return tuple(matriz1[i]*matriz2[i] for i in range(len(matriz1)))

def main():
    matriz1 = ((1,2),(3,4),(5,6))
    matriz2 = ((-1,0),(0,1),(1,1))
    
    matriz3 = producto(matriz1, matriz2)
    print(str(matriz1)+" x "+str(matriz2)+" = "+ str(matriz3))


if __name__ == "__main__":
    main()