"""Dado el conjunto de letras:

vocales = {'a', 'e', 'i', 'o', 'u'}
Crea un conjunto consonantes que contenga las letras del alfabeto que no son vocales.
Crea un conjunto letras_comunes que contenga las letras que están tanto en el conjunto vocales como en el conjunto consonantes.
Estos ejercicios te ayudarán a practicar y comprender mejor cómo trabajar con conjuntos en Python. ¡Espero que te sean útiles! Si tienes alguna pregunta o necesitas más ejercicios, no dudes en decírmelo."""






def main():
    vocales = {'a', 'e', 'i', 'o', 'u'}
    alfabeto = set('abcdefghijklmnopqrstuvwxyz')
    consonantes = alfabeto - vocales
    print(consonantes)
    letras_comunes = alfabeto & vocales 
    print(letras_comunes)


if __name__ == "__main__":
    main()