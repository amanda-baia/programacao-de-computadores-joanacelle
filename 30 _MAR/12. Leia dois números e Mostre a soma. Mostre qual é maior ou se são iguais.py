#12. Leia dois números e: Mostre a soma; Mostre qual é maior ou se são iguais.

n1 = int (input ("Insira o primeiro número: "))
n2 = int (input ("Insira o segundo número: "))

M = (n1 + n2)
print ("O valor da soma é:", M)

if (n1 > n2):
    print(" O primeiro número" , n1, "é maior que o segundo número",n2)
elif (n1 == n2):
    print ("Os dois números são iguais ")
else:
    print ("O segundo número", n2, "é maior que o primeiro número", n1)
