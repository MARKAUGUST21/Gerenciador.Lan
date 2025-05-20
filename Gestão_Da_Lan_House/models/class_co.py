class Computador:
    def __init__(self, tipo_ativo, id, nome, especificacoes, valor, data_aquisicao, estado, vida_util, status):
        self.tipo_ativo = tipo_ativo
        if self.tipo_ativo == 'Escritório':
            self.id = 'COE' + id
            self.tipo = 'Computador de Escritório'
        elif self.tipo_ativo == 'Gamer':
            self.id = 'COG' + id
            self.tipo = 'Computador Gamer'
        elif self.tipo_ativo == 'Servidor':
            self.id = 'COS' + id
            self.tipo = 'Computador de Servidor'
        self.especificacoes = especificacoes
        self.data_aquisicao = data_aquisicao
        self.estado = estado
        self.vida_util = vida_util
        self.valor = valor
        self.nome = nome
        self.status = status

class Monitor:
    def __init__(self, tipo_ativo, id, nome, especificacoes, valor, data_aquisicao, estado, vida_util, status):
        self.tipo_ativo = tipo_ativo
        if self.tipo_ativo == 'Escritório':
            self.id = 'COEM' + id
            self.tipo = 'Monitor de Escritório'
        elif self.tipo_ativo == 'Gamer':
            self.id = 'COGM' + id
            self.tipo = 'Monitor Gamer'
        elif self.tipo_ativo == 'Servidor':
            self.id = 'COSM' + id
            self.tipo = 'Monitor do Servidor'
        self.especificacoes = especificacoes
        self.data_aquisicao = data_aquisicao
        self.estado = estado
        self.vida_util = vida_util
        self.valor = valor
        self.nome = nome
        self.status = status

class Perifericos:
    def __init__(self, tipo_ativo, id, nome, especificacoes, valor, data_aquisicao, estado, vida_util, status):
        self.tipo_ativo = tipo_ativo
        if self.tipo_ativo == 'Escritório':
            self.id = 'COETM' + id
            self.tipo = 'Periferico de Escritório'
        elif self.tipo_ativo == 'Gamer':
            self.id = 'COGTM' + id
            self.tipo = 'Periferico Gamer'
        elif self.tipo_ativo == 'Servidor':
            self.id = 'COSTM' + id
            self.tipo = 'Periferico do Servidor'
        self.especificacoes = especificacoes
        self.data_aquisicao = data_aquisicao
        self.estado = estado
        self.vida_util = vida_util
        self.valor = valor
        self.nome = nome
        self.status = status