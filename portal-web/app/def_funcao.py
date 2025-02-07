import requests
import streamlit as st

def get_municipios():
    response = requests.get("http://localhost:8000/municipios")  # Substitua pelo URL correto da sua API
    if response.status_code == 200:
        return response.json()  # Retorna a lista de municípios
    else:
        st.error("Erro ao carregar os municípios.")
        return []

def get_risco_fogo(municipio: str):
    response = requests.get(f"http://localhost:8000/municipio/{municipio}")  # Substitua pelo URL correto da sua API
    if response.status_code == 200:
        return response.json()  # Retorna os dados de risco de fogo e FRP
    else:
        st.error("Erro ao carregar os dados do município.")
        return None
