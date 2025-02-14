"""Módulo responsável pelo scraping de dados usando Selenium e Watchdog."""
import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from watchdog.observers import Observer

from dotenv import load_dotenv
import def_funcao
from def_funcao import DownloadHandler  # Importação do próprio projeto
load_dotenv()

EMAIL = os.getenv("EMAIL") # Dados cadastrados no .env, utilizado no site de dados. (AL em Dados)
SENHA = os.getenv("SENHA")
DOWNLOAD_DIR = os.getenv("CAMINHO") # Diretório de download. Coloque o caminho no .env.


def baixar_dados(tabela, url):
    """Acessa a URL, clica no botão de download e monitora o arquivo baixado."""
    def_funcao.definir_tabela(tabela)
    driver.get(url)
    time.sleep(5)

    elemento_hover = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, '//*[@id="tab-eg7-0"]/div[1]/div/ul/li/img'))
    )

    action = ActionChains(driver)
    action.move_to_element(elemento_hover).perform()

    botao_csv = driver.find_element(
        By.XPATH, '//a[contains(@class, "amcharts-amexport-item-csv")]')

    # Inicia o Watchdog para monitorar esse download
    observer = Observer()
    event_handler = DownloadHandler(observer)
    observer.schedule(event_handler, path=DOWNLOAD_DIR, recursive=False)
    observer.start()

    botao_csv.click()

    time.sleep(5)  # Aguarda o download terminar

    observer.stop()
    observer.join()


driver = webdriver.Chrome()

driver.get("https://amazonialegalemdados.info/home/home.php?width=1920&height=1080")
time.sleep(5)
# login
driver.find_element(By.XPATH, "/html/body/div[1]/nav/div/div[2]/div/p").click()
driver.find_element(
    By.XPATH,
    "/html/body/div[11]/div/section[1]/section/input[1]").click()
driver.find_element(
    By.XPATH,
    "/html/body/div[11]/div/section[1]/section/input[1]").send_keys(EMAIL)
driver.find_element(
    By.XPATH,
    "/html/body/div[11]/div/section[1]/section/input[2]").send_keys(SENHA)
driver.find_element(
    By.XPATH,
    "/html/body/div[11]/div/section[1]/section/input[2]").click()
driver.find_element(
    By.XPATH,
    "/html/body/div[11]/div/section[2]/div[2]").click()
time.sleep(5)

# CO2
baixar_dados("co2","https://amazonialegalemdados.info/dashboard/perfil.php"
             "?regiao=Amazônia%20Legal&area=Meio%20Ambiente__34&indicador=TX_SEEG_"
             "CO2_PER_CAPITA_UF__34&primeiro"
            )

# Queimadas
baixar_dados(
    "foco",
    "https://amazonialegalemdados.info/dashboard/perfil.php"
    "?regiao=Amazônia%20Legal&area=Meio%20Ambiente__34&indicador=TX_INPE_FOCOS_QUEIMADA_UF__34")

# Desmatamento(DAM)
baixar_dados(
    "dam",
    "https://amazonialegalemdados.info/dashboard/perfil.php"
    "?regiao=Amazônia%20Legal&area=Meio%20Ambiente__34&indicador=TX_INPE_DESMATAMENTO_UF__34")

driver.quit()
