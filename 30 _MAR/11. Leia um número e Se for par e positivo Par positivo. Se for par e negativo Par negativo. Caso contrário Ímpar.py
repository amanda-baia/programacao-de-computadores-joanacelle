#11. Leia um número e: Se for par e positivo → “Par positivo”; Se for par e negativo → “Par negativo”; Caso contrário → “Ímpar”.

n1 = int (input ("Insira um valor:"))

if ((n1 % 2 == 0) and (n1 >= 0)):
    print ("Par positivo")
elif ((n1 % 2 == 0) and (n1 <= 0)):
    print ("Par negativo")
else:
    print ("Ímpar")

