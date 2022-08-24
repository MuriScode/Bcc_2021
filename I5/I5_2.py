# Faça um programa que ordene 3 números inteiros. Não utilize a função abs().
# Entrada: O programa deve receber três números inteiros.
# Saída: A reposta deve ser os três números, escritos na mesma linha, em ordem crescente.
# Dica: Utilize os comandos:
# a=int(input())
# print(a,b,c)
a = int(input())
b = int(input())
c = int(input())
if a > b and a > c and b >= c:
    print(c,b,a)
    # se a for > b e a for > c e b for >= c
    # print c b a
    # essa é a lógica.
elif a > b and a > c and c >= b:
    print(b,c,a)
elif b > a and b > c and a >= c:
    print(c,a,b)
elif b > a and b > c and c >= a:
    print(a,c,b)
elif c > a and c > b and b >= a:
    print(a,b,c)
else:
    print(b,a,c)