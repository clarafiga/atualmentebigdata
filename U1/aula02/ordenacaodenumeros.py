#Ordenação de Três Números
#ecebidos 3 números inteiros, crie um programa que os mostre ordenados em ordem
#rescente.
# Dica: Este desafio exige que você use estruturas if aninhadas ou uma série de testes
#usando operadores de comparação para determinar qual número é o menor, o do
#eio e o maior.

num1 = int(input("Primeiro Número:"))
num2 = int(input("Segundo Número:"))
num3 = int(input("Terceiro Número:"))

if num1<=num2 and num1 <= num3:
    if num2<= num3:
        print (f"{num1}, {num2} , {num3}")
    else:
        print (f"{num1}, {num3} , {num2}")
elif num2 <= num1 and num2 <= num3:
    if num1 <= num3:
        print (f"{num2}, {num1} , {num3}")
else:
    if num1 <= num2:
        print (f"{num3}, {num1} ,{num2}")
    else:
        print (f"{num3}, {num2} ,{num1}")
print ("Completamente em Ordem")