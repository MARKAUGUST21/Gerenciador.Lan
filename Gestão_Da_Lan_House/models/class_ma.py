class Contato:
    def __init__(self, id, nome, especificacoes, valor, data_aquisicao, estado, vida_util, status):
        self.id = 'MACO' + id
        self.tipo = 'Contato'
        self.especificacoes = especificacoes
        self.data_aquisicao = data_aquisicao
        self.estado = estado
        self.vida_util = vida_util
        self.valor = valor
        self.status = status
        self.nome = nome

class Divulgacao:
    def __init__(self, id, nome, especificacoes, valor, data_aquisicao, estado, vida_util, status): 
        self.id = 'MADI' + id
        self.tipo = 'Divulgação'
        self.especificacoes = especificacoes
        self.data_aquisicao = data_aquisicao
        self.estado = estado
        self.vida_util = vida_util
        self.valor = valor
        self.status = status
        self.nome = nome

class Identidade_digital:
    def __init__(self, id, nome, especificacoes, valor, data_aquisicao, estado, vida_util, status):
        self.id = 'MAID' + id
        self.tipo = 'Identidade Digital'
        self.especificacoes = especificacoes
        self.data_aquisicao = data_aquisicao
        self.estado = estado
        self.vida_util = vida_util
        self.valor = valor
        self.status = status
        self.nome = nome