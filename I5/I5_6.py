# Construa uma calculadora que efetue operações aritméticas entre dois números.
# Entrada: O programa deve receber um valor inteiro qualquer, seguido de um operador (que pode ser "+" para soma, "-" para subtração, "*" para multiplicação, "/" para divisão inteira, "%" para resto de divisão, ou "^" para exponenciação), seguido de outro número inteiro qualquer.
# Saída: A resposta deverá ser um único número inteiro, resultado da operação dada na entrada, ou a mensagem "erro" se não for possível realizar a conta (divisões por zero)

x = int(input())
z = input()
y = int(input())
soma = x + y
subtração = x - y
multiplicacão = x * y
exponenciação = x ** y
if z == "+":
    print(soma)
elif z == "-":
    print(subtração)
elif z == "*":
    print(multiplicacão)
elif z == "^":
    print(exponenciação)
if z == "/" and y == 0:
    print("erro")
elif z == "/" and y != 0:
    print(x//y)
elif z == "%" and y != 0:
    print(x%y)
elif z == "%" and y == 0:
    print("erro")