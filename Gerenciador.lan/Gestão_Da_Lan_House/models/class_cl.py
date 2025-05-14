class Ar_condicionado:
    def __init__(self, id_ar_condicionado, especificacoes, valor, data_aquisicao, estado, vida_util):
        
        self.id_ar_condicionado = 'CLAC' + id_ar_condicionado
        self.nome = 'Ar-Condicionado'
        self.especificacoes = especificacoes
        self.data_aquisicao = data_aquisicao
        self.estado = estado
        self.vida_util = vida_util
        self.valor = valor

        def mudar_estado(self, novo_estado):
            self.estado = novo_estado