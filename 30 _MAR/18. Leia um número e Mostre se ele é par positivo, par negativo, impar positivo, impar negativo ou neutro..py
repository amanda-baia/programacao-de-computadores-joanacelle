#18. Leia um número e: Mostre se ele é par positivo, par negativo, impar positivo, impar negativo ou neutro.

n1 = int (input ("Insira um número:"))

if ((n1 % 2 == 0) and (n1 > 0)):
    print ("Par positivo")
elif ((n1 % 2 == 0) and (n1 < 0)):
    print ("Par negativo")
elif ((n1 % 2 != 0) and (n1 < 0)):
    print ("Ímpar negativo")
elif (n1 == 0):
    print ("É neutro")
else:
    print ("Ímpar positivo")