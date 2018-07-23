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
class ISS(object):

	# Duck typing
	def calcula(orcamento):
		return orcamento.valor * 0.1

class ICMS(object):

	# Duck typing
	def calcula(orcamento):
		return orcamento.valor * 0.06
