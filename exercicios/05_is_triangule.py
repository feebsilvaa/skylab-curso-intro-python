# 5)  Ler 3 valores (A, B e C) representando as medidas dos lados de um triângulo e escrever se formam ou não um triângulo. OBS: para formar um triângulo, o valor de cada lado deve ser menor que a soma dos outros 2 lados.


a_side = float(input('Set A side value: '))
b_side = float(input('Set B side value: '))
c_side = float(input('Set C side value: '))

if a_side < (b_side + c_side) and \
  b_side < (a_side + c_side) and \
  c_side < (a_side + b_side):
  print('Yeah, these values can build a triangule.')
else:
  print("Sorry, with these values, it's impossible to build a triangule.")