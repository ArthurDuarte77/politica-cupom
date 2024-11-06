import requests
import subprocess
from concurrent.futures import ThreadPoolExecutor
import time
import json
from tqdm import tqdm
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *

service = Service()
options = webdriver.ChromeOptions()
titulo_arquivo = ""
# options.add_argument("--headless=new")

options.add_argument("--disable-gpu")
options.add_argument("--disable-extensions")
prefs = {"profile.managed_default_content_settings.images": 2}
options.add_experimental_option("prefs", prefs)


driver = webdriver.Chrome(service=service, options=options)



def load_cookies(driver, cookies_file):
    with open(cookies_file, 'r') as file:
        cookies = json.load(file)
    
    # Primeiro, navegue para o domínio para o qual os cookies são válidos
    driver.get("https://www.mercadolivre.com.br")
    
    for cookie in cookies:
        # Alguns browsers só aceitam certos campos do cookie
        cookie_dict = {
            'name': cookie['name'],
            'value': cookie['value'],
            'domain': cookie['domain'],
            'path': cookie['path'],
        }
        # Adicione campos opcionais se estiverem presentes
        if 'expiry' in cookie:
            cookie_dict['expiry'] = int(cookie['expirationDate'])
        if 'secure' in cookie:
            cookie_dict['secure'] = cookie['secure']
        if 'httpOnly' in cookie:
            cookie_dict['httpOnly'] = cookie['httpOnly']

        driver.add_cookie(cookie_dict)

urls = []

def cupom(driver, count=1):
    driver.get(f"https://www.mercadolivre.com.br/cupons/filter?category=acc_vertical&page={count}")
    
    counter = 0
    while True:
        test = driver.find_elements(By.XPATH, '//div/div/div[2]/div/div[1]/div[2]/div[2]/div[2]/span[1]')
        if test:
            break
        else:
            counter += 1
            if counter > 20:
                break
            time.sleep(0.5)
    time.sleep(1)

    # Encontrar todos os botões
    botoes = driver.find_elements(By.XPATH, '//button[@class="andes-button andes-button--small andes-button--quiet"]')
    indices = range(len(botoes)) 
    script = '''
        var botoes = document.evaluate(
            '//*[@class="andes-button andes-button--small andes-button--loud"]',
            document,
            null,
            XPathResult.UNORDERED_NODE_SNAPSHOT_TYPE,
            null
        );

        for (var i = 0; i < botoes.snapshotLength; i++) {
            (function(index) {
                    var botao = botoes.snapshotItem(index);
                    botao.click();
                    console.log('Clicou no botão:', botao);
            })(i);
        }
    '''
    driver.execute_script(script)
    try:
        for index in indices:
            print(index + 1)
            if driver.find_element(By.XPATH, f'//*[@id="filtercoupons"]/div/div[2]/div/div[{index + 1}]/div[2]/div[2]/div[2]/span[1]').text == "Em produtos selecionados":
                continue
            # Armazenar a URL atual
            current_url = driver.current_url
            botao = driver.find_element(By.XPATH, f'//div[{index + 1}]/div[4]/button[@class="andes-button andes-button--small andes-button--quiet"]')
            # Clicar no botão
            botao.click()
            time.sleep(2)  # Esperar a nova página carregar

            # Capturar a URL da nova página
            new_url = driver.current_url
            urls.append(new_url)

            driver.back()
            time.sleep(2)  # Esperar a página anterior carregar

            # Garantir que voltamos para a página correta
            if driver.current_url != current_url:
                driver.get(current_url)
                time.sleep(2)
    except:
        return

    count += 1
    try:
        if driver.find_element(By.XPATH, '/html/body/main/div/div/div[@class="empty-state-container"]'):
            return
    except:
        cupom(driver, count)

try:
    load_cookies(driver, 'cookies.json')
    cupom(driver)
finally:
    driver.quit()

def run_command(cmd):
    subprocess.run(["python", "rodar.py", cmd])


if __name__ == '__main__':
    with ThreadPoolExecutor(max_workers=10) as executor:
        list(tqdm(executor.map(run_command, urls), total=len(urls)))
        