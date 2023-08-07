'''
Fazer um algoritimo que efetue o calculo do valor de uma prestação em atraso utilizando a fórmula
prestação = valor + (valor x (taxa : 100) x tempo em dias).
'''

#Input
valor = float(input("Informe o valor da prestação R$ "))
taxa = float(input("Informe a taxa de juros "))
dias = float(input("Informe a quantidade de dias de atraso "))

#Cálculo
prest = valor + (valor * (taxa / 100) * dias)

#Output
print("O valor da prestação com atraso de", int(dias) , "dia(s) é de R$", prest)
