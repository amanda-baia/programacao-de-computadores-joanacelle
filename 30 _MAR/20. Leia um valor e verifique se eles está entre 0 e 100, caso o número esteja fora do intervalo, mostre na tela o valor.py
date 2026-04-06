#20. Leia um valor e: verifique se eles está entre 0 e 100, caso o número esteja fora do intervalo,mostre na tela o valor

a = int (input ("Insira um valor:"))

if (a >= 0) and (a <= 100):
    print ("Dentro do intervalo")
else:
    print ("Fora do intervalo")