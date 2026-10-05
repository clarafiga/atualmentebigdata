# Rendimento do Taxista:
#Um motorista de táxi deseja calcular o rendimento de seu carro na praça. Sabendo-se que o
#preço do combustível é de R$ 6,15, escreva um programa para ler: a marcação do
#odômetro (km) no início do dia, a marcação (km) no final do dia, o número de litros de
# combustível gasto e o valor total (R$) recebido dos passageiros. Calcular e escrever: a
# média do consumo em km/L e o lucro (líquido) do dia.

#descobrir:
# distancia percorrida
#valor do combustivel
#quanto gastou de combustivel
# total recebido dos passageiros
# media de consumo


litro = 6.15
dia = float(input("Odômetro no início do dia: "))
fim = float(input("Odômetro no final do dia: "))
valor = float(input("Valor total do combustível gasto: "))
reais = float(input("Valor total recebido dos passageiros: "))

combustivel = litro * valor
distancia = fim - dia
media = distancia / combustivel
lucro = reais - combustivel
print(f"A média do consumo é de {media:.2f} km/l.")
print(f"O lucro do dia é de R$ {lucro:.2f}.")