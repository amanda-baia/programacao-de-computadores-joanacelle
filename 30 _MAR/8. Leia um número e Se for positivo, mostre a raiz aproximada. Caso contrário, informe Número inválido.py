#8. Leia um número e: Se for positivo, mostre a raiz aproximada (use **0.5); Caso contrário,informe “Número inválido”

n1 = int (input ("Insira um valor"))
R = (n1 ** 0.5)


if (n1 > 0):
    print (("O valor da raiz quadrada é"), R)
elif (n1 == 0):
    print ("Número inválido")
else:
    print ("Número inválido")