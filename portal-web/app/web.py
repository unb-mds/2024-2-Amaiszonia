import streamlit as st
import pandas as pd
import folium
import requests
from streamlit_folium import st_folium
from streamlit_option_menu import option_menu
import def_funcao

# Carregar dados
@st.cache_data
def load_data(nome):
    return pd.read_csv("../data/" + nome)

st.set_page_config(page_title="Portal Datazonia", layout="wide")

st.markdown("""
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet">        
    <div style="text-align: center;">
        <h3 class="mb-0">Bem-vindo (a) ao</h3>
        <h1 class="mt-0"> Portal A+zônia</h1>
    </div>
""", unsafe_allow_html=True)

# Lista de estados da AL
estados_amazonia_legal = ["Acre", "Amapá", "Amazonas", "Maranhão", "Mato Grosso", "Pará", "Rondônia", "Roraima", "Tocantins"]

def criar_mapa():
    # Centro aproximado da Amazônia Legal
    centro_mapa = [-6.4653, -58.2159]  # Latitude e Longitude do centro
    mapa = folium.Map(location=centro_mapa, zoom_start=4.55, control_scale=True)
    
    # Carregar arquivo GeoJSON com as fronteiras dos estados (ajuste o caminho conforme necessário)
    geojson_url = "https://raw.githubusercontent.com/codeforamerica/click_that_hood/master/public/data/brazil-states.geojson"
    response = requests.get(geojson_url)
    geojson = response.json()
    
    # Filtrando os estados da Amazônia Legal
    geojson["features"] = [
        feature for feature in geojson["features"]
        if feature["properties"]["name"] in estados_amazonia_legal
    ]
    
    # Adicionando os estados ao mapa
    # Adicionando o GeoJSON filtrado no mapa
    folium.GeoJson(
        geojson,
        name="Estados da Amazônia Legal",
        style_function=lambda feature: {
            "fillColor": "cyan",
            "color": "black",
            "weight": 2,
            "fillOpacity": 0.5,
        },
        tooltip=folium.GeoJsonTooltip(fields=["name"], aliases=["Estado:"]),
    ).add_to(mapa)

    return mapa

# Menu inicial
selected = option_menu(
    menu_title=None,
    options=["Início", "Sobre nós"],
    icons=['house', 'book'],
    menu_icon='cast', 
    default_index=0,
    orientation='horizontal',
)

if selected == "Início":
    # Mapa da Amazonia Legal
    st.markdown("""
            <h2>Amazônia Legal </h2>
            <h4>O mapa abaixo destaca os estados que fazem parte da Amazônia Legal. </h4>    
    """, unsafe_allow_html=True)
    mapa = criar_mapa()
    st_folium(mapa, width=900, height=500)
    
    # Dados - Emissão CO2 Per Capita
    dadosCO2 = load_data("emissaoCO2.csv")
    st.markdown("## Emissão de CO2")
    st.write("""
        ##### Os dados abaixo apresentam um comparativo entre os indíces de emissão de CO2 no Brasil todo e estados da Amazônia Legal.
    """)
    st.bar_chart(dadosCO2, x="Ano", y=["Amazonia Legal", "Brasil"], height=350)
    
    # Dados - Foco de Queimadas - Brasil x AL
    dadosFOCO = load_data('foco_queimadas.csv')
    st.markdown("## Foco de Queimadas")
    ("""
        ##### Os dados abaixo apresentam um comparativo entre os indíces de foco de queimadas no Brasil todo e estados da Amazônia Legal.
    """)
    st.line_chart(dadosFOCO, x="Ano", y=["Amazonia Legal", "Brasil"], height=350)
    
    # Dados - Desmatamento Acumulado
    dadosDAM = load_data('desmatamento_acumulado.csv')
    st.markdown("## Desmatamento Acumulado")
    ("""
        ##### Os dados abaixo apresentam um comparativo entre os indíces de desmatamento acumulado no Brasil todo e estados da Amazônia Legal.
    """)
    st.bar_chart(dadosDAM, x="Ano", y=["Amazonia Legal", "Brasil"], height=350)
    
    # Dados - FRP e Risco Fogo, por município da AL
    dadosFRP = load_data('dados_filtrados.csv')
    st.markdown('## FRP e Risco Fogo')
    st.markdown("""
        ### Fire Radiative Power (FRP)

        * O FRP (Potência Radiativa do Fogo) mede a energia térmica emitida por um incêndio em megawatts (MW).
        * Ele é estimado a partir de imagens de satélite e indica a intensidade do fogo.
        * Quanto maior o FRP, mais intenso e energético é o incêndio.
        
        ### Risco de Fogo

        * O Risco de Fogo é um índice que estima a probabilidade de ocorrência de incêndios com base em fatores ambientais.
        * Considera variáveis como temperatura, umidade, precipitação e quantidade de dias sem chuva.
        * Um valor alto indica condições favoráveis para a propagação do fogo.    
    """, unsafe_allow_html=True)
    
    municipios = def_funcao.get_municipios()
    
    if municipios:
        municipio_selecionado = st.selectbox("Selecione um município:", sorted(municipios))
        
        # Requisição para obter dados do risco de fogo e FRP do município selecionado
        dados_municipio = def_funcao.get_risco_fogo(municipio_selecionado)
        
        if dados_municipio:
            st.write(f'Dados sobre o município **{municipio_selecionado}**')
            st.write(f"Risco de Fogo: {dados_municipio['RiscoFogo']}")
            st.write(f"FRP: {dados_municipio['FRP']}")

            # Criar o gráfico de RiscoFogo e FRP
            st.bar_chart({
                "FRP": dados_municipio['FRP'],
                "RiscoFogo": dados_municipio['RiscoFogo']
            }, height=200, width=20)

if selected == "Sobre nós":
    st.markdown("""
        <h1> Portal Datazônia </h1>         
        """, unsafe_allow_html=True)
    st.markdown("""
        <h3> O <a href="https://github.com/unb-mds/2024-2-Squad10/">Portal Datazonia</a> é um projeto que visa monitorar dados ambientais referentes aos estados da Amazônia Legal. </h3>

    """, unsafe_allow_html=True)