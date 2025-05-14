class Licenca_jogo:
    def __init__(self, id_licenca_jogo, especificacoes, valor, data_aquisicao, estado, vida_util):
        
        self.id_licenca_jogo = 'LIJO' + id_licenca_jogo
        self.nome = 'Licenças de Jogos (Anual)'
        self.especificacoes = especificacoes
        self.data_aquisicao = data_aquisicao
        self.estado = estado
        self.vida_util = vida_util
        self.valor = valor

        def mudar_estado(self, novo_estado):
            self.estado = novo_estado

class Jogo_adicional:
    def __init__(self, id_jogo_adicional, especificacoes, valor, data_aquisicao, estado, vida_util):
        
        self.id_jogo_adicional = 'JOAD' + id_jogo_adicional
        self.nome = 'Jogos Adicionais'
        self.especificacoes = especificacoes
        self.data_aquisicao = data_aquisicao
        self.estado = estado
        self.vida_util = vida_util
        self.valor = valor

        def mudar_estado(self, novo_estado):
            self.estado = novo_estado

class Sistema_operacional:
    def __init__(self, id_sistema_operacional, especificacoes, valor, data_aquisicao, estado, vida_util):
        
        self.id_sistema_operacional = 'SIOP' + id_sistema_operacional
        self.nome = 'Sistema Operacional'
        self.especificacoes = especificacoes
        self.data_aquisicao = data_aquisicao
        self.estado = estado
        self.vida_util = vida_util
        self.valor = valor

        def mudar_estado(self, novo_estado):
            self.estado = novo_estado

class Antivirus:
    def __init__(self, id_antivirus, especificacoes, valor, data_aquisicao, estado, vida_util):
        
        self.id_antivirus = 'ANVI' + id_antivirus
        self.nome = 'Antivírus'
        self.especificacoes = especificacoes
        self.data_aquisicao = data_aquisicao
        self.estado = estado
        self.vida_util = vida_util
        self.valor = valor

        def mudar_estado(self, novo_estado):
            self.estado = novo_estado

class Programa_edicao:
    def __init__(self, id_programa_edicao, especificacoes, valor, data_aquisicao, estado, vida_util):
        
        self.id_programa_edicao = 'PRED' + id_programa_edicao
        self.nome = 'Programa de Edição'
        self.especificacoes = especificacoes
        self.data_aquisicao = data_aquisicao
        self.estado = estado
        self.vida_util = vida_util
        self.valor = valor

        def mudar_estado(self, novo_estado):
            self.estado = novo_estado