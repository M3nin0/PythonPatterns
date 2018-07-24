from impostos import calcula_ISS, calcula_ICMS, ISS, ICMS, ICPP, IKCV

'''
Padrão de projeto aplicado: Strategy (Estratégia)

Neste a estratégia de calculo de imposto é passado como parâmetro, assim fazendo com que a estratégia de calculo
mude sem alterar a classe.
'''

class CalculadorDeImpostos(object):

	def realiza_calculo(self, orcamento, imposto):

		# imposto_calculado = imposto(orcamento)

		# Solução orientada a objetos
		imposto_calculado = imposto.calcula(orcamento)

		print(imposto_calculado)

if __name__ == '__main__':

	from orcamento import Orcamento, Item

	calculador = CalculadorDeImpostos()
	orcamento = Orcamento()

	# Adicionando item
	orcamento.adiciona_item(Item('Item - 1', 100))
	orcamento.adiciona_item(Item('Item - 2', 50))
	orcamento.adiciona_item(Item('Item - 3', 400))

	# calculador.realiza_calculo(orcamento, calcula_ISS)
	# calculador.realiza_calculo(orcamento, calcula_ICMS)

	# Solução orientada a objetos
	print('ISS ; ICMS')
	calculador.realiza_calculo(orcamento, ISS())
	calculador.realiza_calculo(orcamento, ICMS())

	print('ISS com ICMS')
	calculador.realiza_calculo(orcamento, ISS(ICMS()))

	print('ICPP ; IKCV')
	calculador.realiza_calculo(orcamento, ICPP())
	calculador.realiza_calculo(orcamento, IKCV())

	print('ICPP com IKCV')
	calculador.realiza_calculo(orcamento, IKCV(ICPP()))
