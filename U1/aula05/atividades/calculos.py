#Use o laço for para repetir a lógica de cálculo de média e status
#(Aprovado/Reprovado/Recuperação) que você fez na Aula 4, agora para 10 estudante

for i in range(10):
    print("Média Escolar!")
    nome = input("Nome: ")
    nota1 = float(input("Primeira nota: "))
    nota2 = float(input("Segunda nota: "))
    nota3 = float(input("Terceira nota: "))

    media = (nota1 + nota2 + nota3) / 3

    if media >= 7:
        status = "Aprovado! Parabéns!"
    elif media >= 5:
        status = "Recuperação, ainda tem mais um chance!"
    else:
        status = "Reprovado, nos vemos ano que vem!"

    print(f"Estudante: {nome}, Média: {media}, Status: {status}")