class Contato:
    def __init__(self, id_contato, nome, especificacoes, valor, data_aquisicao, estado, vida_util, status):
        self.id_contato = 'MACO' + id_contato
        self.tipo = 'Contato'
        self.especificacoes = especificacoes
        self.data_aquisicao = data_aquisicao
        self.estado = estado
        self.vida_util = vida_util
        self.valor = valor
        self.status = status
        self.nome = nome

class Divulgacao:
    def __init__(self, id_divulgacao, nome, especificacoes, valor, data_aquisicao, estado, vida_util, status): 
        self.id_divulgacao = 'MADI' + id_divulgacao
        self.tipo = 'Divulgação'
        self.especificacoes = especificacoes
        self.data_aquisicao = data_aquisicao
        self.estado = estado
        self.vida_util = vida_util
        self.valor = valor
        self.status = status
        self.nome = nome

class Identidade_digital:
    def __init__(self, id_identidade_digital, nome, especificacoes, valor, data_aquisicao, estado, vida_util, status):
        self.id_identidade_digital = 'MAID' + id_identidade_digital
        self.tipo = 'Identidade Digital'
        self.especificacoes = especificacoes
        self.data_aquisicao = data_aquisicao
        self.estado = estado
        self.vida_util = vida_util
        self.valor = valor
        self.status = status
        self.nome = nome