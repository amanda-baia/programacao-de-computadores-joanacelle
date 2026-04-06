#4. Leia um número e informe se ele é par ou ímpar.

n1 = float (input ("Insira um número:"))

M = n1 % 2

if (M <= 0):
    print ("Esse número é par")

else:
    print ("Esse número é Ímpar")