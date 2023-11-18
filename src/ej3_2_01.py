"""Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, pregunte al usuario por una divisa y muestre su símbolo o un mensaje de aviso si la divisa no está en el diccionario."""

def tipo_moneda(monedas: dict):
    print("Dime la divisa: ")
    divisa = input()
    if divisa in monedas:
        
        return print(monedas[divisa])
    
    else:
        return print("La divisa no está en el diccionario")






def main():
    monedas = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
    tipo_moneda(monedas)


if __name__ == "__main__":
    main()