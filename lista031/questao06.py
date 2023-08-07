'''
Fazer um programa que pergunte uma temperatura ao usuário, em grais Fahrenheit, e apresente esta temperatura convertida em gráus Celsius. A formula da conversão é
'''

#Input
f = float(input("Informe a temperatura em graus Fahrenheit:"))

#Cálculo
c = (f -32) * 5 / 9

#Output
print("A temperatura em Celsius é de: C", c)
