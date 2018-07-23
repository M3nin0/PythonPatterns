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
Padrão de projeto aplicado: Template Method

Este é aplicado quando uma estrutura (Lógica) é parecida em diversas classes, e para evitar repetições de código
cria-se uma template com os métodos que substituem os valores na lógica, possibilitando assim que herança sejam feitas
e a lógica original seja reutilizada.
'''

# Template utilizada no padrão de projeto
class TemplateDeImpostoCondicional(object):

	__metaclass__ = ABCMeta
	# Ducktyping na template
	def calcula(self, orcamento):
		if self.deve_usar_maxima_taxacao(orcamento):
			return self.maxima_taxacao(orcamento)
		else:
			return self.minima_taxacao(orcamento)

	@abstractmethod
	def deve_usar_maxima_taxacao(self, orcamento):
		pass

	@abstractmethod
	def maxima_taxacao(self, orcamento):
		pass

	@abstractmethod
	def minima_taxacao(self, orcamento):
		pass

class ISS(object):

	# Duck typing
	def calcula(self, orcamento):
		return orcamento.valor * 0.1

class ICMS(object):

	# Duck typing
	def calcula(self, orcamento):
		return orcamento.valor * 0.06

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
