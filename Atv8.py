# Escrever os numeros com espaço
numeros = str(input(" "))
numeros2 = str(input(" "))
numeros_conv = numeros.split()
numeros_conv2 = numeros2.split()
conv = list(map(float, numeros_conv))
conv2 = list(map(float, numeros_conv2))
codigo, peca, valor = conv
codigo2, peca2, valor2 = conv2
soma = (peca * valor) + (peca2 * valor2)
print("VALOR A PAGAR = R$", round(soma, 2))