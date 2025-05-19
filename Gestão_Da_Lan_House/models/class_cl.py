class Ar_condicionado:
    def __init__(self, id_ar_condicionado, nome, especificacoes, valor, data_aquisicao, estado, vida_util, status):
        self.id_ar_condicionado = 'CLAC' + id_ar_condicionado
        self.tipo = 'Ar-Condicionado'
        self.especificacoes = especificacoes
        self.data_aquisicao = data_aquisicao
        self.estado = estado
        self.vida_util = vida_util
        self.valor = valor
        self.nome = nome
        self.status = status