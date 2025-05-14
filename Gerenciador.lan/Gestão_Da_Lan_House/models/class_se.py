class Camera:
    def __init__(self, id_camera, especificacoes, valor, data_aquisicao, estado, vida_util):
        
        self.id_camera = 'SEC' + id_camera
        self.nome = 'Câmera de Segurança'
        self.especificacoes = especificacoes
        self.data_aquisicao = data_aquisicao
        self.estado = estado
        self.vida_util = vida_util
        self.valor = valor

        def mudar_estado(self, novo_estado):
            self.estado = novo_estado

class Alarme:
    def __init__(self, id_alarme, especificacoes, valor, data_aquisicao, estado, vida_util):
        
        self.id_alarme = 'SESA' + id_alarme
        self.nome = 'Sistema de Alarme'
        self.especificacoes = especificacoes
        self.data_aquisicao = data_aquisicao
        self.estado = estado
        self.vida_util = vida_util
        self.valor = valor

        def mudar_estado(self, novo_estado):
            self.estado = novo_estado