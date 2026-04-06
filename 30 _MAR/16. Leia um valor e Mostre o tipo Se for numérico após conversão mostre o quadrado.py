#16. Leia um valor e: Mostre o tipo; Se for numérico (após conversão) → mostre o quadrado.

valor = (input ("Insira um valor"))

print ("O tipo de dado, após a conversão é", type(valor))

if valor.replace ('.','', 1).isdigit():
    numero = float (valor)
    print (("O valor ao quadrado é"), numero ** 2)
else:
    print ("Entrada Inválida")
