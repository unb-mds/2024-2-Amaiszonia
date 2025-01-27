import streamlit as st
import pandas as pd
import numpy as np

# Configuração da página
st.set_page_config(page_title="Portal A+zônia", layout="wide")

# Estados da Amazônia Legal
estados_amazonia = [
    "Acre", "Amapá", "Amazonas", "Maranhão", "Mato Grosso", "Pará", "Rondônia", "Roraima", "Tocantins"
]

# Simulação de dados para o mapa (dados fictícios para coordenadas) depois a gente tem que adicionar um arquivo csv com as coordenadas)
coordenadas_estados = {
    "Acre": [(-9.97, -67.8), (-10.1, -67.7)],
    "Amapá": [(1.4, -51.8), (1.5, -51.9)],
    "Amazonas": [(-3.1, -60.0), (-4.1, -61.2)],
    "Maranhão": [(-2.5, -44.3), (-3.2, -44.5)],
    "Mato Grosso": [(-12.6, -55.0), (-13.5, -56.0)],
    "Pará": [(-1.5, -48.5), (-1.7, -48.7)],
    "Rondônia": [(-11.4, -61.4), (-12.3, -62.3)],
    "Roraima": [(2.8, -60.7), (3.1, -61.1)],
    "Tocantins": [(-10.2, -48.3), (-10.5, -48.7)],
}

# Seção: Início
st.markdown("# Início")
# filtro pra filtrar por estados 
estado_selecionado = st.sidebar.selectbox(
    "Selecione o estado para consulta:",
    estados_amazonia
)

# Dados do mapa para o estado (fictícios também)
dados_mapa = pd.DataFrame(
    coordenadas_estados[estado_selecionado],
    columns=["lat", "lon"]
)

# Título para o mapa
st.markdown(f"## Mapa de localizações no estado: {estado_selecionado}")
st.map(dados_mapa)

# Aqui coloquei só uma simulação de dados de queimadas (fictícios) pra testar, tem que alterar ainda 
dados_queimadas = pd.DataFrame({
    "Mês": [
        "Janeiro", "Fevereiro", "Março", "Abril", "Maio", 
        "Junho", "Julho", "Agosto", "Setembro", "Outubro", 
        "Novembro", "Dezembro"
    ],
    "Queimadas": np.random.randint(50, 500, size=12)
})

# Seção: Dados
st.markdown("# Dados")
# Título do gráfico
st.markdown("## Gráfico de queimadas por mês")
st.bar_chart(dados_queimadas.set_index("Mês"))

# Titulo adicional por estado. 
st.markdown(f"### Dados de queimadas no estado: {estado_selecionado}")