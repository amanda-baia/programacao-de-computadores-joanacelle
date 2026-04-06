#27. Leia dois números informados pelo usuário. Se ambos forem positivos, calcule e exiba a soma entre eles. Caso contrário, calcule e exiba o produto entre eles

a = float(input("Digite o primeiro valor: "))
b = float(input("Digite o segundo valor: "))
P = (a) * (b)
S = (a) + (b)
if (a > 0) and (b > 0):
    print("O valor da soma entre eles é", S)
else:
    print ("O valor do produto é ", P)

