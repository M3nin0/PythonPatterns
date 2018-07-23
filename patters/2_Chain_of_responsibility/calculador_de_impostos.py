from impostos import calcula_ISS, calcula_ICMS, ISS, ICMS

'''
Padrão de projeto aplicado: Strategy (Estratégia)

Neste a estratégia de calculo de imposto é passado como parâmetro, assim fazendo com que a estratégia de calculo
mude sem alterar a classe.
'''

class CalculadorDeImpostos(object):

	def realiza_calculo(self, orcamento, imposto):

		imposto_calculado = imposto(orcamento)

		# Solução orientada a objetos
		# imposto_calculado = imposto.calcula(orcamento)

		print(imposto_calculado)

if __name__ == '__main__':

	from orcamento import Orcamento

	calculador = CalculadorDeImpostos()
	orcamento = Orcamento(500)

	calculador.realiza_calculo(orcamento, calcula_ISS)
	calculador.realiza_calculo(orcamento, calcula_ICMS)

	# Solução orientada a objetos
	calculador.realiza_calculo(orcamento, ISS())
	calculador.realiza_calculo(orcamento, ICMS())
