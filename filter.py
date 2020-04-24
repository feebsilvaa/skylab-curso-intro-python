

def pares(i):
	if i%2==0:
		return i 

lista = [1, 2, 3, 4, 5]


lista_pares = filter(pares, lista)
lista_impares = filter(lambda x: x%2==1, lista)


print(lista_pares)
print(lista_impares)

