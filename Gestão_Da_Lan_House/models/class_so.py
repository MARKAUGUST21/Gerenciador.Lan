class Software_gerenciamento:
    def __init__(self, id, nome, especificacoes, valor, data_aquisicao, estado, vida_util, status):
        self.id = 'SOGE' + id
        self.tipo = 'Software de Gerenciamento'
        self.especificacoes = especificacoes
        self.data_aquisicao = data_aquisicao
        self.estado = estado
        self.vida_util = vida_util
        self.valor = valor
        self.status = status
        self.nome = nome

class Banco_de_dados:
    def __init__(self, id, nome, especificacoes, valor, data_aquisicao, estado, vida_util, status):
        self.id = 'SOBD' + id
        self.tipo = 'Banco de Dados'
        self.especificacoes = especificacoes
        self.data_aquisicao = data_aquisicao
        self.estado = estado
        self.vida_util = vida_util
        self.valor = valor
        self.status = status
        self.nome = nome

class Website:
    def __init__(self, id, nome, especificacoes, valor, data_aquisicao, estado, vida_util, status):
        self.id = 'WEBS' + id
        self.tipo = 'Website próprio'
        self.especificacoes = especificacoes
        self.data_aquisicao = data_aquisicao
        self.estado = estado
        self.vida_util = vida_util
        self.valor = valor
        self.status = status
        self.nome = nome