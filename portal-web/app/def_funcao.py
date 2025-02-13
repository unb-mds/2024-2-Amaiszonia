"""modulo para funcoes e requisicoes da api"""
import requests
import streamlit as st

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
        response = requests.get(f"http://localhost:8000/municipio/{municipio}", timeout=10)
        response.raise_for_status()  #erro se o status não for 200
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Erro ao carregar os dados do município '{municipio}': {e}")
        return None
