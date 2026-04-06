#17. Leia idade e: Mostre: Menor de idade (<18); Adulto (18 a 59); Idoso (60+).

n1 = int (input ("Insira uma idade"))
if n1 < 18:
    print ("Menor de idade")
elif n1 >= 18 and n1 < 59:
    print ("Adulto")
else:
    print ("Idoso")
