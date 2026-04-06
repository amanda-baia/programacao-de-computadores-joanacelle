#10. Leia um número e informe: “Dentro do intervalo” se estiver entre 0 e 10; “Fora do intervalo” caso contrário.

n1 = int (input ("Insira um valor: "))

if ((0 <= n1) and (n1 <= 10)):
    print("Dentro do intervalo")
else:
    print("Fora do intervalo")

