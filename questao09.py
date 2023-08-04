'''
Fazer um algoritimo que pergunte 1 número simples e apresente:
a) O próprio número
b) O quadrado deste número
c) A raiz quadrada desse número
'''
import math

#Input
num = float(input("Escreva um número"))

#Cálculo
potencia = math.pow(num,2)
raiz = math.sqrt(num)

#Output
print("O número informado", num)
print("O quadrado do número informado é:", potencia)
print("A raiz quadrada do número informado é:", raiz)
