"""Escribir un programa que pregunte una fecha en formato dd/mm/aaaa y muestre por pantalla la misma fecha en formato dd de <mes> de aaaa donde <mes> es el nombre del mes."""

def fecha():
    fech = input("Dime la fecha de hoy (dd/mm/aaaa): ")
    fech = fech.split("/")
    return {"dia":fech[0],"mes":fech[1],"año":fech[2]}


def main():
    dic = fecha()
    print(f"{dic["dia"]} de {dic["mes"]} de {dic["año"]}")


if __name__ == "__main__":
    main()