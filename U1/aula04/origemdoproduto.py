#4. Código de Origem do Produto:
#Escreva um programa que leia o código de origem de um produto e imprima na tela a região
#de sua procedência, conforme a tabela abaixo:
#Observação: caso o código não seja nenhum dos especificados, o produto deve ser
#encarado como “Importado”.

regioes = {1: "Sul" ,
            2: "Norte" ,
            3: "Leste" ,
            4: "Oeste" ,
            5 or 6 : "Nordeste" ,
            7 or 8 or 9: "Sudeste", 
            10: "Centro Oeste", 
            11: "Noroeste" }

codigo = int(input ("Código do produto:"))
if codigo == 1:
    print("Esse produto é do: Sul")
elif codigo == 2:
    print("Esse produto é do: Norte")
elif codigo == 3:
    print("Esse produto é do: Leste")
elif codigo == 4:
    print("Esse produto é do: Oeste")
elif codigo == 5 or codigo == 6:
    print("Esse produto é do: Nordeste")
elif codigo == 7 or codigo == 8 or codigo == 9:
    print("Esse produto é do: Sudeste")
elif codigo == 10:
    print("Esse produto é do: Centro-Oeste")
elif codigo == 11:
    print("Esse produto é do: Noroeste")
else:
    print("Esse produto é Importado!")