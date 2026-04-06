#13. Leia um número e: Se for maior que 100 → mostre metade; Senão → mostre o dobro.

n1 = (float (input("Insira um número")))
M = (n1/2)
D = (n1*2)

if (n1 > 100):
    print ("A metade do valor é", M)
else:
    print ("O dobro do valor é", D)

