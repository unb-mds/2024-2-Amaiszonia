""" Este módulo contém funções para criar a API e interagir com o banco de dados SQLite. """
import sqlite3
from typing import List
from pydantic import BaseModel
from fastapi import FastAPI

app = FastAPI()

def get_db_connection():
    """
    Estabelece uma conexão com o banco de dados SQLite.

    Returns:
        sqlite3.Connection: A conexão com o banco de dados.
    """
    conn = sqlite3.connect('../data/dados.db')
    conn.row_factory = sqlite3.Row
    return conn

class Data(BaseModel):
    """
    Modelo Pydantic para representar os dados de CO2, DAM, Foco e outros dados relacionados.

    Attributes:
        id (int): O identificador único.
        ano (int): O ano da medição.
        Brasil (float): O valor para o Brasil.
        AL (float): O valor para a Amazonia Legal.
    """
    id: int
    ano: int
    Brasil: float
    AL: float

@app.get("/co2", response_model=List[Data])
def get_co2_data():
    """
    Retorna os dados de CO2 do banco de dados.

    Returns:
        List[Data]: Uma lista de objetos Data com os dados de CO2.
    """
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM co2_data')
    dados = cursor.fetchall()
    conn.close()

    result = []
    for row in dados:
        result.append(Data(
            id=row['id'],
            ano=row['ano'],
            Brasil=row['Brasil'],
            AL=row['AL']
        ))

    return result

@app.get("/dam", response_model=List[Data])
def get_dam_data():
    """
    Retorna os dados de Desmatamento acumulado(DAM) do banco de dados.

    Returns:
        List[Data]: Uma lista de objetos Data com os dados de DAM.
    """
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM dam_data')
    dados = cursor.fetchall()
    conn.close()

    result = []
    for row in dados:
        result.append(Data(
            id=row['id'],
            ano=row['ano'],
            Brasil=row['Brasil'],
            AL=row['AL']
        ))

    return result

@app.get("/foco", response_model=List[Data])
def get_foco_data():
    """
    Retorna os dados de Foco do banco de dados.

    Returns:
        List[Data]: Uma lista de objetos Data com os dados de Foco.
    """
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM foco_data')
    dados = cursor.fetchall()
    conn.close()

    result = []
    for row in dados:
        result.append(Data(
            id=row['id'],
            ano=row['ano'],
            Brasil=row['Brasil'],
            AL=row['AL']
        ))

    return result

@app.get("/municipios", response_model=list[str])
def get_municipios():
    """
    Retorna uma lista de municípios disponíveis no banco de dados.

    Returns:
        list[str]: Lista de nomes de municípios.
    """
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT DISTINCT Municipio FROM filtrados_data ORDER BY Municipio")
    municipios = [row["Municipio"] for row in cursor.fetchall()]

    conn.close()
    return municipios

@app.get("/municipio/{municipio}")
def get_risco_fogo(municipio: str):
    """
    Retorna o risco de fogo e o FRP para um município específico.

    Args:
        municipio (str): Nome do município para o qual buscar os dados.

    Returns:
        dict: Um dicionário com o município, risco de fogo e FRP.
    """
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT Municipio, RiscoFogo, FRP FROM filtrados_data WHERE Municipio = ?",
        (municipio,)
    )

    resultado = cursor.fetchone()
    conn.close()

    return {
        "Municipio": resultado["Municipio"],
        "RiscoFogo": resultado["RiscoFogo"],
        "FRP": resultado["FRP"]
    }

if __name__ == '__main__':
    #Inicia o servidor Uvicorn para rodar a aplicação FastAPI.

    #O servidor será executado no endereço '0.0.0.0' na porta 8000.
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
