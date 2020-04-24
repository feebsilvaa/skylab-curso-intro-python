# 2)  Num cartório o nome das pessoas a serem cadastradas no sistema devem ser inseridos com todas as iniciais maiúsculas(nome, sobrenome, nome do meio com exceção do “de” ou “da”) ex.: José da Silva , porém nem todo funcionário tem esse cuidado na hora do cadastro.  Crie uma função que receba um nome completo e formate nessas condições.

def handle_name(name):
  names = name.split(' ')
  handled_name = ''

  for n in names:
    if n.startswith('d') and len(n) <= 3:
      handled_name += n + ' '
    else:
      handled_name += n.capitalize() + ' '

  return handled_name.strip()

print(handle_name('josé da silva'))
print(handle_name('joão marcos da silva'))
print(handle_name('miguel josiah barbosa silva'))
print(handle_name('edrieli maria das graças barbosa silva'))
print(handle_name('edrieli mª das graças barbosa silva'))