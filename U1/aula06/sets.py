#SETS

#elimina duplicatas e veriica a presença de itens rapidamente, a orde dos itens não é garantida.

numerospares = {
    202,
    203,
    204,
    204,
    205,
    219,
    291,
    292,
    202
}
#print(numerospares, type (numerospares))

numimpares = {111, 111, 112, 291,291,205}
print (numimpares.intersection (numerospares))
numerospares.remove (205)
print(numerospares)