from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import os
from dotenv import load_dotenv

load_dotenv()

EMAIL = os.getenv("EMAIL")
SENHA = os.getenv("SENHA")

driver = webdriver.Chrome()

driver.get("https://amazonialegalemdados.info/home/home.php?width=1920&height=1080")
time.sleep(5)
#login
driver.find_element(By.XPATH, "/html/body/div[1]/nav/div/div[2]/div/p").click()
driver.find_element(By.XPATH, "/html/body/div[11]/div/section[1]/section/input[1]").click()
driver.find_element(By.XPATH, "/html/body/div[11]/div/section[1]/section/input[1]").send_keys(EMAIL)
driver.find_element(By.XPATH, "/html/body/div[11]/div/section[1]/section/input[2]").send_keys(SENHA)
driver.find_element(By.XPATH, "/html/body/div[11]/div/section[1]/section/input[2]").click()
driver.find_element(By.XPATH, "/html/body/div[11]/div/section[2]/div[2]").click()
time.sleep(1)

#co2
driver.get("https://amazonialegalemdados.info/dashboard/perfil.php?regiao=Amazônia%20Legal&area=Meio%20Ambiente__34&indicador=TX_SEEG_CO2_PER_CAPITA_UF__34&primeiro")
time.sleep(5)

elemento_hover = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="tab-eg7-0"]/div[1]/div/ul/li/img'))
)

action = ActionChains(driver)
action.move_to_element(elemento_hover).perform()

botao_csv = driver.find_element(By.XPATH, '//a[contains(@class, "amcharts-amexport-item-csv")]')
botao_csv.click()
time.sleep(5)
#foco queimadas
driver.get("https://amazonialegalemdados.info/dashboard/perfil.php?regiao=Amazônia%20Legal&area=Meio%20Ambiente__34&indicador=TX_INPE_FOCOS_QUEIMADA_UF__34")
time.sleep(5)

elemento_hover = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="tab-eg7-0"]/div[1]/div/ul/li/img'))
)

action = ActionChains(driver)
action.move_to_element(elemento_hover).perform()

botao_csv = driver.find_element(By.XPATH, '//a[contains(@class, "amcharts-amexport-item-csv")]')
botao_csv.click()
time.sleep(5)
#Dam
driver.get("https://amazonialegalemdados.info/dashboard/perfil.php?regiao=Amazônia%20Legal&area=Meio%20Ambiente__34&indicador=TX_INPE_DESMATAMENTO_UF__34")
time.sleep(5)

elemento_hover = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="tab-eg7-0"]/div[1]/div/ul/li/img'))
)

action = ActionChains(driver)
action.move_to_element(elemento_hover).perform()

botao_csv = driver.find_element(By.XPATH, '//a[contains(@class, "amcharts-amexport-item-csv")]')
botao_csv.click()
time.sleep(5)


driver.quit()
