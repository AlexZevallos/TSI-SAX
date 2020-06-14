from math import sqrt
numero=int(input("Ingresar un número : "))

a=sqrt(numero)
print(sqrt(numero))

if numero%a==0 :   #un numero entero entre un número decimal nunca ,me va a dar cero 
    raiz=True

else:
    raiz=False
print(raiz)
