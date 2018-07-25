# -*- coding: UTF-8 -*-
from datetime import date

class Item(object):

    def __init__(self, descricao, valor):
        self.__descricao = descricao
        self.__valor = valor

    @property
    def descricao(self):
        return self.__descricao

    @property
    def valor(self):
        return self.__valor

class NotaFiscal(object):

    '''
    Os parâmetros nomeados e parâmetros com valores padrão já são uma forma de tratrar o builder,
    sem isto um recurso de linguagem.
    '''
    def __init__(self, razao_social, cnpj, itens, data_de_emissao=date.today(), detalhes=''):
        self.__razao_social = razao_social
        self.__cnpj = cnpj
        self.__data_de_emissao = data_de_emissao
        if len(detalhes) > 20:
            raise Exception('Detalhes da nota não pode ter mais do que 20 caracteres')
        self.__detalhes = detalhes
        self.__itens = itens

    @property
    def razao_social(self):
        return self.__razao_social

    @property
    def cnpj(self):
        return self.__cnpj

    @property
    def data_de_emissao(self):
        return self.__data_de_emissao

    @property
    def detalhes(self):
        return self.__detalhes

if __name__ == '__main__':

    from criador_de_nota_fiscal import CriadorDeNotaFiscal

    itens=[
        Item(
            'ITEM A',
            100
        ),
        Item(
            'ITEM B',
            200
        )
    ]

    nota_fiscal = NotaFiscal(
        cnpj='012345678901234',
        razao_social='FHSA Limitada',
        itens=itens
    )

    nota_fiscal_builder = (CriadorDeNotaFiscal()
                                .com_razao_social('FHSA LTDA')
                                .com_cnpj('123456789')
                                .com_itens(itens)
                                .constroi())
