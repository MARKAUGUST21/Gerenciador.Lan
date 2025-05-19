class Licenca_jogo:
    def __init__(self, id_licenca_jogo, nome, especificacoes, valor, data_aquisicao, estado, vida_util, status):
        self.id_licenca_jogo = 'LIJO' + id_licenca_jogo
        self.tipo = 'Licenças de Jogos (Anual)'
        self.especificacoes = especificacoes
        self.data_aquisicao = data_aquisicao
        self.estado = estado
        self.vida_util = vida_util
        self.valor = valor
        self.nome = nome
        self.status = status

class Jogo_adicional:
    def __init__(self, id_jogo_adicional, nome, especificacoes, valor, data_aquisicao, estado, vida_util, status):
        self.id_jogo_adicional = 'LIJA' + id_jogo_adicional
        self.tipo = 'Jogos Adicionais'
        self.especificacoes = especificacoes
        self.data_aquisicao = data_aquisicao
        self.estado = estado
        self.vida_util = vida_util
        self.valor = valor
        self.nome = nome
        self.status = status

class Sistema_operacional:
    def __init__(self, id_sistema_operacional, nome, especificacoes, valor, data_aquisicao, estado, vida_util, status):
        self.id_sistema_operacional = 'LISO' + id_sistema_operacional
        self.tipo = 'Sistema Operacional'
        self.especificacoes = especificacoes
        self.data_aquisicao = data_aquisicao
        self.estado = estado
        self.vida_util = vida_util
        self.valor = valor
        self.nome = nome
        self.status = status

class Antivirus:
    def __init__(self, id_antivirus, nome, especificacoes, valor, data_aquisicao, estado, vida_util, status):
        self.id_antivirus = 'LIAN' + id_antivirus
        self.tipo = 'Antivírus'
        self.especificacoes = especificacoes
        self.data_aquisicao = data_aquisicao
        self.estado = estado
        self.vida_util = vida_util
        self.valor = valor
        self.status = status
        self.nome = nome

class Programa_edicao:
    def __init__(self, id_programa_edicao, nome, especificacoes, valor, data_aquisicao, estado, vida_util, status):
        self.id_programa_edicao = 'LIED' + id_programa_edicao
        self.tipo = 'Programa de Edição'
        self.especificacoes = especificacoes
        self.data_aquisicao = data_aquisicao
        self.estado = estado
        self.vida_util = vida_util
        self.valor = valor
        self.status = status
        self.nome = nome