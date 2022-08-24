# Escreva um programa que, dadas a nota da prova, da atividade e dos exercícios de um aluno de uma disciplina da UFABC que calcula o conceito final desse aluno antes da recuperação.
# Considere que a média final da disciplina é dada pela fórmula MF = 0.45 P + 0.25 A + 0.3 L sendo P a nota da prova, A a nota da atividade e L a média das listas de exercícios.
# E o conceito final é
# |     Conceito    |       Notas        |
# |         A       |    se MF >= 8.5    |
# |         B       | se 7.0 <= MF < 8.5 |
# |         C       | se 6.0 <= MF < 7.0 |
# |         D       | se 5.0 <= MF < 6.0 |
# |         F       | se 0.0 <= MF < 5.0 |
# Entrada: O programa deverá receber três números decimais positivos maiores ou iguais a 0 e menores ou iguais a 10, nessa ordem: P, A e L.
# Saída: Utilize o comando print("MF=",mf,"e conceito=",conceito) para mostrar o valor da MF e do conceito.
P = float(input())
A = float(input())
L = float(input())
# float é o tipo de dado real, ou seja que pode receber vírgula.
MF = (P*0.45) + (A*0.25) + (L*0.3)

if MF >= 8.5:
    conceito = "A"
    print("MF=", MF, "e conceito=", conceito)
elif 7.0 <= MF < 8.5:
    conceito = "B"
    print("MF=", MF, "e conceito=", conceito)
elif 6.0 <= MF < 7.0:
    conceito = "C"
    print("MF=", MF, "e conceito=", conceito)
elif 5.0 <= MF < 6.0:
    conceito = "D"
    print("MF=", MF, "e conceito=", conceito)
elif 0.0 <= MF < 5.0:
    conceito = "F"
    print("MF=", MF, "e conceito=", conceito)