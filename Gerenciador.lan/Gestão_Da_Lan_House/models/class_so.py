class Software_gerenciamento:
    def __init__(self, id_software_gerenciamento, especificacoes, valor, data_aquisicao, estado, vida_util):
        
        self.id_software_gerenciamento = 'SOGE' + id_software_gerenciamento
        self.nome = 'Software de Gerenciamento'
        self.especificacoes = especificacoes
        self.data_aquisicao = data_aquisicao
        self.estado = estado
        self.vida_util = vida_util
        self.valor = valor

        def mudar_estado(self, novo_estado):
            self.estado = novo_estado

class Banco_de_dados:
    def __init__(self, id_banco_de_dados, especificacoes, valor, data_aquisicao, estado, vida_util):
        
        self.id_banco_de_dados = 'SOBD' + id_banco_de_dados
        self.nome = 'Banco de Dados'
        self.especificacoes = especificacoes
        self.data_aquisicao = data_aquisicao
        self.estado = estado
        self.vida_util = vida_util
        self.valor = valor

        def mudar_estado(self, novo_estado):
            self.estado = novo_estado

class Website:
    def __init__(self, id_website, especificacoes, valor, data_aquisicao, estado, vida_util):
        
        self.id_website = 'WEBS' + id_website
        self.nome = 'Website próprio'
        self.especificacoes = especificacoes
        self.data_aquisicao = data_aquisicao
        self.estado = estado
        self.vida_util = vida_util
        self.valor = valor

        def mudar_estado(self, novo_estado):
            self.estado = novo_estado