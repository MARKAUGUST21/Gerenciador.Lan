from models import *

class AtivoController:
    def __init__(self):
        self.ativos = []

    def adicionar_ativo(self, ativo):
        self.ativos.append(ativo)

    def listar_ativos(self):
        return self.ativos

    def remover_ativo_por_id(self, id):
        self.ativos = [a for a in self.ativos if a.id != id]