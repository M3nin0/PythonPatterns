'''
Padrão de projeto Observer: Este é utilizado quando dado uma determinada ação realizada, outras ações devem
ser realizadas, desta forma, tem-se que será necessário a interação entre estas ações.

Neste caso para desacoplar o código foi realizado uma iteração em uma lista de observadores 
(Interessados na ação que está sendo realizada), e esta lista foi passada no construtor, fazendo com que,
a classe não fique dependente de saber são os observadores, apenas utilizando eles.
'''

def imprime(nota_fiscal):
    print('Imprimindo nova fiscal %s' % (nota_fiscal.cnpj))

def envia_por_email(nota_fiscal):
    print('Enviando por e-mail %s' % (nota_fiscal.cnpj))

def salva_no_banco(nota_fiscal): 
    print('Salvando no banco de dados %s' % (nota_fiscal.cnpj))

