'''
Fazer um programa que pergunte oo salário de um funcionário e apresente este salário com um aumento de % 15
'''

#Input
sal = float(input("Informe o seu salário: R$"))

#Cálculo
aumento = sal + (sal * 15/100)

#Output
print("O aumento do seu salário é de R$", aumento)