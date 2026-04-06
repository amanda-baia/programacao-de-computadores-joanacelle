#21. Leia um número inteiro informado pelo usuário.Verifique se o número é positivo. Caso seja, analise se ele é múltiplo de 2 e de 3 ao mesmo tempo. Se atender a ambas as condições, exiba:“Múltiplo de 2 e 3”. Caso contrário, exiba: “Não atende”. Se o número não for positivo, exiba: “Número inválido”.

n1 = (input ("Insira um número inteiro"))

if n1.isdigit():
    n = int (n1)
    if n> 10:
        print ("Alto")
    else:
        print ("Baixo")
else:
    print ("Entrada inválida")

