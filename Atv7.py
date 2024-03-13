nome = str(input(" "))
salario = float(input(" "))
montante = float(input(" "))
comissao = (montante * 15) / 100
total = salario + comissao
print("TOTAL =  R$", round(total, 2))
