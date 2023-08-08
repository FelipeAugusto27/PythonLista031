a = 3
b = -4

# Operadores Aritméticos
soma = a + b
sub = a - b
mult = a * b
div = a / b
div_inteiros = a // b

print(f"Soma: {soma}")  # 3 + (-4) = -1
print(f"Subtração: {sub}")  # 3 - (-4) = 3 + 4 = 7
print(f"Multiplicação: {mult}")  # 3 * -(4) = -16
print(f"Divisão: {div}")
print(f"Divisão de inteiros: {div_inteiros}")
print(f"Calculos dentro do print {a*b}")
print(f"Resto da divisão de 16 por a: {16 % a}")

print("")
# Operadores Relacionais
print(f"a == b: {a == b}")
print(f"a < 5: {a < 5}")
print(f"a > b: {a > b}")
print(f"a <= 3: {a <= 3}")
print(f"a >= 4: {a >= 4}")
print(f"a != b: {a !=b}")

c = a != b
print(f"c: {c}")
print(f"Tipo da variavel c: {type(c)}")  # Bool é booleano ou lógico

#  Operadores Lógicos
logic1 = True
logic2 = False
print(f"type(logic1) {type(logic1)}")
print(f"type(logic2) {type(logic2)}")

print(f"logic1: {logic1}")
print(f"logic1: {not logic1}")
print(f"logic1 or logic2 {logic1 or logic2}")
print(f"logic1 and logic2 {logic1 and logic2}")
