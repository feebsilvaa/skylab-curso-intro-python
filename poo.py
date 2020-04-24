# -*- coding: utf-8 -*-

from pessoa import Pessoa
from pessoa_fisica import PessoaFisica

p = Pessoa('Fernando', 26)
p.falar_nome()

p.set_nome('Miguel')
print(p.get_nome())

p.falar('Olá mundo')


pf = PessoaFisica('Miguel', 4, 122333412312)
print(pf.get_nome())
print(pf.get_idade())
print(pf.get_cpf())