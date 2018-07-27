def calcula_ISS(orcamento):

	return orcamento.valor * 0.1

def calcula_ICMS(orcamento):

	return orcamento.valor * 0.06

# Solução utilizando classes
'''
'Sobre o duck typing: Se voa igual um pato, se faz quck, deixa passar que está valendo'

Esta é uma maneira de reutilizar objetos de classes que tenham o mesmo método, assim, 
mesmo não sendo do mesmo tipo, pode-se passar como parâmetro objetos diferentes, desde que estes tenham 
os mesmos métodos
'''

from abc import ABCMeta, abstractmethod

'''
Padrão de projeto aplicado (Imposto): Decorator

Neste pattern, um objeto recebe outro objeto para fazer parte de seu comportamento, veja que, em outras
linguagens, este é um processo um pouco mais rígido, já que nele é necessário que o objeto recebido como parâmetro
seja do mesmo tipo do objeto que recebe.

Veja que em python há também o decorator, que também é descrito abaixo, neste o resultado é parecido com o 
resultado obtido quando trabalhamos com as classes.

A diferença entre o padrão feito manualmente e o recurso do Python, é que o feito manualmente, pode ser executado
ou não, mudando de acordo com os dados, e o decorator do Python, sempre será executado.

'Decorando, o objeto original!'
'''
class Imposto(object):
	def __init__(self, outro_imposto = None):
		self.__outro_imposto = outro_imposto

	# Calculo do outro imposto criado
	def calculo_do_outro_imposto(self, orcamento):
		if self.__outro_imposto != None:
			return self.__outro_imposto.calcula(orcamento)
		return 0

	@abstractmethod
	# Duck typing
	def calcula(self, orcamento):
		pass

'''
Padrão de projeto aplicado: Template Method

Este é aplicado quando uma estrutura (Lógica) é parecida em diversas classes, e para evitar repetições de código
cria-se uma template com os métodos que substituem os valores na lógica, possibilitando assim que herança sejam feitas
e a lógica original seja reutilizada.
'''

# Template utilizada no padrão de projeto
class TemplateDeImpostoCondicional(metaclass = ABCMeta, Imposto):

	# Ducktyping na template
	def calcula(self, orcamento):
		if self.deve_usar_maxima_taxacao(orcamento):
			return self.maxima_taxacao(orcamento) + self.calculo_do_outro_imposto(orcamento)
		else:
			return self.minima_taxacao(orcamento) + self.calculo_do_outro_imposto(orcamento)

	@abstractmethod
	def deve_usar_maxima_taxacao(self, orcamento):
		pass

	@abstractmethod
	def maxima_taxacao(self, orcamento):
		pass

	@abstractmethod
	def minima_taxacao(self, orcamento):
		pass

# Função utilizada para demonstrar o Decorator nativo da linguagem Python.
def IPVX(metodo_ou_funcao):
	"""Chama o cálculo do imposto ISS, pega o resultado e soma com R$ 50.00
	"""

	def wrapper(self, orcamento):
		"""
		:param: self: Auto referência da classe onde está o método a ser chamado
		:param: orcamento: orcamento recebido no método calcula
		"""
		return metodo_ou_funcao(self, orcamento) + 50
	return wrapper

class ISS(Imposto):

	# Duck typing
	@IPVX # Decorador do python
	def calcula(self, orcamento):
		return (orcamento.valor * 0.1) + self.calculo_do_outro_imposto(orcamento)

class ICMS(Imposto):

	# Duck typing
	@IPVX
	def calcula(self, orcamento):
		return (orcamento.valor * 0.06) + self.calculo_do_outro_imposto(orcamento)

# Novos impostos (Imaginários) (Apenas para as aulas)
class ICPP(TemplateDeImpostoCondicional):

	def deve_usar_maxima_taxacao(self, orcamento):
		return orcamento.valor > 500
			
	def maxima_taxacao(self, orcamento):
		return orcamento.valor * 0.07

	def minima_taxacao(self, orcamento):
		return orcamento.valor * 0.05

class IKCV(TemplateDeImpostoCondicional):

	def __tem_item_maior_que_100_reais(self, orcamento):
		for item in orcamento.obter_itens():
			if item.valor > 100:
				return True
		return False

	def deve_usar_maxima_taxacao(self, orcamento):
		return orcamento.valor > 500 and self.__tem_item_maior_que_100_reais(orcamento)
			
	def maxima_taxacao(self, orcamento):
		return orcamento.valor * 0.1

	def minima_taxacao(self, orcamento):
		return orcamento.valor * 0.06;
