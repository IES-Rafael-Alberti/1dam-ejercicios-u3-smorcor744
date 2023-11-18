"""Escribir un programa que almacene los vectores (1,2,3) y (-1,0,2) en dos listas y muestre por pantalla su producto escalar"""
def escalar(vec1, vec2):
    producto = []
    for i in range(len(vec1)):
        multi = vec1[i] * vec2[i]
        producto.append(multi)
    
    return producto


def main():
    vector1 = [1,2,3]
    vector2 = [-1,0,2]
    print(escalar(vector1,vector2))


if __name__ == "__main__":
    main()
