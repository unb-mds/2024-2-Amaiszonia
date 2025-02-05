from fastapi import FastAPI
import sqlite3
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Função para conectar ao banco de dados SQLite
def get_db_connection():
    conn = sqlite3.connect('../data/dados.db')
    conn.row_factory = sqlite3.Row  # Para obter resultados como dicionários
    return conn

# Definindo o modelo para os dados
class Data(BaseModel):
    id: int
    ano: int
    Brasil: float
    AL: float

# Endpoint para obter dados CO2
@app.get("/co2", response_model=List[Data])
def get_co2_data():
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

# Endpoint para obter dados Dam
@app.get("/dam", response_model=List[Data])
def get_dam_data():
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

# Endpoint para obter dados foco
@app.get("/foco", response_model=List[Data])
def get_foco_data():
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
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute("SELECT DISTINCT Municipio FROM filtrados_data ORDER BY Municipio")
    municipios = [row["Municipio"] for row in cursor.fetchall()]
    
    conn.close()
    return municipios

@app.get("/municipio/{municipio}")
def get_risco_fogo(municipio: str):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT Municipio, RiscoFogo, FRP FROM filtrados_data WHERE Municipio = ?",
        (municipio,)
    )
    
    resultado = cursor.fetchone()
    conn.close()

    return{
            "Municipio": resultado["Municipio"],
            "RiscoFogo": resultado["RiscoFogo"],
            "FRP": resultado["FRP"]
        }

# Iniciar a aplicação com Uvicorn
if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)