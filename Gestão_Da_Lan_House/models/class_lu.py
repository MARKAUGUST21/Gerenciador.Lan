class Painel_led:
    def __init__(self, id_painel_led, nome, especificacoes, valor, data_aquisicao, estado, vida_util, status):
        self.id_painel_led = 'LUP' + id_painel_led
        self.tipo = 'Painel de LED'
        self.especificacoes = especificacoes
        self.data_aquisicao = data_aquisicao
        self.estado = estado
        self.vida_util = vida_util
        self.valor = valor
        self.status = status
        self.nome = nome