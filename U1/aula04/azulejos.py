# Quantidade de Caixas de Azulejos:
# Escreva um programa para ler as dimensões de uma cozinha retangular (comprimento,
# largura e altura), calcular e escrever a quantidade de caixas de azulejos para se colocar em
# todas as suas paredes (considere que não será descontada a área ocupada por portas e
# janelas). Cada caixa de azulejos possui 1,5 m²

umacaixa = 1.5



comprimento = float(input("Digite o comprimento do cômodo em metros:"))
largura = float(input("Digite a largura do cômodo em metros:"))
altura= float(input("Digite a altura do cômodo em metros:"))


areapiso = (comprimento * largura)
areaparedes = (comprimento * altura *2) + (largura * altura *2)
caixa = 1.5
print(f"A área do cômodo em metros quadrados é: {areapiso + areaparedes}")
print(f"A quantidade de caixas de azulejos necessárias é: {(areapiso + areaparedes) / caixa}")