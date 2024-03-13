# Escrever os numeros com espaço
numeros = str(input(" "))
numeros_conv = numeros.split()
conv = list(map(float, numeros_conv))
A, B, C = conv
pi = 3.14159
TRIANGULO = 1/2 * A * C
CIRCULO = pi * pow(C, 2)
TRAPEZIO = ((A + B) * C) / 2
QUADRADO = pow(A, 2)
RETANGULO = A * B
print("TRIANGULO: ", round(TRIANGULO, 3))
print("CIRCULO: ", round(CIRCULO, 3))
print("TRAPEZIO: ", round(TRAPEZIO, 3))
print("QUADRADO: ", round(QUADRADO, 3))
print("RETANGULO: ", round(RETANGULO, 3))
