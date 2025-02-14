import streamlit as st
import pandas as pd
import plotly.express as px
import folium
import requests
from streamlit_folium import st_folium
import def_funcao
import base64

# Função para carregar dados (cache para desempenho)
@st.cache_data
def load_data(nome):
    return pd.read_csv(f"../data/{nome}")

# Configuração da página
st.set_page_config(page_title="Portal Datazônia", layout="wide", page_icon="🌍")

# Custom CSS para fundo branco e correção dos gráficos
st.markdown(
    """
    <style>
    html, body, [data-testid="stAppViewContainer"] {
        background-color: #ffffff !important;
        color: #023616;
    }
    #MainMenu, header, footer { visibility: hidden; }
    .header {
        position: fixed;
        top: 0; left: 0; right: 0;
        background-color: #028436;
        padding: 1rem 2rem;
        z-index: 1000;
        display: flex;
        align-items: center;
        justify-content: space-between;
    }
    .header h1 { margin: 0; font-size: 2rem; color: white; }
    .nav-links a {
        color: white; margin-left: 1rem;
        text-decoration: none; font-weight: bold; font-size: 1.1rem;
    }
    .nav-links a:hover { text-decoration: underline; }
    .spacer { margin-top: 50px; }
    .section-title { color: #028436; margin-top: 1rem; text-align: center; }
    .map-container { text-align: center; }
    .metric-container {
        color: #023616 !important;
        font-weight: bold;
        font-size: 20px;
        
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Função para converter imagem em Base64
def get_image_base64(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# Caminho correto da imagem 
logo_path = "pictures/logo_white.png"

# Converter imagem para Base64
logo_base64 = get_image_base64(logo_path)

# Cabeçalho fixo com fundo verde e altura reduzida
st.markdown(
    f"""
    <style>
    .header {{
        position: fixed;
        top: 0; left: 0; right: 0;
        background-color: #028436;
        padding: 0.5rem 1rem; 
        z-index: 1000;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        text-align: center;
    }}
    .header img {{
        max-width: 180px; 
        height: auto;
    }}
    .nav-links {{
        margin-top: 0.3rem;
    }}
    .nav-links a {{
        color: white;
        text-decoration: none;
        font-weight: bold;
        font-size: 1rem; 
        margin: 0 0.8rem;
    }}
    .nav-links a:hover {{
        text-decoration: underline;
    }}
    </style>

    <div class="header">
        <img src="data:image/png;base64,{logo_base64}" alt="Logo Datazônia">
        <div class="nav-links">
            <a href="/" target="_self">Início</a>
            <a href="/?page=Sobre%20nós" target="_self">Sobre nós</a>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)


st.markdown('<div class="spacer"></div>', unsafe_allow_html=True)

# --- Função para criar gráficos com cores temáticas e renomear "Brasil" ---
def criar_grafico(df, x_col, y_cols, titulo, tipo="bar", cores=None):
    # Renomear a coluna "Brasil" para "Resto do Brasil"
    df = df.rename(columns={"Brasil": "Resto do Brasil"})
    y_cols = ["Resto do Brasil" if col == "Brasil" else col for col in y_cols]
    
    if tipo == "bar":
        fig = px.bar(df, x=x_col, y=y_cols, title=titulo, barmode="group", color_discrete_sequence=cores)
    else:
        fig = px.line(df, x=x_col, y=y_cols, title=titulo, markers=True, color_discrete_sequence=cores)
    
    # Personalização do layout
    fig.update_layout(
        plot_bgcolor="white",
        paper_bgcolor="white",
        font=dict(color="#023616"),
        title=dict(font=dict(color="#023616")),
        xaxis=dict(
            title=dict(text=x_col, font=dict(color="#023616")),
            tickfont=dict(color="#023616")
        ),
        yaxis=dict(
            title=dict(text="Valor", font=dict(color="#023616")),
            tickfont=dict(color="#023616")
        ),
        legend=dict(font=dict(color="#023616"))
    )
    return fig



# --- Recupera o parâmetro "page" da URL ---
query_params = st.query_params
page = query_params.get("page", None)
if isinstance(page, list):
    page = page[0] if len(page) > 0 else None
if page not in [None, "Sobre nós"]:
    st.query_params.clear()
    st.rerun()

# --- Seção "Sobre nós" ou Conteúdo Principal ---
if page == "Sobre nós":
# Seção Sobre Nós
    st.markdown(
    """
    <style>
        .about-container {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            text-align: center;
            width: 100%;
            margin: 0 auto;
        }
        .about-title {
            color: #023616;
            font-size: 2rem;
            font-weight: bold;
        }
        .about-text {
            font-size: 1.4rem; 
            line-height: 1.6;
            color: #023616;
            max-width: 900px; 
            margin: 0 auto;
        }
        .team-container {
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            gap: 20px;
            margin-top: 20px;
        }
        .team-member {
            text-align: center;
        }
        .team-member img {
            width: 100px;
            height: 100px;
            border-radius: 50%;
            border: 2px solid #028436;
        }
        .team-member p {
            margin-top: 10px;
            font-size: 1rem;
            color: #023616;
        }
        .links-container {
            text-align: center;
            margin-top: 30px;
        }
        .links-container a {
            font-size: 1.2rem;
            color: #028436;
            font-weight: bold;
            text-decoration: none;
            margin: 0 15px;
        }
        .links-container a:hover {
            text-decoration: underline;
        }
    </style>

    <div class="about-container">
        <h1 class="about-title">Sobre o Portal Datazônia</h1>
        <p class="about-text">
            O <a href="https://github.com/unb-mds/2024-2-Squad10/" target="_blank">Portal Datazônia</a> é um projeto desenvolvido no âmbito da disciplina 
            <strong>Métodos de Desenvolvimento de Software (2024/2)</strong> na Universidade de Brasília (UnB).<br><br>
            O objetivo do projeto é monitorar dados ambientais relacionados aos estados da Amazônia Legal, 
            fornecendo informações visuais e acessíveis para análise e tomada de decisão.
        </p>
    </div>

    <h2 style="text-align: center; color: #023616;">Equipe</h2>
    <div class="team-container">
        <div class="team-member">
            <a href="https://github.com/fdiogo1" target="_blank">
                <img src="https://avatars.githubusercontent.com/fdiogo1">
                <p>Diogo Ferreira</p>
            </a>
        </div>
        <div class="team-member">
            <a href="https://github.com/GuilhermeOliveira1327" target="_blank">
                <img src="https://avatars.githubusercontent.com/GuilhermeOliveira1327">
                <p>Guilherme Oliveira</p>
            </a>
        </div>
        <div class="team-member">
            <a href="https://github.com/GuilhermeDavila" target="_blank">
                <img src="https://avatars.githubusercontent.com/GuilhermeDavila">
                <p>Guilherme D'Ávila</p>
            </a>
        </div>
        <div class="team-member">
            <a href="https://github.com/bigkaio" target="_blank">
                <img src="https://avatars.githubusercontent.com/bigkaio">
                <p>Kaio Macedo</p>
            </a>
        </div>
        <div class="team-member">
            <a href="https://github.com/renanpariiz" target="_blank">
                <img src="https://avatars.githubusercontent.com/renanpariiz">
                <p>Renan Pariz</p>
            </a>
        </div>
        <div class="team-member">
            <a href="https://github.com/devwallyson" target="_blank">
                <img src="https://avatars.githubusercontent.com/devwallyson">
                <p>Wallyson Souza</p>
            </a>
        </div>
    </div>

    <div class="links-container">
        <p>Você pode encontrar mais informações nos links abaixo:</p>
        <a href="https://unb-mds.github.io/2024-2-Datazonia/" target="_blank">📄 Documentação</a>
        <a href="https://github.com/unb-mds/2024-2-Squad10/" target="_blank">💻 GitHub do Projeto</a>
    </div>
    """,
    unsafe_allow_html=True
)
else:
    st.markdown("<h2 class='section-title'>Amazônia Legal</h2>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: center;'>O mapa abaixo destaca os estados que fazem parte da Amazônia Legal.</h4>", unsafe_allow_html=True)

    # --- Mapa Interativo ---
    def criar_mapa():
        estados_amazonia_legal = [
            "Acre", "Amapá", "Amazonas", "Maranhão",
            "Mato Grosso", "Pará", "Rondônia", "Roraima", "Tocantins"
        ]
        centro_mapa = [-6.4653, -58.2159]
        mapa = folium.Map(location=centro_mapa, zoom_start=4.55, control_scale=True)
        geojson_url = "https://raw.githubusercontent.com/codeforamerica/click_that_hood/master/public/data/brazil-states.geojson"
        response = requests.get(geojson_url)
        geojson = response.json()
        geojson["features"] = [
            feature for feature in geojson["features"]
            if feature["properties"]["name"] in estados_amazonia_legal
        ]
        folium.GeoJson(
            geojson,
            name="Estados da Amazônia Legal",
            style_function=lambda feature: {
                "fillColor": "cyan",
                "color": "black",
                "weight": 2,
                "fillOpacity": 0.5,
            },
            tooltip=folium.GeoJsonTooltip(fields=["name"], aliases=["Estado:"])
        ).add_to(mapa)
        return mapa

    st.markdown('<div class="map-container">', unsafe_allow_html=True)
    st_folium(criar_mapa(), use_container_width=True, height=600)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("<hr>", unsafe_allow_html=True)

    # --- Gráfico: Emissão de CO2 ---
    dadosCO2 = load_data("emissaoCO2.csv")
    st.markdown("<h2 class='section-title'>Emissão de CO2</h2>", unsafe_allow_html=True)
    st.markdown("<h5 style='text-align: center; '>Comparativo entre os índices de emissão de CO2 na Amazônia Legal e no restante do Brasil.</h5>", unsafe_allow_html=True)
    st.plotly_chart(criar_grafico(dadosCO2, "Ano", ["Amazonia Legal", "Resto do Brasil"], "Emissão de CO2", cores=["#0009de", "#87e7f7"]))

    st.markdown("<hr>", unsafe_allow_html=True)

    # --- Gráfico: Foco de Queimadas ---
    dadosFOCO = load_data("foco_queimadas.csv")
    st.markdown("<h2 class='section-title'>Foco de Queimadas</h2>", unsafe_allow_html=True)
    st.markdown("<h5 style='text-align: center; '>Comparativo entre os índices de foco de queimadas na Amazônia Legal e no restante do Brasil.</h5>", unsafe_allow_html=True)
    st.plotly_chart(criar_grafico(dadosFOCO, "Ano", ["Amazonia Legal", "Resto do Brasil"], "Foco de Queimadas", tipo="line", cores=["#ff7300", "#f7e45f"]))

    st.markdown("<hr>", unsafe_allow_html=True)

    # --- Gráfico: Desmatamento Acumulado ---
    dadosDAM = load_data("desmatamento_acumulado.csv")
    st.markdown("<h2 class='section-title'>Desmatamento Acumulado</h2>", unsafe_allow_html=True)
    st.markdown("<h5 style='text-align: center; '>Comparativo entre os índices de desmatamento acumulado na Amazônia Legal e no restante do Brasil.</h5>", unsafe_allow_html=True)
    st.plotly_chart(criar_grafico(dadosDAM, "Ano", ["Amazonia Legal", "Resto do Brasil"], "Desmatamento Acumulado", cores=["#3fd170", "#223f18"]))

    st.markdown("<hr>", unsafe_allow_html=True)

    # --- Seção FRP e Risco de Fogo ---
    st.markdown("<h2 class='section-title'>FRP e Risco de Fogo</h2>", unsafe_allow_html=True)
    st.markdown(
        """
        <p style='text-align: center; '>
            <strong>Fire Radiative Power (FRP):</strong> Mede a energia térmica emitida por um incêndio em megawatts (MW).<br>
            <strong>Risco de Fogo:</strong> Índice que estima a probabilidade de incêndios com base em variáveis ambientais.
        </p>
        """, unsafe_allow_html=True
    )

    # Obtém a lista de municípios
    municipios = def_funcao.get_municipios()
    if municipios:
        municipio_selecionado = st.selectbox("Selecione um município:", sorted(municipios))
        
        # Obtém os dados do município selecionado
        dados_municipio = def_funcao.get_risco_fogo(municipio_selecionado)
        if dados_municipio:
            st.markdown(f"<h3>Dados sobre {municipio_selecionado}</h3>", unsafe_allow_html=True)

            # Cria colunas para exibir os valores de Risco de Fogo e FRP
            col1, col2 = st.columns(2)
            with col1:
                st.markdown(f'<p class="metric-container">Risco de Fogo: {dados_municipio["RiscoFogo"]}</p>', unsafe_allow_html=True)
            with col2:
                st.markdown(f'<p class="metric-container">FRP: {dados_municipio["FRP"]}</p>', unsafe_allow_html=True)

            # Ajuste para evitar erro no gráfico
            df_metrica = pd.DataFrame({
                "Métrica": ["FRP", "Risco de Fogo"],
                "Valor": [dados_municipio["FRP"], dados_municipio["RiscoFogo"]]
            })

            # Cria um gráfico de barras com as cores específicas
            fig_metrica = px.bar(
                df_metrica,
                x="Métrica",
                y="Valor",
                title="FRP e Risco de Fogo",
                text="Valor",
                color="Métrica",
                color_discrete_map={"FRP": "#ba4ce7", "Risco de Fogo": "#fc5c5c"}
            )

            # Melhorias no layout do gráfico
            fig_metrica.update_traces(textposition="outside")
            fig_metrica.update_layout(
                plot_bgcolor="white",
                paper_bgcolor="white",
                font=dict(color="#023616"),
                title=dict(font=dict(color="#023616")),
                xaxis=dict(
                    title=dict(text="Métrica", font=dict(color="#023616")),
                    tickfont=dict(color="#023616")
                ),
                yaxis=dict(
                    title=dict(text="Valor", font=dict(color="#023616")),
                    tickfont=dict(color="#023616")
                ),
                legend=dict(font=dict(color="#023616"))
            )

            # Exibe o gráfico na interface
            st.plotly_chart(fig_metrica, use_container_width=True)

