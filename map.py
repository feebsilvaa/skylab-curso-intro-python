


def dobro(x):
	return x*2

valores = [1, 2, 3, 4, 5]

valores_dobrados = map(dobro, valores)

print(valores)
print(valores_dobrados)

valores_triplicados = map(lambda x: x*3, valores)

print(valores_triplicados)