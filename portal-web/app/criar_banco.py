import os
import sqlite3
import pandas as pd

# Configurar caminhos corretos
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, '../data/')
DB_PATH = os.path.join(DATA_PATH, 'dados.db')

# Conectar ao banco de dados SQLite
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# Criar as tabelas
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

# Carregar dados dos CSVs
dadosCO2 = pd.read_csv(os.path.join(DATA_PATH, 'emissaoCO2.csv'))
dadosFOCO = pd.read_csv(os.path.join(DATA_PATH, 'foco_queimadas.csv'))
dadosDAM = pd.read_csv(os.path.join(DATA_PATH, 'desmatamento_acumulado.csv'))
print(dadosCO2)
print(dadosFOCO)
print(dadosDAM)
# Inserir dados no banco
for _, row in dadosCO2.iterrows():
    cursor.execute('''
    INSERT INTO co2_data (Ano, Brasil, AL)
    VALUES (?, ?, ?)
    ''', (row['Ano'], row['Brasil'], row['Amazonia Legal']))

for _, row in dadosFOCO.iterrows():
    cursor.execute('''
    INSERT INTO foco_data (Ano, Brasil, AL)
    VALUES (?, ?, ?)
    ''', (row['Ano'], row['Brasil'], row['Amazonia Legal']))

for _, row in dadosDAM.iterrows():
    cursor.execute('''
    INSERT INTO dam_data (Ano, Brasil, AL)
    VALUES (?, ?, ?)
    ''', (row['Ano'], row['Brasil'], row['Amazonia Legal']))

# Confirmar e fechar conexão
conn.commit()
conn.close()

print("Banco de dados atualizado com sucesso!")
