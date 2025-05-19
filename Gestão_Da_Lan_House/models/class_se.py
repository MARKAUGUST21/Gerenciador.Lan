class Camera:
    def __init__(self, id_camera, nome, especificacoes, valor, data_aquisicao, estado, vida_util, status):
        self.id_camera = 'SEC' + id_camera
        self.tipo = 'Câmera de Segurança'
        self.especificacoes = especificacoes
        self.data_aquisicao = data_aquisicao
        self.estado = estado
        self.vida_util = vida_util
        self.valor = valor
        self.status = status
        self.nome = nome

class Alarme:
    def __init__(self, id_alarme, nome, especificacoes, valor, data_aquisicao, estado, vida_util, status):
        self.id_alarme = 'SESA' + id_alarme
        self.tipo = 'Sistema de Alarme'
        self.especificacoes = especificacoes
        self.data_aquisicao = data_aquisicao
        self.estado = estado
        self.vida_util = vida_util
        self.valor = valor
        self.status = status
        self.nome = nome