 #Cálculo de Média e Status do Estudante
#Dadas as 4 notas de um estudante, calcule sua média e, com base nela, emita a mensagem
#de status correspondente.
#1. Aprovado: Média estritamente maior que 7.
#2. Recuperação: Média entre 5 (inclusive) e 7 (inclusive).
#3. Reprovação: Média estritamente abaixo de 5

print("Saiba se está aprovado ou não!")

nota1 = float(input("Nota1:"))
nota2 = float(input("Nota2:"))
nota3 = float(input("Nota3:"))
nota4 = float(input("Nota4:"))

media = (nota1 + nota2 + nota3 + nota4) / 4

if media > 7:
    print("Parabéns! Você esta aprovado, te vejo no outro módulo!")
elif media >= 5 and media <= 7:
    print("Você está de recuperação,boa sorte! Prova na semana que vem!")
else:
    print("Você está reprovado, mas nunca é tarde para recomeçar")

print ("Sua média é:", media)
print("Nos vemos em breve!")