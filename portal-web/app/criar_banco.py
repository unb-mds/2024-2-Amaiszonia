"""
Este módulo contém funções para criar e interagir com o banco de dados SQLite.
Ele realiza operações de criação de tabelas e inserção de dados no banco.
"""
import os
import sqlite3
#import pandas as pd

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, '../data/')
DB_PATH = os.path.join(DATA_PATH, 'dados.db')

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS co2_data (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    Ano INTEGER,
    Brasil REAL,
    AL REAL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS foco_data (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    Ano INTEGER,
    Brasil REAL,
    AL REAL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS dam_data (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    Ano INTEGER,
    Brasil REAL,
    Al REAL
)
''')
cursor.execute('''
CREATE TABLE IF NOT EXISTS filtrados_data (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    Estado VARCHAR(30),
    Municipio VARCHAR(30),
    RiscoFogo REAL,
    FRP REAL
)
''')

# dadosCO2 = pd.read_csv(os.path.join(DATA_PATH, 'emissaoCO2.csv'))
# dadosFOCO = pd.read_csv(os.path.join(DATA_PATH, 'foco_queimadas.csv'))
# dadosDAM = pd.read_csv(os.path.join(DATA_PATH, 'desmatamento_acumulado.csv'))
# dadosFILT = pd.read_csv(os.path.join(DATA_PATH, 'dados_filtrados.csv'))

# for _, row in dadosCO2.iterrows():
#     cursor.execute('''
#     INSERT INTO co2_data (Ano, Brasil, AL)
#     VALUES (?, ?, ?)
#     ''', (row['Ano'], row['Brasil'], row['Amazonia Legal']))

# for _, row in dadosFOCO.iterrows():
#     cursor.execute('''
#     INSERT INTO foco_data (Ano, Brasil, AL)
#     VALUES (?, ?, ?)
#     ''', (row['Ano'], row['Brasil'], row['Amazonia Legal']))

# for _, row in dadosDAM.iterrows():
#     cursor.execute('''
#     INSERT INTO dam_data (Ano, Brasil, AL)
#     VALUES (?, ?, ?)
#     ''', (row['Ano'], row['Brasil'], row['Amazonia Legal']))

# for _, row in dadosFILT.iterrows():
#     cursor.execute('''
#     INSERT INTO filtrados_data(Estado, Municipio, RiscoFogo, FRP)
#     VALUES (?, ?, ?, ?)
#     ''', (row['Estado'], row['Municipio'], row['RiscoFogo'],row['FRP'])
#                    )

conn.commit()
conn.close()

print("Banco de dados atualizado com sucesso!")
