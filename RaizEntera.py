from math import sqrt
numero=int(input("Ingresar un número : "))

a=sqrt(numero)
print(sqrt(numero))

if numero%a==0: 
    raiz=True

else:
    raiz=False
print(raiz)
