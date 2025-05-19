class Computador:
    def __init__(self, tipo_ativo, nome, id_computador, especificacoes, valor, data_aquisicao, estado, vida_util, status):
        self.tipo_ativo = tipo_ativo
        if self.tipo_ativo == 'Escritório':
            self.id_computador = 'COE' + id_computador
            self.tipo = 'Computador de Escritório'
        elif self.tipo_ativo == 'Gamer':
            self.id_computador = 'COG' + id_computador
            self.tipo = 'Computador Gamer'
        elif self.tipo_ativo == 'Servidor':
            self.id_computador = 'COS' + id_computador
            self.tipo = 'Computador de Servidor'
        self.especificacoes = especificacoes
        self.data_aquisicao = data_aquisicao
        self.estado = estado
        self.vida_util = vida_util
        self.valor = valor
        self.nome = nome
        self.status = status

class Monitor:
    def __init__(self, tipo_ativo, id_monitor, nome, especificacoes, valor, data_aquisicao, estado, vida_util, status):
        self.tipo_ativo = tipo_ativo
        if self.tipo_ativo == 'Escritório':
            self.id_monitor = 'COEM' + id_monitor
            self.tipo = 'Monitor de Escritório'
        elif self.tipo_ativo == 'Gamer':
            self.id_monitor = 'COGM' + id_monitor
            self.tipo = 'Monitor Gamer'
        elif self.tipo_ativo == 'Servidor':
            self.id_monitor = 'COSM' + id_monitor
            self.tipo = 'Monitor do Servidor'
        self.especificacoes = especificacoes
        self.data_aquisicao = data_aquisicao
        self.estado = estado
        self.vida_util = vida_util
        self.valor = valor
        self.nome = nome
        self.status = status

class Perifericos:
    def __init__(self, tipo_ativo, id_periferico, nome, especificacoes, valor, data_aquisicao, estado, vida_util, status):
        self.tipo_ativo = tipo_ativo
        if self.tipo_ativo == 'Escritório':
            self.id_periferico = 'COETM' + id_periferico
            self.tipo = 'Periferico de Escritório'
        elif self.tipo_ativo == 'Gamer':
            self.id_periferico = 'COGTM' + id_periferico
            self.tipo = 'Periferico Gamer'
        elif self.tipo_ativo == 'Servidor':
            self.id_periferico = 'COSTM' + id_periferico
            self.tipo = 'Periferico do Servidor'
        self.especificacoes = especificacoes
        self.data_aquisicao = data_aquisicao
        self.estado = estado
        self.vida_util = vida_util
        self.valor = valor
        self.nome = nome
        self.status = status