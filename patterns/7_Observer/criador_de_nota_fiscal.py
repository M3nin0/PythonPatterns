from datetime import date
from nota_fiscal import NotaFiscal

'''
Padrão de projeto aplicado: Builder

O pattern builder é utilizado para facilitar a construção de objetos com construtores complexos.

Mas perceba que, o Python já traz recursos de linguagem que ajuda a resolver o problema de objetos complexos, 
estes recursos são o argumento padrão e o argumento nomeado.

Desta forma talvez este padrão em python não seja o melhor a ser aplicado.
'''

class CriadorDeNotaFiscal(object):

	def __init__(self):
		self.__razao_social = None
		self.__cnpj = None
		self.__data_de_emissao = None
		self.__itens = None
		self.__detalhes = None

	def com_razao_social(self, razao_social):
		self.__razao_social = razao_social

		return self

	def com_cnpj(self, cnpj):
		self.__cnpj = cnpj

		return self

	def com_data_de_emissao(self, data_de_emissao):
		self.__data_de_emissao = data_de_emissao

		return self

	def com_itens(self, itens):
		self.__itens = itens

		return self

	def com_detalhes(self, detalhes): 
		self.__detalhes = detalhes

		return self

	def constroi(self):
		if self.__razao_social is None:
			raise Exception('Razão social deve ser preenchida')
		if self.__cnpj is None:
			raise Exception('CNPJ deve ser preenchido')
		if self.__itens is None:
			raise Exception('Itens devem ser preenchidos')
		if self.__data_de_emissao is None:
			self.__data_de_emissao = date.today()
		if self.__detalhes is None:
			self.__detalhes = ''

		return NotaFiscal(razao_social = self.__razao_social, cnpj = self.__cnpj,
							data_de_emissao = self.__data_de_emissao, 
							itens = self.__itens, detalhes = self.__detalhes)
