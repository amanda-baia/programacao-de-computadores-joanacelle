#23. Leia três números inteiros informados pelo usuário. Exiba em ordem decrescente o resto da divisão por 3
from pickletools import read_bytes1

a = int (input ("Insira o primeiro número: "))
b = int (input ("Insira o segundo número:"))
c = int (input ("Insira o terceiro número:"))

ra = a % 3
rb = b % 3
rc = c % 3

if ra == rb == rc:
    print("Não existe ordem, pois, os valores do resto da divisão são iguais")
elif   ra >= rb and ra >= rc :
    if rb >= rc:
        print ("A ordem é ra,rb,rc")
    else:
        print ("A ordem é ra,rc,rb")
elif rb >= ra and rb >= rc:
    if ra >= rc:
        print ("A ordem é rb,ra,rc")
    else:
        print ("A ordem é rb,rc,ra")
else:
    if ra >= rb:
        print(rc,ra,rb)
    else:
        print(rc,rb,ra)



