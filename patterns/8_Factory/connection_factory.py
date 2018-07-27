import MySQLdb

'''
Padrão de projeto aplicado: Factory

Neste tem-se uma classe/função especializada na construção de um determinado objeto.

Veja a diferença entre o Factory e o Builder:

	Builder = Auxilia a criação do objeto, mas este pode ser alterado pelo desenvolvedor
	Factory = Entrega um objeto criado, sem poder realizar nenhuma mudança.
'''

class ConnectionFactory(object):
	def get_connection(self):
		return MySQLdb.connect(
			host = "localhost",
			user = "root",
			passwd = "",
			db = "Bancao"
		)
