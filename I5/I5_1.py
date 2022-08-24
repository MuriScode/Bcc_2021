#Alice e Bob querem jogar par ou ímpar.
#Alice sempre aposta no par e Bob no ímpar.
#Faça um programa que mostre quem é o ganhador em um jogo dos dois.
#Entrada: O programa deve receber inicialmente um inteiro, que é o valor escolhido pela Alice, e em seguida outro inteiro, que é o valor escolhido por Bob.
#Saída: A resposta deverá ser o nome do ganhador do jogo

a = int(input())
b = int(input())
# o int serve pra definir que o número a ser recebido é um inteiro, e o input é a função que irá receber esse inteiro.
d = a + b
if d % 2 == 0:
    print ("Alice")
else:
    print ("Bob")
# o if e else são condicionais (if = se) e (else = senão), o % significa resto da divisão.