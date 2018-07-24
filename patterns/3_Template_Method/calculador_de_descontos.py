# -*- coding: UTF-8 -*-

'''
Padrão de projeto aplicado: Chain of responsibility

Neste padrão há uma cadeia de resposabilidade que é passada para o código, assim, sempre que uma função 
não resolver o problema, ela chama uma proxima função que pode resolver o problema (Este é definido pelo programador)
'''

from descontos import DescontoPorCincoItens, DescontoPorMaisDeQuinhentosReais, SemDesconto

class CalculadorDeDescontos(object):
	def calcula(self, orcamento):
		
		desconto = DescontoPorCincoItens(
				DescontoPorMaisDeQuinhentosReais(
					SemDesconto())
		).calcula(orcamento)

		return desconto
		
if __name__ == '__main__':

	from orcamento import Orcamento, Item

	orcamento = Orcamento()

	orcamento.adiciona_item(Item('Item - 1', 100))
	orcamento.adiciona_item(Item('Item - 2', 50))
	orcamento.adiciona_item(Item('Item - 3', 400))

	print(orcamento.valor)
 	
	calculador = CalculadorDeDescontos()

	desconto_calculado = calculador.calcula(orcamento)
	print(desconto_calculado)
