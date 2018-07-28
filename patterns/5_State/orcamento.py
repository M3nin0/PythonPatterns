# -*- coding: UTF-8 -*-

'''
Padrão de projeto aplicado (Com a utilização da classe EstadoDeOrcamento): State

Neste a ideia é separar os estados de uma classe em classes, cada uma representado um respectivo estado. Assim
é possível criar classes especializadas, cada uma com uma função diferente, além de permitir que, seja possível
limitar e saber quais serão as proximas classes (Estados)
'''

from abc import ABCMeta, abstractmethod

class EstadoDeOrcamento(metaclass=ABCMeta, object):

	@abstractmethod
	def aplica_desconto_extra(self, orcamento):
		pass

	@abstractmethod
	def aprova(self, orcamento):
		pass

	@abstractmethod
	def reprova(self, orcamento):
		pass

	@abstractmethod
	def finaliza(self, orcamento):
		pass

class EmAprovacao(EstadoDeOrcamento):
	def aplica_desconto_extra(self, orcamento):
		orcamento.adiciona_desconto_extra(orcamento.valor * 0.02)

	def aprova(self, orcamento):
		orcamento.estado_atual = Aprovado()

	def reprova(self, orcamento):
		orcamento.estado_atual = Reprovado()

	def finaliza(self, orcamento):
		raise Exception('Orçamento em aprovação não pode ir para finalizado')

class Aprovado(EstadoDeOrcamento):
	def aplica_desconto_extra(self, orcamento):
		orcamento.adiciona_desconto_extra(orcamento.valor * 0.05)

	def aprova(self, orcamento):
		raise Exception('Orçamento já está aprovado')

	def reprova(self, orcamento):
		raise Exception('Orçamento aprovado não podem mais serem reprovados')

	def finaliza(self, orcamento):
		orcamento.estado_atual = Finalizado()

class Reprovado(EstadoDeOrcamento):
	def aplica_desconto_extra(self, orcamento):
		raise Exception('Orçamentos reprovados não recebem desconto extra')

	def aprova(self, orcamento):
		raise Exception('Orçamento reprovado não podem mais serem aprovados')

	def reprova(self, orcamento):
		raise Exception('Orçamento reprovados não podem mais serem reprovados')

	def finaliza(self, orcamento):
		orcamento.estado_atual = Finalizado()

class Finalizado(EstadoDeOrcamento):
	def aplica_desconto_extra(self, orcamento):
		raise Exception('Orçamentos finalizados não recebem desconto extra')

	def aprova(self, orcamento):
		raise Exception('Orçamentos finalizados não podem mais serem aprovados')

	def reprova(self, orcamento):
		raise Exception('Orçamentos finalizados não podem mais serem reprovados')

	def finaliza(self, orcamento):
		raise Exception('Orcamento reprovados não podem ser reprovados')

class Orcamento(object):

	def __init__(self):
		self.__itens = []
		self.estado_atual = EmAprovacao()
		self.__desconto_extra = 0

	def aprova(self):
		self.estado_atual.aprova(self)

	def reprova(self):
		self.estado_atual.reprova(self)

	def finaliza(self):
		self.estado_atual.finaliza(self)

	def aplica_desconto_extra(self):

		self.estado_atual.aplica_desconto_extra(self)

	def adiciona_desconto_extra(self, desconto):
		self.__desconto_extra += desconto

	@property
	def valor(self):
		total = 0.0
		for item in self.__itens:
			total += item.valor
		return total - self.__desconto_extra

	def obter_itens(self):
		return tuple(self.__itens)

	@property
	def total_itens(self): 
		return len(self.__itens)

	def adiciona_item(self, item):
		self.__itens.append(item)

class Item(object):
	def __init__(self, nome, valor):
		self.__nome = nome
		self.__valor = valor

	@property
	def valor(self):
		return self.__valor

	@property
	def nome(self):
		return self.__nome

# orcamento = Orcamento(500)
# orcamento.valor


if __name__ == '__main__':

	orcamento = Orcamento()

	orcamento.adiciona_item(Item('Item - 1', 100))
	orcamento.adiciona_item(Item('Item - 2', 50))
	orcamento.adiciona_item(Item('Item - 3', 400))

	print(orcamento.valor)
	orcamento.reprova()
	orcamento.finaliza()
	orcamento.aplica_desconto_extra()
	print(orcamento.valor)
