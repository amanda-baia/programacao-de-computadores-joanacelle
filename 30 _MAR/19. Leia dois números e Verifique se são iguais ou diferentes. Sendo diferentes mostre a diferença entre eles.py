#19. Leia dois números e: Verifique se são iguais ou diferentes. Sendo diferentes mostre a diferença entre eles

a = int(input("Insira o primeiro número"))
b = int(input("Insira o segundo número"))
S = (a - b)

if (a != b):
    print ("Os números são diferentes e a subtração entre eles é:",S )
else:
    print ("Os números são iguais")

