class Computador:
    def __init__(self, tipo, id_computador, especificacoes, valor, data_aquisicao, estado, vida_util):
        self.tipo = tipo
        if self.tipo == 'E':
            self.id_computador = 'COE' + id_computador
            self.nome = 'Computador de Escritório'
        elif self.tipo == 'G':
            self.id_computador = 'COG' + id_computador
            self.nome = 'Computador Gamer'
        elif self.tipo == 'S':
            self.id_computador = 'COS' + id_computador
            self.nome = 'Computador de Servidor'
        self.especificacoes = especificacoes
        self.data_aquisicao = data_aquisicao
        self.estado = estado
        self.vida_util = vida_util
        self.valor = valor

        def mudar_estado(self, novo_estado):
            self.estado = novo_estado

class Monitor:
    def __init__(self, tipo, id_monitor, especificacoes, valor, data_aquisicao, estado, vida_util):
        self.tipo = tipo
        if self.tipo == 'E':
            self.id_monitor = 'COEM' + id_monitor
            self.nome = 'Monitor de Escritório'
        elif self.tipo == 'G':
            self.id_monitor = 'COGM' + id_monitor
            self.nome = 'Monitor Gamer'
        elif self.tipo == 'S':
            self.id_monitor = 'COSM' + id_monitor
            self.nome = 'Monitor do Servidor'
        self.especificacoes = especificacoes
        self.data_aquisicao = data_aquisicao
        self.estado = estado
        self.vida_util = vida_util
        self.valor = valor

        def mudar_estado(self, novo_estado):
            self.estado = novo_estado

class Perifericos:
    def __init__(self, tipo, id_periferico, especificacoes, valor, data_aquisicao, estado, vida_util):
        self.tipo = tipo
        if self.tipo == 'E':
            self.id_periferico = 'COETM' + id_periferico
            self.nome = 'Periferico de Escritório'
        elif self.tipo == 'G':
            self.id_periferico = 'COGTM' + id_periferico
            self.nome = 'Periferico Gamer'
        elif self.tipo == 'S':
            self.id_periferico = 'COSTM' + id_periferico
            self.nome = 'Periferico do Servidor'
        self.especificacoes = especificacoes
        self.data_aquisicao = data_aquisicao
        self.estado = estado
        self.vida_util = vida_util
        self.valor = valor

        def mudar_estado(self, novo_estado):
            self.estado = novo_estado
