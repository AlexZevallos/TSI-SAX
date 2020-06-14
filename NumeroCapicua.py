numero=int(input("Ingrese:"))

def capicúa(num):
    if numero>=0:
        if str(num)==str(num)[::-1]:
            cap=True
        else:
            cap=False

    else:
        print("el numero debe de ser positivo")
    return cap

print(numero, "es capicúa?", capicúa(numero))
