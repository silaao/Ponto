from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

# Configuração do Chrome em modo headless
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Inicia o driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# Acessa o site
driver.get("https://rh-colaborador.quark.tec.br/")

# Login e senha fixos (por enquanto)
login = "silas.ferreira@quark.tec.br"
senha = "ohchio8ve#F5"

driver.find_element("id", "login").send_keys(login)
driver.find_element("id", "senha").send_keys(senha)
driver.find_element("id", "politica-privacidade").click()

driver.find_element("id", "login-button").click()

time.sleep(3)
driver.quit()
