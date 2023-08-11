import math

Co = float(input("Valor do cateto oposto: "))
Ca = float(input("Valor do cateto adjacente: "))

H = Co*Co + Ca*Ca

raiz = math.sqrt(H)
real = format(math.trunc(raiz))

print("Valor da Hipotenusa =", real)