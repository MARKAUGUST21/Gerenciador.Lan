class Contato:
    def __init__(self, id_contato, especificacoes, valor, data_aquisicao, estado, vida_util):
        
        self.id_contato = 'CONT' + id_contato
        self.nome = 'Contato'
        self.especificacoes = especificacoes
        self.data_aquisicao = data_aquisicao
        self.estado = estado
        self.vida_util = vida_util
        self.valor = valor

        def mudar_estado(self, novo_estado):
            self.estado = novo_estado

class Divulgação:
    def __init__(self, id_divulgacao, especificacoes, valor, data_aquisicao, estado, vida_util):
        
        self.id_divulgacao = 'DIVU' + id_divulgacao
        self.nome = 'Divulgação'
        self.especificacoes = especificacoes
        self.data_aquisicao = data_aquisicao
        self.estado = estado
        self.vida_util = vida_util
        self.valor = valor

        def mudar_estado(self, novo_estado):
            self.estado = novo_estado

class Identidade_digital:
    def __init__(self, id_identidade_digital, especificacoes, valor, data_aquisicao, estado, vida_util):
        
        self.id_identidade_digital = 'IDDI' + id_identidade_digital
        self.nome = 'Identidade Digital'
        self.especificacoes = especificacoes
        self.data_aquisicao = data_aquisicao
        self.estado = estado
        self.vida_util = vida_util
        self.valor = valor

        def mudar_estado(self, novo_estado):
            self.estado = novo_estado