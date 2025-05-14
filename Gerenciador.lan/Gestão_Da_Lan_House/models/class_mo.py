class Mesa_computador:
    def __init__(self, id_mesa_computador, especificacoes, valor, data_aquisicao, estado, vida_util):
        
        self.id_mesa_computador = 'MECO' + id_mesa_computador
        self.nome = 'Mesa para Computador'
        self.especificacoes = especificacoes
        self.data_aquisicao = data_aquisicao
        self.estado = estado
        self.vida_util = vida_util
        self.valor = valor

        def mudar_estado(self, novo_estado):
            self.estado = novo_estado

class Mesa_administracao:
    def __init__(self, id_mesa_administracao, especificacoes, valor, data_aquisicao, estado, vida_util):
        
        self.id_mesa_administracao = 'MERE' + id_mesa_administracao
        self.nome = 'Mesa para Computador Administração'
        self.especificacoes = especificacoes
        self.data_aquisicao = data_aquisicao
        self.estado = estado
        self.vida_util = vida_util
        self.valor = valor

        def mudar_estado(self, novo_estado):
            self.estado = novo_estado

class Cadeira_computador:
    def __init__(self, id_cadeira_computador, especificacoes, valor, data_aquisicao, estado, vida_util):
        
        self.id_cadeira_computador = 'CACO' + id_cadeira_computador
        self.nome = 'Cadeira para Computador'
        self.especificacoes = especificacoes
        self.data_aquisicao = data_aquisicao
        self.estado = estado
        self.vida_util = vida_util
        self.valor = valor

        def mudar_estado(self, novo_estado):
            self.estado = novo_estado

class Balcao_recepcao:
    def __init__(self, id_balcao_recepcao, especificacoes, valor, data_aquisicao, estado, vida_util):
        
        self.id_balcao_recepcao = 'BARE' + id_balcao_recepcao
        self.nome = 'Balcao para Recepção'
        self.especificacoes = especificacoes
        self.data_aquisicao = data_aquisicao
        self.estado = estado
        self.vida_util = vida_util
        self.valor = valor

        def mudar_estado(self, novo_estado):
            self.estado = novo_estado

class Piso_vinilico:
    def __init__(self, id_piso_vinilico, especificacoes, valor, data_aquisicao, estado, vida_util):
        
        self.id_piso_vinilico = 'PIVI' + id_piso_vinilico
        self.nome = 'Piso Vinílico em Régua'
        self.especificacoes = especificacoes
        self.data_aquisicao = data_aquisicao
        self.estado = estado
        self.vida_util = vida_util
        self.valor = valor

        def mudar_estado(self, novo_estado):
            self.estado = novo_estado

class Decoracao:
    def __init__(self, id_decoracao, especificacoes, valor, data_aquisicao, estado, vida_util):
        
        self.id_decoracao = 'DEC' + id_decoracao
        self.nome = 'Decoração'
        self.especificacoes = especificacoes
        self.data_aquisicao = data_aquisicao
        self.estado = estado
        self.vida_util = vida_util
        self.valor = valor

        def mudar_estado(self, novo_estado):
            self.estado = novo_estado