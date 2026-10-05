#impot time
#time.sleep

#time /  os / random / sys
#main.py e init.py arquivos iniciadores (guardad em um e executado em outro)
# aspas triplas são para falar o qu a função faz '''   '''


import random 
numero_random = random.randint(1,30)

def sorteiame():
    '''
    escolhe e retorna um numero inteiro aleatorio no intervalo de 1 ate 30
    '''
    import random 

    numero_random = random.randint(1,30)

    return numero_random
#print(numero_random)]

resultado = sorteiame()
print(resultado)