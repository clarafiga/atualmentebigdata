#Escreva um programa para calcular e imprimir o número de lâmpadas necessárias para
#iluminar um determinado cômodo de uma residência. Dados de entrada: a potência da
#lâmpada utilizada (em watts), as dimensões (largura e comprimento, em metros) do
#cômodo. Considere que a potência necessária é de 3 watts por metro quadrado e a cada
#3m² existe um bocal para uma lâmpada.

#variaveis largura comprimento e watts 
#Potencia 3

#1m  3
#3   x
#x=9

#tamanho referencia1 menor ou igual  3x3 =  entao 1 lampada


largura = float(input("Por favor,adicione a largura do seu cômodo em metros!"))
comprimento = float(input("Por favor,adicione o comprimento do seu cômodo em metros!"))
potencia = POTENCIA = 3
area = largura * comprimento
potencianecessaria = area * 3
numero_lampadas = int((potencianecessaria + potencia - 1) // potencia)

print(f"{numero_lampadas} lâmpadas são necessárias para iluminar todo o seu cômodo.")