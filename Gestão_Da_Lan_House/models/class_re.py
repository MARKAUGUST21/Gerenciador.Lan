class Roteador:
    def __init__(self, id_roteador, nome, especificacoes, valor, data_aquisicao, estado, vida_util, status):
        self.id_roteador = 'RER' + id_roteador
        self.tipo = 'Roteador de Dual Band'
        self.especificacoes = especificacoes
        self.data_aquisicao = data_aquisicao
        self.estado = estado
        self.vida_util = vida_util
        self.valor = valor
        self.status = status
        self.nome = nome

class Cabo_de_rede:
    def __init__(self, id_cabo_de_rede, nome, especificacoes, valor, data_aquisicao, estado, vida_util, status):
        self.id_cabo_de_rede = 'REC' + id_cabo_de_rede
        self.tipo = 'Cabo de Rede'
        self.especificacoes = especificacoes
        self.data_aquisicao = data_aquisicao
        self.estado = estado
        self.vida_util = vida_util
        self.valor = valor
        self.status = status
        self.nome = nome

class Nobreak:
    def __init__(self, id_nobreak, nome, especificacoes, valor, data_aquisicao, estado, vida_util, status):
        self.id_nobreak = 'REN' + id_nobreak
        self.tipo = 'Nobreak'
        self.especificacoes = especificacoes
        self.data_aquisicao = data_aquisicao
        self.estado = estado
        self.vida_util = vida_util
        self.valor = valor
        self.status = status
        self.nome = nome

class Switch:
    def __init__(self, id_switch, nome, especificacoes, valor, data_aquisicao, estado, vida_util, status):
        self.id_switch = 'RES' + id_switch
        self.tipo = 'Switch'
        self.especificacoes = especificacoes
        self.data_aquisicao = data_aquisicao
        self.estado = estado
        self.vida_util = vida_util
        self.valor = valor
        self.status = status
        self.nome = nome

class Patch_panel:
    def __init__(self, id_patch_panel, nome, especificacoes, valor, data_aquisicao, estado, vida_util, status):
        self.id_patch_panel = 'REPP' + id_patch_panel
        self.tipo = 'Patch Panel'
        self.especificacoes = especificacoes
        self.data_aquisicao = data_aquisicao
        self.estado = estado
        self.vida_util = vida_util
        self.valor = valor
        self.status = status
        self.nome = nome

class Estabilizador:
    def __init__(self, id_estabilizador, nome, especificacoes, valor, data_aquisicao, estado, vida_util, status):
        self.id_estabilizador = 'REE' + id_estabilizador
        self.tipo = 'Estabilizador'
        self.especificacoes = especificacoes
        self.data_aquisicao = data_aquisicao
        self.estado = estado
        self.vida_util = vida_util
        self.valor = valor
        self.status = status
        self.nome = nome