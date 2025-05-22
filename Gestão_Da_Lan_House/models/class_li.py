class Licenca_jogo:
    def __init__(self, id, nome, especificacoes, valor, data_aquisicao, estado, vida_util, status):
        self.id = 'LIJO' + id
        self.tipo = 'Licenças de Jogos (Anual)'
        self.especificacoes = especificacoes
        self.data_aquisicao = data_aquisicao
        self.estado = estado
        self.vida_util = vida_util
        self.valor = valor
        self.nome = nome
        self.status = status

class Jogo_adicional:
    def __init__(self, id, nome, especificacoes, valor, data_aquisicao, estado, vida_util, status):
        self.id = 'LIJA' + id
        self.tipo = 'Jogos Adicionais'
        self.especificacoes = especificacoes
        self.data_aquisicao = data_aquisicao
        self.estado = estado
        self.vida_util = vida_util
        self.valor = valor
        self.nome = nome
        self.status = status

class Sistema_operacional:
    def __init__(self, id, nome, especificacoes, valor, data_aquisicao, estado, vida_util, status):
        self.id = 'LISO' + id
        self.tipo = 'Sistema Operacional'
        self.especificacoes = especificacoes
        self.data_aquisicao = data_aquisicao
        self.estado = estado
        self.vida_util = vida_util
        self.valor = valor
        self.nome = nome
        self.status = status

class Antivirus:
    def __init__(self, id, nome, especificacoes, valor, data_aquisicao, estado, vida_util, status):
        self.id = 'LIAN' + id
        self.tipo = 'Antivírus'
        self.especificacoes = especificacoes
        self.data_aquisicao = data_aquisicao
        self.estado = estado
        self.vida_util = vida_util
        self.valor = valor
        self.status = status
        self.nome = nome

class Programa_edicao:
    def __init__(self, id, nome, especificacoes, valor, data_aquisicao, estado, vida_util, status):
        self.id = 'LIED' + id
        self.tipo = 'Programa de Edição'
        self.especificacoes = especificacoes
        self.data_aquisicao = data_aquisicao
        self.estado = estado
        self.vida_util = vida_util
        self.valor = valor
        self.status = status
        self.nome = nome