class Mesa_computador:
    def __init__(self, id_mesa_computador, nome, especificacoes, valor, data_aquisicao, estado, vida_util, status):
        self.id_mesa_computador = 'MOMC' + id_mesa_computador
        self.tipo = 'Mesa para Computador'
        self.especificacoes = especificacoes
        self.data_aquisicao = data_aquisicao
        self.estado = estado
        self.vida_util = vida_util
        self.valor = valor
        self.status = status
        self.nome = nome

class Mesa_administracao:
    def __init__(self, id_mesa_administracao, nome, especificacoes, valor, data_aquisicao, estado, vida_util, status):
        self.id_mesa_administracao = 'MOMA' + id_mesa_administracao
        self.tipo = 'Mesa para Computador Administração'
        self.especificacoes = especificacoes
        self.data_aquisicao = data_aquisicao
        self.estado = estado
        self.vida_util = vida_util
        self.valor = valor
        self.status = status
        self.nome = nome

class Cadeira_computador:
    def __init__(self, id_cadeira_computador, nome, especificacoes, valor, data_aquisicao, estado, vida_util, status):
        self.id_cadeira_computador = 'MOCC' + id_cadeira_computador
        self.tipo = 'Cadeira para Computador'
        self.especificacoes = especificacoes
        self.data_aquisicao = data_aquisicao
        self.estado = estado
        self.vida_util = vida_util
        self.valor = valor
        self.status = status
        self.nome = nome

class Balcao_recepcao:
    def __init__(self, id_balcao_recepcao, nome, especificacoes, valor, data_aquisicao, estado, vida_util, status):
        self.id_balcao_recepcao = 'MOBR' + id_balcao_recepcao
        self.tipo = 'Balcao para Recepção'
        self.especificacoes = especificacoes
        self.data_aquisicao = data_aquisicao
        self.estado = estado
        self.vida_util = vida_util
        self.valor = valor
        self.status = status
        self.nome = nome

class Piso_vinilico:
    def __init__(self, id_piso_vinilico, nome, especificacoes, valor, data_aquisicao, estado, vida_util, status):
        self.id_piso_vinilico = 'MOPI' + id_piso_vinilico
        self.tipo = 'Piso Vinílico em Régua'
        self.especificacoes = especificacoes
        self.data_aquisicao = data_aquisicao
        self.estado = estado
        self.vida_util = vida_util
        self.valor = valor
        self.status = status
        self.nome = nome

class Decoracao:
    def __init__(self, id_decoracao, nome, especificacoes, valor, data_aquisicao, estado, vida_util, status):
        self.id_decoracao = 'MODE' + id_decoracao
        self.tipo = 'Decoração'
        self.especificacoes = especificacoes
        self.data_aquisicao = data_aquisicao
        self.estado = estado
        self.vida_util = vida_util
        self.valor = valor
        self.status = status
        self.nome = nome