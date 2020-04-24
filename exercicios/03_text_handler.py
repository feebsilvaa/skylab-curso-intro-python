# 3)  Um designer está desenvolvendo uma página para o site do cliente e percebeu que determinadas informações de texto são muito longas para caber no espaço disponível da página que são apenas 15 caracteres, então ele decide exibir apenas parte do texto seguido por “...” para indicar que o texto continua, ou apresentar o texto completo caso tenha 15 caracteres no máximo. Vamos ajudar nosso amigo :) 
# obs.: use dir(“string”) e tente achar uma função que ajude a calcular o tamanho do texto.



def handle_big_text(text):
  if len(text) > 15:
    return text[0:12] + '...'
  else:
    return text

print(handle_big_text('abcdefghijklmno'))
print(handle_big_text('abcdefghijklmnop'))
print(handle_big_text('Enim exercitation anim dolor laboris cillum do est laborum sint proident. Adipisicing ex consectetur anim excepteur consectetur cillum minim. Cupidatat eiusmod irure exercitation irure mollit magna ea aliquip. Incididunt nisi esse elit qui qui in labore sit ut aute magna. Quis laborum incididunt ullamco pariatur minim minim tempor sit proident incididunt fugiat culpa.'))