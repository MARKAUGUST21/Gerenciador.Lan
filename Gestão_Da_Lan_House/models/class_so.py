class Software_gerenciamento:
    def __init__(self, id_software_gerenciamento, nome, especificacoes, valor, data_aquisicao, estado, vida_util, status):
        self.id_software_gerenciamento = 'SOGE' + id_software_gerenciamento
        self.tipo = 'Software de Gerenciamento'
        self.especificacoes = especificacoes
        self.data_aquisicao = data_aquisicao
        self.estado = estado
        self.vida_util = vida_util
        self.valor = valor
        self.status = status
        self.nome = nome

class Banco_de_dados:
    def __init__(self, id_banco_de_dados, nome, especificacoes, valor, data_aquisicao, estado, vida_util, status):
        self.id_banco_de_dados = 'SOBD' + id_banco_de_dados
        self.tipo = 'Banco de Dados'
        self.especificacoes = especificacoes
        self.data_aquisicao = data_aquisicao
        self.estado = estado
        self.vida_util = vida_util
        self.valor = valor
        self.status = status
        self.nome = nome

class Website:
    def __init__(self, id_website, nome, especificacoes, valor, data_aquisicao, estado, vida_util, status):
        self.id_website = 'WEBS' + id_website
        self.tipo = 'Website próprio'
        self.especificacoes = especificacoes
        self.data_aquisicao = data_aquisicao
        self.estado = estado
        self.vida_util = vida_util
        self.valor = valor
        self.status = status
        self.nome = nome