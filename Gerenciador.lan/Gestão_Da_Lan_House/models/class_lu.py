class Painel_led:
    def __init__(self, id_painel_led, especificacoes, valor, data_aquisicao, estado, vida_util):
        
        self.id_painel_led = 'LUP' + id_painel_led
        self.nome = 'Painel de LED'
        self.especificacoes = especificacoes
        self.data_aquisicao = data_aquisicao
        self.estado = estado
        self.vida_util = vida_util
        self.valor = valor

        def mudar_estado(self, novo_estado):
            self.estado = novo_estado