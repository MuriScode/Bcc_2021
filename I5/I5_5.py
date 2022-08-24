# Escreva um programa que determina a data cronologicamente menor de duas datas fornecidas pelo usuário.
# Entrada: O programa deve receber seis valores inteiros, onde os três primeiros representam o dia, mês e ano da primeira data e os três últimos representam o dia, mês e ano da segunda data.
# Saída: A resposta deverá ser uma única linha com o texto com uso do comando print(d,"/",m,"/",a), indicando corretamente a menor das duas datas.
dia1 = int(input())
mes1 = int(input())
ano1 = int(input())
dia2 = int(input())
mes2 = int(input())
ano2 = int(input())
if ano1 > ano2:
    dia = dia2
    mes = mes2
    ano = ano2
else:
    dia = dia1
    mes = mes1
    ano = ano1
if ano1 == ano2:
    if mes1 > mes2:
        dia = dia2
        mes = mes2
        ano = ano2
    else:
        dia = dia1
        mes = mes1
        ano = ano1
if ano1 == ano2 and mes1 == mes2:
    if dia1 > dia2:
        dia = dia2
        mes = mes2
        ano = ano2
    else:
        dia = dia1
        mes = mes1
        ano = ano1
print(dia,"/",mes,"/",ano)