# 1)  IMC é a sigla para Índice de Massa Corporal que serve para avaliar o peso do indivíduo em relação à sua altura e assim indicar se está dentro do peso ideal, acima ou abaixo do peso desejado. O cálculo do IMC deve ser feito usando a seguinte fórmula matemática: Peso ÷ altura x altura.


# IMC
# Classificação do IMC
# < 16
# Magreza grave
# 16 a < 17
# Magreza moderada
# 17 a < 18,5 
# Magreza leve
# 18,5 a < 25
# Saudável
# 25 a < 30  
# Sobrepeso
# 30 a < 35 
# Obesidade Grau I
# 35 a < 40  
# Obesidade Grau II (severa)
# > 40 
# Obesidade Grau III (mórbida)


def imc_calc(weight, height):
  return weight / (height * height)

def imc_classificate(imc):
  if imc < 16:
    print('Magreza grave')
  elif imc >= 16 and imc < 17:
    print('Magreza moderada')
  elif imc >= 17 and imc < 18.5:
    print('Magreza leve')
  elif imc >= 18.5 and imc < 25:
    print('Saudável')
  elif imc >= 25 and imc < 30:
    print('Sobrepeso')
  elif imc >= 30 and imc < 35:
    print('Obesidade grau I')
  elif imc >= 35 and imc < 40:
    print('Obesidade grau II (severa)')
  else:
    print('Obesidade grau III (mórbida)')

print('Calculo de imc!\n')

weight = float(input('Informe o seu peso (Ex: 98.5 Kg): '))
height = float(input('Informe a sua altura (Ex: 1.70 m): '))

imc = imc_calc(weight, height)
print(imc)
imc_classificate(imc)