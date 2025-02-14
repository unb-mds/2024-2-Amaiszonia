"""modulo para funcoes e requisicoes da api"""
import time
import os
import sqlite3
import pandas as pd
import requests
import streamlit as st
# from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from dotenv import load_dotenv

load_dotenv()


def get_municipios():
    """
    Obtém a lista de municípios da API.

    Returns:
        list: Lista de municípios ou uma lista vazia em caso de erro.
    """
    try:
        response = requests.get("http://localhost:8000/municipios", timeout=10)
        response.raise_for_status()  # erro se o status não for 200
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Erro ao carregar os municípios: {e}")
        return []


def get_risco_fogo(municipio: str):
    """
    Obtém os dados de risco de fogo para um município específico.

    Args:
        municipio (str): O nome do município para obter os dados de risco de fogo.

    Returns:
        dict or None: Dados do risco de fogo ou None em caso de erro.
    """
    try:
        response = requests.get(
            f"http://localhost:8000/municipio/{municipio}",
            timeout=10)
        response.raise_for_status()  # erro se o status não for 200
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Erro ao carregar os dados do município '{municipio}': {e}")
        return None

CAMINHO = os.getenv("CAMINHO")
DOWNLOAD_DIR = CAMINHO
DB_PATH = "../data/dados.db"

TABELA_ATUAL = None


def definir_tabela(nome_tabela):
    """Define para qual tabela os dados serão enviados."""
    global TABELA_ATUAL
    TABELA_ATUAL = nome_tabela
    print(f"Tabela definida: {TABELA_ATUAL}")


class DownloadHandler(FileSystemEventHandler):
    """
    Classe que manipula eventos de arquivos, como downloads,
    e os processa para inserir os dados no banco de dados.
    """

    def __init__(self, observer):
        super().__init__()
        self.observer = observer

    def on_created(self, event):
        """Chamado quando um novo arquivo é detectado na pasta."""
        if event.is_directory:
            return

        file_path = event.src_path
        file_name = os.path.basename(file_path)

        if file_name.endswith(".crdownload") or file_name.startswith(
                ".com.google.Chrome"):
            print(f"Ignorando arquivo temporário: {file_name}")
            return

        time.sleep(4)  # Aguarda o download terminar

        if TABELA_ATUAL:
            self.process_csv(file_path, TABELA_ATUAL)
            self.observer.stop()  # Para a observação após a inserção dos dados
        else:
            print(
                f"Nenhuma tabela foi definida para {file_name}, ignorando.")

    def process_csv(self, file_path, table_name):
        """Lê o arquivo CSV e insere os dados na tabela correta."""
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        df = pd.read_csv(file_path, sep=None, engine="python")
        df.columns = df.columns.str.strip()
        if table_name == "co2":
            cursor.execute("""
                    CREATE TABLE IF NOT EXISTS co2_data (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        Ano INTEGER,
                        Brasil REAL,
                        AL REAL
                    )
                """)
            df.columns = [
                'Ano',
                'Brasil',
                'Nordeste',
                'Sudeste',
                'Sul',
                'Centro_Oeste',
                'AL']
            for _, row in df.iterrows():
                cursor.execute('''
                        INSERT INTO co2_data (Ano, Brasil, AL)
                        VALUES (?, ?, ?)
                        ''', (row['Ano'], row['Brasil'], row['AL']))
        elif table_name == "foco":
            cursor.execute('''
                    CREATE TABLE IF NOT EXISTS foco_data (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        Ano INTEGER,
                        Brasil REAL,
                        AL REAL
                    )
                ''')
            df.columns = [
                'Ano',
                'Brasil',
                'Nordeste',
                'Sudeste',
                'Sul',
                'Centro_Oeste',
                'AL']
            for _, row in df.iterrows():
                cursor.execute('''
                        INSERT INTO foco_data (Ano, Brasil, AL)
                        VALUES (?, ?, ?)
                        ''', (row['Ano'], row['Brasil'], row['AL']))
        elif table_name == "dam":
            cursor.execute('''
                    CREATE TABLE IF NOT EXISTS dam_data (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        Ano INTEGER,
                        Brasil REAL,
                        AL REAL
                    )
                ''')
            df = df.drop(columns=['dummy'])
            df.columns = [
                'Ano',
                'Brasil',
                'Nordeste',
                'Sudeste',
                'Sul',
                'Centro_Oeste',
                'AL']
            for _, row in df.iterrows():
                cursor.execute('''
                        INSERT INTO dam_data (Ano, Brasil, AL)
                        VALUES (?, ?, ?)
                        ''', (row['Ano'], row['Brasil'], row['AL']))
            # print("Dados antes da inserção:", df.head())
            # Usar o pandas para inserir diretamente os dados
            # df.to_sql(table_name, conn, if_exists='append', index=False)
            # cursor.execute("SELECT COUNT(*) FROM co2_data")
            # count = cursor.fetchone()[0]
            # print(f"Linhas inseridas na tabela co2_data: {count}")

        conn.commit()
        conn.close()
        print(f"Dados inseridos na tabela {table_name} com sucesso!")
        time.sleep(2)
        os.remove(file_path)  # Remove o arquivo após inserção
