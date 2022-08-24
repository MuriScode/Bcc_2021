# Faça um programa que indique se um ano é bissexto ou não.
# OBS: Todos os anos múltiplos de 400 são bissextos. Não sendo múltiplo de 400, são bissextos todos os anos múltiplos de 4 mas que não são múltiplos de 100.
# Entrada: O programa deve receber um único número inteiro que representa o ano desejado.
# Saída: A resposta deverá ser a palavra "SIM" ou "NÃO", indicando se o ano dado é bissexto ou não
anobissexto = int(input())
if anobissexto % 400 == 0:
    print("SIM")
elif anobissexto % 4 == 0 and anobissexto % 100 != 0:
    print("SIM")
else:
    print("NÃO")