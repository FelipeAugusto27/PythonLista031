nome = "Carla Joaquina" # tipo str
idade = 27 # tipo inteiro
altura = 1.759 #tipo float

print(f"Tipo da variável nome: %s " % type(nome))
print(f"Tipo da variável nome: %s " % type(idade))
print(f"Tipo da variável nome: %s " % type(altura))

print("Nome: %s" % nome)
print("Idade: %d" % idade)
print("Altura: %.2f" % altura)
print("%s possui %d anos e tem %.2fm de altura" % (nome, idade, altura))
