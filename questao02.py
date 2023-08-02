'''
Elaborar um programa que pergunte quatro valores e apresente 2 resultados:
a) O resultado de suas adições
b) O resultado de suas multiplicações
'''

#Input
num1 = float(input("Informe o primeiro valor"))
num2 = float(input("Informe o segundo valor"))
num3 = float(input("Informe o terceiro valor"))
num4 = float(input("Informe o quarto valor"))

#Cálculo
soma = num1 + num2 + num3 + num4
multi = num1 * num2 * num3 * num4

#Output
print("A soma dos valores é", soma)
print("O produto é", multi)
