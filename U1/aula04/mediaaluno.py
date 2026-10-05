#Escreva um programa que leia as notas das duas avaliações normais e a nota da avaliação
#optativa dos estudantes de uma turma. Caso o estudante não tenha feito a optativa, deve
#ser fornecido o valor -1. Calcular a média do semestre considerando que a prova optativa
#substitui a nota mais baixa entre as duas primeiras avaliações. Escrever a média e
#mensagens que indiquem se o estudante foi aprovado, reprovado ou se está em
#recuperação, de acordo com as informações abaixo:
#Aprovado: média >= 6.0
#Reprovado: média < 3.0
#Recuperação: média >= 3.0 e < 6.0
#Observação: nota optativa - o estudante decide fazer uma prova extra para melhorar o
#resultado final.
#6. Positivo ou N


nota1 = float(input("Digite a nota da primeira avaliação: "))
nota2 = float(input("Digite a nota da segunda avaliação: "))
notaopt = float(input("Digite a nota da avaliação optativa:"))

if notaopt <= -1:
    if notaopt > nota1 or notaopt > nota2:
        nota1 = notaopt

media = (nota1 + nota2) or (nota1 + notaopt) or (nota2 + notaopt) / 2
if media >= 6.0:
    print("Aprovado, parabéns!")

elif media < 3.0:
    print("Reprovado, nos vemos ano que vem!")

else:
    print("Recuperação, ainda tem mais uma chance, boa sorte!")
print("A média do semestre é: ", media)