from concurrent.futures import ThreadPoolExecutor
from unidecode import unidecode
from selenium.webdriver.support.ui import Select
import threading
import subprocess
import os
import time
from tqdm import tqdm
import shutil
import json
from tqdm import tqdm
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
from selenium.common.exceptions import *
import re
import sys
import numpy as np
import cv2
import requests

service = Service()
options = webdriver.ChromeOptions()
titulo_arquivo = ""
# options.add_argument("--headless=new")

options.add_argument("--disable-gpu")
options.add_argument("--disable-extensions")
prefs = {"profile.managed_default_content_settings.images": 2}
options.add_experimental_option("prefs", prefs)


def limpar_pasta(caminho_pasta):
    # Verifica se o caminho é um diretório
    if not os.path.isdir(caminho_pasta):
        print(f'O caminho "{caminho_pasta}" não é um diretório válido.')
        return
    
    try:
        # Percorre todos os arquivos na pasta
        for nome_arquivo in os.listdir(caminho_pasta):
            caminho_completo = os.path.join(caminho_pasta, nome_arquivo)
            # Verifica se é um arquivo (não um diretório)
            if os.path.isfile(caminho_completo):
                # Remove o arquivo
                os.remove(caminho_completo)
                print(f'Arquivo "{nome_arquivo}" removido com sucesso.')
            else:
                print(f'O item "{nome_arquivo}" não é um arquivo.')

        print(f'Todos os arquivos em "{caminho_pasta}" foram removidos.')
    except Exception as e:
        print(f'Ocorreu um erro ao tentar limpar a pasta: {e}')

def excluir_arquivo(caminho_arquivo):
    # Verifica se o arquivo existe
    if os.path.exists(caminho_arquivo):
        try:
            # Remove o arquivo
            os.remove(caminho_arquivo)
            print(f'Arquivo "{caminho_arquivo}" removido com sucesso.')
        except Exception as e:
            print(f'Ocorreu um erro ao tentar excluir o arquivo: {e}')
    else:
        print(f'O arquivo "{caminho_arquivo}" não existe.')
        
excluir_arquivo("planilha_final.xlsx")        
limpar_pasta("dados")

def download_image_from_url(url, path):
    response = requests.get(url)
    img = cv2.imdecode(np.frombuffer(response.content, np.uint8), cv2.IMREAD_COLOR)
    if img is not None:
        cv2.imwrite(path, img)
        return path
    else:
        return None



driver = webdriver.Chrome(service=service, options=options)
try:
    driver.get("https://corp.shoppingdeprecos.com.br/login")
    counter = 0
    while True:
        test = driver.find_elements(By.XPATH, '//*[@id="email"]')
        if test:
            break
        else:
            counter += 1
            if counter > 20:
                break;
            time.sleep(0.5)
    driver.find_element(By.XPATH, '//*[@id="email"]').send_keys("loja@jfaeletronicos.com")
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys("922982PC")
    driver.find_element(By.XPATH, '//*[@id="btnLogin"]').click()
    print("Fez login")
except TimeoutException as e:
    print(f"Timeout ao tentar carregar a página ou encontrar um elemento: {e}")
except NoSuchElementException as e:
    print(f"Elemento não encontrado na página: {e}")
except WebDriverException as e:
    print(f"Erro no WebDriver: {e}")

time.sleep(3)
driver.get("https://corp.shoppingdeprecos.com.br/vendedores/busca")


driver.find_element(By.XPATH, '//*[@id="txtTermo"]').send_keys("jfa")
time.sleep(1)
driver.execute_script("tabela(0);")
time.sleep(8)

commands = []
urls = []

for i in driver.find_elements(By.XPATH ,'//*[@id="table_result"]/tbody/tr'):
    url = i.find_element(By.XPATH, ".//td[3]/a")
    url = url.get_attribute("href")
    loja = i.find_element(By.XPATH, './/td[2]/a')
    commands.append([url, loja.text])



driver.quit()

def run_command(cmd):
    subprocess.run(["python", "rodar.py", cmd[0], cmd[1] ])

if __name__ == '__main__':
    with ThreadPoolExecutor(max_workers=10) as executor: 
        list(tqdm(executor.map(run_command, commands), total=len(commands)))
        
        
subprocess.run(["python", "ordernar.py"])
