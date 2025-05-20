import sqlite3
import os

def get_connection():
    base_dir = os.path.dirname(__file__)
    db_path = os.path.join(base_dir, "ativos.db")
    conn = sqlite3.connect(db_path)
    return conn

def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    tabelas = [
        "Computador", "Rede", "Segurança", "Climatização", "Iluminação", "Mobília", "Licença", "Software", "Marca"
    ]

    for tabela in tabelas:
        cursor.execute(f'''
            CREATE TABLE IF NOT EXISTS "{tabela}" (
                id TEXT PRIMARY KEY,
                tipo TEXT,
                nome TEXT,
                especificacoes TEXT,
                valor INTEGER,
                estado TEXT,
                data_aquisicao TEXT,
                vida_util INTEGER,
                status TEXT
            )
        ''')

    conn.commit()
    conn.close()