class Painel_led:
    def __init__(self, id, nome, especificacoes, valor, data_aquisicao, estado, vida_util, status):
        self.id = 'LUP' + id
        self.tipo = 'Painel de LED'
        self.especificacoes = especificacoes
        self.data_aquisicao = data_aquisicao
        self.estado = estado
        self.vida_util = vida_util
        self.valor = valor
        self.status = status
        self.nome = nome