#21. Leia um número inteiro informado pelo usuário.Verifique se o número é positivo. Caso seja, analise se ele é múltiplo de 2 e de 3 ao mesmo tempo. Se atender a ambas as condições, exiba:“Múltiplo de 2 e 3”. Caso contrário, exiba: “Não atende”. Se o número não for positivo, exiba: “Número inválido”.

n = int (input ("Insira um número:"))

if (n > 0) :
    if (n % 2 == 0) and (n % 3 == 0) :
        print ("Múltiplo de 2 e 3")
    else:
        print ("Não atende")
else:
    print ("Número inválido")

