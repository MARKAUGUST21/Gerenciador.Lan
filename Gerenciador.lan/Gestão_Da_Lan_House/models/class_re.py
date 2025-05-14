class Roteador:
    def __init__(self, id_roteador, especificacoes, valor, data_aquisicao, estado, vida_util):
        
        self.id_roteador = 'RER' + id_roteador
        self.nome = 'Roteador de Dual Band'
        self.especificacoes = especificacoes
        self.data_aquisicao = data_aquisicao
        self.estado = estado
        self.vida_util = vida_util
        self.valor = valor

        def mudar_estado(self, novo_estado):
            self.estado = novo_estado

class Cabo_de_rede:
    def __init__(self, id_cabo_de_rede, especificacoes, valor, data_aquisicao, estado, vida_util):
        
        self.id_cabo_de_rede = 'REC' + id_cabo_de_rede
        self.nome = 'Cabo de Rede'
        self.especificacoes = especificacoes
        self.data_aquisicao = data_aquisicao
        self.estado = estado
        self.vida_util = vida_util
        self.valor = valor

        def mudar_estado(self, novo_estado):
            self.estado = novo_estado

class Nobreak:
    def __init__(self, id_nobreak, especificacoes, valor, data_aquisicao, estado, vida_util):
        
        self.id_nobreak = 'REN' + id_nobreak
        self.nome = 'Nobreak'
        self.especificacoes = especificacoes
        self.data_aquisicao = data_aquisicao
        self.estado = estado
        self.vida_util = vida_util
        self.valor = valor

        def mudar_estado(self, novo_estado):
            self.estado = novo_estado

class Switch:
    def __init__(self, id_switch, especificacoes, valor, data_aquisicao, estado, vida_util):
        
        self.id_switch = 'RES' + id_switch
        self.nome = 'Switch'
        self.especificacoes = especificacoes
        self.data_aquisicao = data_aquisicao
        self.estado = estado
        self.vida_util = vida_util
        self.valor = valor

        def mudar_estado(self, novo_estado):
            self.estado = novo_estado

class Patch_panel:
    def __init__(self, id_patch_panel, especificacoes, valor, data_aquisicao, estado, vida_util):
        
        self.id_patch_panel = 'REPP' + id_patch_panel
        self.nome = 'Patch Panel'
        self.especificacoes = especificacoes
        self.data_aquisicao = data_aquisicao
        self.estado = estado
        self.vida_util = vida_util
        self.valor = valor

        def mudar_estado(self, novo_estado):
            self.estado = novo_estado

class Estabilizador:
    def __init__(self, id_estabilizador, especificacoes, valor, data_aquisicao, estado, vida_util):
        
        self.id_estabilizador = 'REE' + id_estabilizador
        self.nome = 'Estabilizador'
        self.especificacoes = especificacoes
        self.data_aquisicao = data_aquisicao
        self.estado = estado
        self.vida_util = vida_util
        self.valor = valor

        def mudar_estado(self, novo_estado):
            self.estado = novo_estado