# -*- coding: utf-8 -*-

arquivo = open('arquivo.txt')

linhas = arquivo.readlines()
conteudo = arquivo.read()

print(conteudo) 

# for l in linhas:
#   print(l)


f2 = open('arquivo2.txt', 'w')
f2.write('Esse é o meu arquivo')
f2.close()