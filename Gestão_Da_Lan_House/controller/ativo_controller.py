from models import *
from utils.database import get_connection

class AtivoController:
    def __init__(self):
        self.tabelas = {
            "Computador": "Computador",
            "Monitor": "Computador",
            "Perifericos": "Computador",
            "Switch": "Rede",
            "Cabo_de_rede": "Rede",
            "Nobreak": "Rede",
            "Patch_panel": "Rede",
            "Roteador": "Rede",
            "Estabilizador": "Rede",
            "Ar_condicionado": "Climatização",
            "Licenca_jogo": "Licença",
            "Jogo_adicional": "Licença",
            "Sistema_operacional": "Licença",
            "Antivirus": "Licença",
            "Programa_edicao": "Licença",
            "Painel_led": "Iluminação",
            "Contato": "Marca",
            "Divulgacao": "Marca",
            "Identidade_digital": "Marca",
            "Mesa_computador": "Mobília",
            "Mesa_administracao": "Mobília",
            "Cadeira_computador": "Mobília",
            "Balcao_recepcao": "Mobília",
            "Piso_vinilico": "Mobília",
            "Decoracao": "Mobília",
            "Camera": "Segurança",
            "Alarme": "Segurança",
            "Software_gerenciamento": "Software",
            "Banco_de_dados": "Software",
            "Website": "Software",
            }

    def adicionar_ativo(self, ativo):
        conn = get_connection()
        cursor = conn.cursor()

        classe = ativo.__class__.__name__

        tabela = self.tabelas[classe]
        # Monta o dicionário de campos exigidos
        dados = {
            "id": getattr(ativo, 'id', ''),
            "tipo": getattr(ativo, 'tipo', ''),
            "nome": getattr(ativo, 'nome', ''),
            "especificacoes": getattr(ativo, 'especificacoes', ''),
            "valor": int(getattr(ativo, 'valor', 0)),
            "estado": getattr(ativo, 'estado', ''),
            "data_aquisicao": getattr(ativo, 'data_aquisicao', ''),
            "vida_util": int(getattr(ativo, 'vida_util', 0)),
            "status": getattr(ativo, 'status', '')
        }

        cursor.execute(f'''
            INSERT INTO "{tabela}" (id, tipo, nome, especificacoes, valor, estado, data_aquisicao, vida_util, status)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            dados["id"],
            dados["tipo"],
            dados["nome"],
            dados["especificacoes"],
            dados["valor"],
            dados["estado"],
            dados["data_aquisicao"],
            dados["vida_util"],
            dados["status"]
        ))

        conn.commit()
        conn.close()

    def listar_ativos(self, tabela):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(f'SELECT * FROM "{tabela}"')
        ativos = cursor.fetchall()
        conn.close()
        return ativos

    def remover_ativo_por_id(self, id):
        self.ativos = [a for a in self.ativos if a.id != id]