class Ar_condicionado:
    def __init__(self, id, nome, especificacoes, valor, data_aquisicao, estado, vida_util, status):
        self.id = 'CLAC' + id
        self.tipo = 'Ar-Condicionado'
        self.especificacoes = especificacoes
        self.data_aquisicao = data_aquisicao
        self.estado = estado
        self.vida_util = vida_util
        self.valor = valor
        self.nome = nome
        self.status = status