from random import randint

def soma(n1, n2, n3=0):
	return n1 + n2

# print(soma(1, 2, 1))

def funcao_dinamica(*args, **kwargs):
	print(args)
	print(kwargs)

# funcao_dinamica(1, 2, 3, 4, 5, 6, 7, teste='teste', teste2='teste2')


def gerar_numero():
	x = randint(0, 9)
	y = randint(0, 1)
	
	try:
		print(x / y)
	except Exception as e:
		dir(e)
		print('Ocorreu um erro: ', e)