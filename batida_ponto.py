import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Pega login e senha das variáveis de ambiente
LOGIN = os.getenv("silas.ferreira@quark.tec.br")
SENHA = os.getenv("ohchio8ve#F5")

if not LOGIN or not SENHA:
    raise Exception("As variáveis QUARK_LOGIN e QUARK_SENHA não estão definidas.")

# Configurações do Chrome para rodar no GitHub Actions (headless)
chrome_options = Options()
chrome_options.add_argument("--headless=new")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Inicializa o navegador
driver = webdriver.Chrome(options=chrome_options)

try:
    driver.get("https://rh-colaborador.quark.tec.br/")
    wait = WebDriverWait(driver, 20)

    # Login
    wait.until(EC.element_to_be_clickable((By.ID, "login"))).send_keys(LOGIN)
    driver.find_element(By.ID, "senha").send_keys(SENHA)
    driver.find_element(By.ID, "politica-privacidade").click()
    driver.find_element(By.ID, "logar").click()

    # Clicar no botão "Registrar Ponto"
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn-gradient"))).click()

    # Clicar no botão final
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".container__direito-maquina"))).click()

    # Esperar a mensagem de sucesso
    wait.until(EC.text_to_be_present_in_element(
        (By.TAG_NAME, "body"),
        "Ponto registrado com sucesso!"
    ))

    print("✅ Ponto registrado com sucesso!")

    # Espera 3 segundos para garantir
    time.sleep(3)

finally:
    driver.quit()
