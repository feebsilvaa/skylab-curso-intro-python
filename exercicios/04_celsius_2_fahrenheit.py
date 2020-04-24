# 4)  Escreva um algoritmo para ler uma temperatura em graus Fahrenheit, calcular e escrever o valor correspondente em graus Celsius (baseado na fórmula abaixo):

#   C    =  F - 32
#    5             9

def celsius_to_fahrenheit(celsius):
  return (celsius * 9 / 5) + 32

def fahrenheit_to_celsius(Fahrenheit):
  return (Fahrenheit - 32) * 5 / 9


print(celsius_to_fahrenheit(10))

f = fahrenheit_to_celsius(10)
print("%.2f" % f)