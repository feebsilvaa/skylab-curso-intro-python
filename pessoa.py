# -*- coding: utf-8 -*-

class Pessoa():

	def __init__(self, nome, idade):
		self.nome = nome
		self.idade = idade

	def get_nome(self):
		return self.nome

	def set_nome(self, nome):
		self.nome = nome

	def get_idade(self):
		return self.idade

	def set_idade(self, idade):
		self.idade = idade

	def falar(self, palavra):
		print(palavra)

	def falar_nome(self):
		print('Meu nome é ', self.nome)