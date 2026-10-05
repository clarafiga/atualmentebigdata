#Simule um sistema de login simples onde o usuário tem um número limitado de tentativas
#para digitar a senha correta.
#● Defina um nome de usuário e uma senha corretos (ex: admin e 123456).
#● Dê ao usuário 3 tentativas para acertar a combinação.
#● Se a senha estiver correta, imprima uma mensagem de sucesso e use o comando
#break para sair do loop.
#● Se a senha estiver errada, informe o erro e diminua o número de tentativas
#restantes.
#● Se as tentativas acabarem, imprima uma mensagem de bloqueio

login = "figaclara"
senha =  "sherlocked"
tentativa = 3

for tentativa in range (3):
    login1 = input("Bem-Vindo ao Sistema. Login:")
    senha1 = input("Senha:")

    if login1 == login and senha1 == senha:
        print ("Sucesso, logado!")
        break

    else:  
        tentativa - 1
        print ("Login ou senha incorretos, tente novamente!")

    if tentativa == 2:
        print("Cancelado!!")