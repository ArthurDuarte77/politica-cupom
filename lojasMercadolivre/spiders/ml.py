import zipfile
import os
from openpyxl.utils.exceptions import InvalidFileException
from unidecode import unidecode
import scrapy
import pandas
from datetime import datetime


data_atual = datetime.now()

# Formata a data no formato dia/mês/ano
data_formatada = data_atual.strftime("%d/%m/%Y")
start_row = 20  
end_row = 37
num_rows = end_row - start_row

df = pandas.read_excel("GESTÃO DE AÇÕES E-COMMERCE.xlsx", usecols='C:K', skiprows=start_row, nrows=num_rows, engine='openpyxl')

df.columns = ['PRODUTO', 'SITE', 'COLUNA3', 'CLÁSSICO ML', 'COLUNA5', 'PREMIUM ML', 'COLUNA7', 'MARKETPLACES', 'COLUNA9']


for index, i in df.iterrows():
    if i['PRODUTO'] == "FONTE 40A":
        fonte40Marketplace = round(i['COLUNA3'], 2);
        fonte40Classico = round(i['COLUNA5'], 2);
        fonte40Premium = round(i['COLUNA7'], 2);
    elif i['PRODUTO'] == "FONTE 60A":
        fonte60Marketplace = round(i['COLUNA3'], 2);
        fonte60Classico = round(i['COLUNA5'], 2);
        fonte60Premium = round(i['COLUNA7'], 2);
    elif i['PRODUTO'] == "FONTE 60A LITE":
        fonte60liteMarketplace = round(i['COLUNA3'], 2);
        fonte60liteClassico = round(i['COLUNA5'], 2);
        fonte60litePremium = round(i['COLUNA7'], 2);
    elif i['PRODUTO'] == "FONTE 70A":
        fonte70Marketplace = round(i['COLUNA3'], 2);
        fonte70Classico = round(i['COLUNA5'], 2);
        fonte70Premium = round(i['COLUNA7'], 2);
    elif i['PRODUTO'] == "FONTE 70A LITE":
        fonte70liteMarketplace = round(i['COLUNA3'], 2);
        fonte70liteClassico = round(i['COLUNA5'], 2);
        fonte70litePremium = round(i['COLUNA7'], 2);
    elif i['PRODUTO'] == "FONTE 90 BOB":
        fonte90bobMarketplace = round(i['COLUNA3'], 2);
        fonte90bobClassico = round(i['COLUNA5'], 2);
        fonte90bobPremium = round(i['COLUNA7'], 2);
    elif i['PRODUTO'] == "FONTE 120 BOB":
        fonte120bobMarketplace = round(i['COLUNA3'], 2);
        fonte120bobClassico = round(i['COLUNA5'], 2);
        fonte120bobPremium = round(i['COLUNA7'], 2);
    elif i['PRODUTO'] == "FONTE 120A LITE":
        fonte120liteMarketplace = round(i['COLUNA3'], 2);
        fonte120liteClassico = round(i['COLUNA5'], 2);
        fonte120litePremium = round(i['COLUNA7'], 2);
    elif i['PRODUTO'] == "FONTE 120A":
        fonte120Marketplace = round(i['COLUNA3'], 2);
        fonte120Classico = round(i['COLUNA5'], 2);
        fonte120Premium = round(i['COLUNA7'], 2);
    elif i['PRODUTO'] == "FONTE 200 BOB":
        fonte200bobMarketplace = round(i['COLUNA3'], 2);
        fonte200bobClassico = round(i['COLUNA5'], 2);
        fonte200bobPremium = round(i['COLUNA7'], 2);
    elif i['PRODUTO'] == "FONTE 200A LITE":
        fonte200liteMarketplace = round(i['COLUNA3'], 2);
        fonte200liteClassico = round(i['COLUNA5'], 2);
        fonte200litePremium = round(i['COLUNA7'], 2);
    elif i['PRODUTO'] == "FONTE 200 MONO":
        fonte200monoMarketplace = round(i['COLUNA3'], 2);
        fonte200monoClassico = round(i['COLUNA5'], 2);
        fonte200monoPremium = round(i['COLUNA7'], 2);
    elif i['PRODUTO'] == "FONTE 200A":
        fonte200Marketplace = round(i['COLUNA3'], 2);
        fonte200Classico = round(i['COLUNA5'], 2);
        fonte200Premium = round(i['COLUNA7'], 2);
    elif i['PRODUTO'] == "K1200":
        k1200Marketplace = round(i['COLUNA3'], 2);
        k1200Classico = round(i['COLUNA5'], 2);
        k1200Premium = round(i['COLUNA7'], 2);
    elif i['PRODUTO'] == "K600":
        k600Marketplace = round(i['COLUNA3'], 2);
        k600Classico = round(i['COLUNA5'], 2);
        k600Premium = round(i['COLUNA7'], 2);
    elif i['PRODUTO'] == "CONTROLE WR":
        controleWrMarketplace = round(i['COLUNA3'], 2);
        controleWrClassico = round(i['COLUNA5'], 2);
        controleWrPremium = round(i['COLUNA7'], 2);
    elif i['PRODUTO'] == "ACQUA":
        acquaMarketplace = round(i['COLUNA3'], 2);
        acquaClassico = round(i['COLUNA5'], 2);
        acquaPremium = round(i['COLUNA7'], 2);

def identificar_modelo(nome, preco, categoria):
    new_name = unidecode(nome.lower())
    modelo_escolhido = ""
    if "bob" not in new_name and "lite" not in new_name and "light" not in new_name  and "controle" not in new_name and 'jfa' in new_name:
        if "40a" in new_name or "40" in new_name or "40 amperes" in new_name or "40amperes" in new_name or "36a" in new_name or "36" in new_name or "36 amperes" in new_name or "36amperes" in new_name:
            modelo_escolhido = "FONTE 40A STORM"
    if "bob" not in new_name and "lite" not in new_name and "light" not in new_name  and "controle" not in new_name and 'jfa' in new_name:
        if "60a" in new_name or "60" in new_name or "60 amperes" in new_name or "60amperes" in new_name or "60 a" in new_name:
            modelo_escolhido = "FONTE 60A STORM"
    if "bob" not in new_name and ("lite" in new_name or "light" in new_name) and "controle" not in new_name and 'jfa' in new_name:
        if "60a" in new_name or "60" in new_name or "60 amperes" in new_name or "60amperes" in new_name or "60 a" in new_name:
            modelo_escolhido = "FONTE 60A LITE"
    if "bob" not in new_name and "lite" not in new_name and "light" not in new_name  and "controle" not in new_name and 'jfa' in new_name:
        if "70a" in new_name or "70" in new_name or "70 amperes" in new_name or "70amperes" in new_name or "70 a" in new_name:
            modelo_escolhido = "FONTE 70A STORM"
    if "bob" not in new_name and  ("lite" in new_name or "light" in new_name) and "controle" not in new_name and 'jfa' in new_name:
        if "70a" in new_name or "70" in new_name or "70 amperes" in new_name or "70amperes" in new_name or "70 a" in new_name:
            modelo_escolhido = "FONTE 70A LITE"
    if "bob" in new_name and "lite" not in new_name and "light" not in new_name  and "controle" not in new_name and 'jfa' in new_name:
        if "90a" in new_name or "90" in new_name or "90 amperes" in new_name or "90amperes" in new_name or "90 a" in new_name:
            modelo_escolhido = "FONTE 90 BOB"
    if "bob" not in new_name and "lite" not in new_name and "light" not in new_name  and "controle" not in new_name and 'jfa' in new_name:
        if "120a" in new_name or "120" in new_name or "120 amperes" in new_name or "120amperes" in new_name or "120 a" in new_name:
            modelo_escolhido = "FONTE 120A STORM"
    if "bob" not in new_name and  ("lite" in new_name or "light" in new_name) and "controle" not in new_name and 'jfa' in new_name:
        if "120a" in new_name or "120" in new_name or "120 amperes" in new_name or "120amperes" in new_name or "120 a" in new_name:
            modelo_escolhido = "FONTE 120A LITE"
    if "bob" in new_name and "lite" not in new_name and "light" not in new_name  and "controle" not in new_name and 'jfa' in new_name:
        if "120a" in new_name or "120" in new_name or "120 amperes" in new_name or "120amperes" in new_name or "120 a" in new_name:
            modelo_escolhido = "FONTE 120 BOB"
    if "bob" not in new_name and "lite" not in new_name and "light" not in new_name  and "controle" not in new_name and 'jfa' in new_name and 'mono' not in new_name and 'mono' not in new_name and 'monovolt' not in new_name and '220v' not in new_name:
        if "200a" in new_name or "200" in new_name or "200 amperes" in new_name or "200amperes" in new_name or "200 a" in new_name:
            modelo_escolhido = "FONTE 200A STORM"
    if "bob" not in new_name and "lite" not in new_name and "light" not in new_name  and "controle" not in new_name and 'jfa' in new_name and ("mono" in new_name or "220v" in new_name or "monovolt" in new_name):
        if "200a" in new_name or "200" in new_name or "200 amperes" in new_name or "200amperes" in new_name or "200 a" in new_name:        
            modelo_escolhido = "FONTE 200 MONO"
    if "bob" not in new_name and  ("lite" in new_name or "light" in new_name) and "controle" not in new_name and 'jfa' in new_name and 'mono' not in new_name and 'monovolt' not in new_name and '220v' not in new_name:
        if "200a" in new_name or "200" in new_name or "200 amperes" in new_name or "200amperes" in new_name or "200 a" in new_name:
            modelo_escolhido = "FONTE 200A LITE"
    if "bob" in new_name and "lite" not in new_name and "light" not in new_name  and "controle" not in new_name and 'jfa' in new_name and 'mono' not in new_name and 'mono' not in new_name and 'monovolt' not in new_name and '220v' not in new_name:
        if "200a" in new_name or "200" in new_name or "200 amperes" in new_name or "200amperes" in new_name or "200 a" in new_name:
            modelo_escolhido = "FONTE 200 BOB"
    if "k600" in new_name and "controle" in new_name and "jfa" in new_name and "fonte" not in new_name and "k1200" not in new_name:
        modelo_escolhido = "K600"
    if "k1200" in new_name and "controle" in new_name and "jfa" in new_name and "fonte" not in new_name and "k600" not in new_name:
        modelo_escolhido = "K1200"
    if ("controle wr" in new_name or "wr" in new_name) and "controle" in new_name and "jfa" in new_name and "fonte" not in new_name:
        modelo_escolhido = "CONTROLE WR"
    if "acqua" in new_name and "controle" in new_name and "jfa" in new_name and "fonte" not in new_name:
        modelo_escolhido = "ACQUA"
    
            
    modelos = {
        "FONTE 40A STORM": {"classico": (352.97, 423.99), "premium": (402.79, 455.79)},
        "FONTE 60A STORM": {"classico": (391.13, 466.39), "premium": (443.07, 498.19)},
        "FONTE 60A LITE": {"classico": (321.09, 384.16), "premium": (364.95, 410.97)},
        "FONTE 70A STORM": {"classico": (438.83, 519.39), "premium": (493.42, 551.19)},
        "FONTE 70A LITE": {"classico": (362.36, 430.25), "premium": (408.73, 457.29)},
        "FONTE 120A STORM": {"classico": (572.39, 667.79), "premium": (634.40, 710.19)},
        "FONTE 120A LITE": {"classico": (484.94, 564.48), "premium": (536.26, 603.54)},
        "FONTE 200A STORM": {"classico": (734.57, 847.99), "premium": (805.59, 890.39)},
        "FONTE 200A LITE": {"classico": (624.50, 717.72), "premium": (681.83, 754.44)},
        "FONTE 90 BOB": {"classico": (372.05, 445.19), "premium": (422.93, 466.39)},
        "FONTE 120 BOB": {"classico": (444.55, 525.75), "premium": (499.46, 568.15)},
        "FONTE 200 BOB": {"classico": (562.85, 657.19), "premium": (624.33, 731.39)},
        "FONTE 200 MONO": {"classico": (602.61, 775.38), "premium": (736.61, 815.66)},
        "K600": {"classico": (602.61, 775.38), "premium": (736.61, 815.66)},
        "K1200": {"classico": (602.61, 775.38), "premium": (736.61, 815.66)},
        "CONTROLE WR": {"classico": (602.61, 775.38), "premium": (736.61, 815.66)},
        "ACQUA": {"classico": (602.61, 775.38), "premium": (736.61, 815.66)},
    }
    
    if categoria not in ["classico", "premium"]:
        return "Categoria inválida"
    
    for modelo, categorias in modelos.items():           
        if modelo == modelo_escolhido:
            # min_preco, max_preco = categorias[categoria]
            # if min_preco <= preco <= max_preco:
            #     return modelo
            # else:
            return modelo
    return "Sem Modelo"

def verificar_politica(modelo, preco, tipo):
    if tipo == "classico" and preco:
        if modelo == "FONTE 40A STORM":
            if preco > fonte40Classico:
                return "Acima";
            elif preco < fonte40Classico:
                return "Baixo";
            return "Igual";
        elif modelo == "FONTE 60A LITE":
            if preco > fonte60liteClassico:
                return "Acima";
            elif preco < fonte60liteClassico:
                return "Baixo";
            return "Igual";
        elif modelo == "FONTE 60A STORM":
            if preco > fonte60Classico:
                return "Acima";
            elif preco < fonte60Classico:
                return "Baixo";
            return "Igual";
        elif modelo == "FONTE 70A LITE":
            if preco > fonte70liteClassico:
                return "Acima";
            elif preco < fonte70liteClassico:
                return "Baixo";
            return "Igual";
        elif modelo == "FONTE 70A STORM":
            if preco > fonte70Classico:
                return "Acima";
            elif preco < fonte70Classico:
                return "Baixo";
            return "Igual";
        elif modelo == "FONTE 90 BOB":
            if preco > fonte90bobClassico:
                return "Acima";
            elif preco < fonte90bobClassico:
                return "Baixo";
            return "Igual";
        elif modelo == "FONTE 120 BOB":
            if preco > fonte120bobClassico:
                return "Acima";
            elif preco < fonte120bobClassico:
                return "Baixo";
            return "Igual";
        elif modelo == "FONTE 120A LITE":
            if preco > fonte120liteClassico:
                return "Acima";
            elif preco < fonte120liteClassico:
                return "Baixo";
            return "Igual";
        elif modelo == "FONTE 120A STORM":
            if preco > fonte120Classico:
                return "Acima";
            elif preco < fonte120Classico:
                return "Baixo";
            return "Igual";
        elif modelo == "FONTE 200 BOB":
            if preco > fonte200bobClassico:
                return "Acima";
            elif preco < fonte200bobClassico:
                return "Baixo";
            return "Igual";
        elif modelo == "FONTE 200A LITE":
            if preco > fonte200liteClassico:
                return "Acima";
            elif preco < fonte200liteClassico:
                return "Baixo";
            return "Igual";
        elif modelo == "FONTE 200 MONO":
            if preco > fonte200monoClassico:
                return "Acima";
            elif preco < fonte200monoClassico:
                return "Baixo";
            return "Igual";
        elif modelo == "FONTE 200A STORM":
            if preco > fonte200Classico:
                return "Acima";
            elif preco < fonte200Classico:
                return "Baixo";
            return "Igual";
        elif modelo == "K600":
            if preco > k600Classico:
                return "Acima";
            elif preco < k600Classico:
                return "Baixo";
            return "Igual";
        elif modelo == "K1200":
            if preco > k1200Classico:
                return "Acima";
            elif preco < k1200Classico:
                return "Baixo";
            return "Igual";
        elif modelo == "CONTROLE WR":
            if preco > controleWrClassico:
                return "Acima";
            elif preco < controleWrClassico:
                return "Baixo";
            return "Igual";
        elif modelo == "ACQUA":
            if preco > acquaClassico:
                return "Acima";
            elif preco < acquaClassico:
                return "Baixo";
            return "Igual";
    elif tipo == "premium" and preco:
        if modelo == "FONTE 40A STORM":
            if preco > fonte40Premium:
                return "Acima";
            elif preco < fonte40Premium:
                return "Baixo";
            return "Igual";
        elif modelo == "FONTE 60A LITE":
            if preco > fonte60litePremium:
                return "Acima";
            elif preco < fonte60litePremium:
                return "Baixo";
            return "Igual";
        elif modelo == "FONTE 60A STORM":
            if preco > fonte60Premium:
                return "Acima";
            elif preco < fonte60Premium:
                return "Baixo";
            return "Igual";
        elif modelo == "FONTE 70A LITE":
            if preco > fonte70litePremium:
                return "Acima";
            elif preco < fonte70litePremium:
                return "Baixo";
            return "Igual";
        elif modelo == "FONTE 70A STORM":
            if preco > fonte70Premium:
                return "Acima";
            elif preco < fonte70Premium:
                return "Baixo";
            return "Igual";
        elif modelo == "FONTE 90 BOB":
            if preco > fonte90bobPremium:
                return "Acima";
            elif preco < fonte90bobPremium:
                return "Baixo";
            return "Igual";
        elif modelo == "FONTE 120 BOB":
            if preco > fonte120bobPremium:
                return "Acima";
            elif preco < fonte120bobPremium:
                return "Baixo";
            return "Igual";
        elif modelo == "FONTE 120A LITE":
            if preco > fonte120litePremium:
                return "Acima";
            elif preco < fonte120litePremium:
                return "Baixo";
            return "Igual";
        elif modelo == "FONTE 120A STORM":
            if preco > fonte120Premium:
                return "Acima";
            elif preco < fonte120Premium:
                return "Baixo";
            return "Igual";
        elif modelo == "FONTE 200 BOB":
            if preco > fonte200bobPremium:
                return "Acima";
            elif preco < fonte200bobPremium:
                return "Baixo";
            return "Igual";
        elif modelo == "FONTE 200A LITE":
            if preco > fonte200litePremium:
                return "Acima";
            elif preco < fonte200litePremium:
                return "Baixo";
            return "Igual";
        elif modelo == "FONTE 200 MONO":
            if preco > fonte200monoPremium:
                return "Acima";
            elif preco < fonte200monoPremium:
                return "Baixo";
            return "Igual";
        elif modelo == "FONTE 200A STORM":
            if preco > fonte200Premium:
                return "Acima";
            elif preco < fonte200Premium:
                return "Baixo";
            return "Igual";
        elif modelo == "K600":
            if preco > k600Premium:
                return "Acima";
            elif preco < k600Premium:
                return "Baixo";
            return "Igual";
        elif modelo == "K1200":
            if preco > k1200Premium:
                return "Acima";
            elif preco < k1200Premium:
                return "Baixo";
            return "Igual";
        elif modelo == "CONTROLE WR":
            if preco > controleWrPremium:
                return "Acima";
            elif preco < controleWrPremium:
                return "Baixo";
            return "Igual";
        elif modelo == "ACQUA":
            if preco > acquaPremium:
                return "Acima";
            elif preco < acquaPremium:
                return "Baixo";
            return "Igual";

    return ""


class MlSpider(scrapy.Spider):
    name = "ml"
    allowed_domains = ["mercadolivre.com.br"]
    start_urls = ["https://lista.mercadolivre.com.br/fonte-60a-jfa#D[A:fonte%2060a%20jfa]"]
    items = []
    loja = ""
    last_part = ""
    contagem = 0
    is_full = ""
    fullis = ""

    def __init__(self, palavra=None, loja=None, *args, **kwargs):
        super(MlSpider, self).__init__(*args, **kwargs)
        self.palavra = palavra
        self.loja = loja
        
    def parse(self, response, **kwargs):
        yield scrapy.Request(url=self.palavra, callback=self.parse_img)

    def parse_produto(self, response, nome, preco, link, is_classico):
        full = response.xpath('.//div[@class="ui-pdp-media ui-pdp-promotions-pill-label__icon"]')        
        if full:
            is_full = "FULL"
        else:
            is_full = "NA"
        modelo = identificar_modelo(nome, preco, is_classico)
        politica = verificar_politica(modelo, preco, is_classico)
        self.items.append({
            "data": data_formatada,
            "loja": self.last_part,
            "nome": nome,
            "modelo": modelo,
            "preco": preco,
            "politica": politica,
            "full": is_full,
            "tipo": is_classico,
            "link": link,
        })
    
    def parse_img(self, response):
        self.last_part = self.loja
        self.last_part = unidecode(self.last_part.lower())
        self.contagem += 1
        for i in response.xpath('//*[@id="root-app"]/div/div[4]/section/ol/li'):
            nome = i.xpath('.//div/div/div[2]/div/div[1]/a/@title').get()
            sem_juros = i.xpath('.//div[2]/div/div[2]/span/text()').getall()
            if nome and "jfa" not in nome.lower():
                continue
            preco = i.xpath('.//div[2]/div/div[2]/div/div/div/span[1]/span[2]/text()').get()
            centavos = i.xpath('.//div[2]/div/div[2]/div/div/div/span[1]/span[4]/text()').get()
            link = i.xpath('.//div/div/div[2]/div/div[1]/a/@href').get()
            full = i.xpath('.//p[@class="fulfillment ui-pb-label-builder fulfillment fulfillment"]').get()
            image = i.xpath('.//div/div/div[1]/img/@data-src').get()
            if not link:
                continue
            if preco:
                if not centavos:
                    centavos = "0";
                preco = float(preco.replace(".", "") + "." + centavos)
                
        
            for item in sem_juros:
                if "sem juros" in item:
                    is_classico = "premium"
                    break
                else: 
                    is_classico = "classico"
            # if full:
            #     is_full = "FULL"
            # else:
            #     full = i.xpath('.//div/div/div[2]/div/div[5]/div/p').get()
            #     if full:
            #         is_full = "FULL"
            #     is_full = "NA"

            if not nome:
                nome = i.xpath('.//div/div/div[2]/div/div[2]/a/@title').get()
            yield scrapy.Request(url=link, callback=self.parse_produto, cb_kwargs={"nome": nome, "preco": preco, "link": link, "is_classico": is_classico})
        
        if len(self.items) == 0:
            
            for i in response.xpath('//*[@id="root-app"]/div/div[3]/section/ol/li'):
                nome = i.xpath('.//div/div/div[2]/div[1]/a/@title').get()
                link = i.xpath('.//div/div/div[2]/div[1]/a/@href').get()
                if nome and "jfa" not in nome.lower():
                    continue
                preco = i.xpath('.//span[@class = "andes-money-amount ui-search-price__part ui-search-price__part--medium andes-money-amount--cents-superscript"]/span[@class = "andes-money-amount__fraction"][1]/text()').get()
                centavos = i.xpath('.//span[@class = "andes-money-amount ui-search-price__part ui-search-price__part--medium andes-money-amount--cents-superscript"]/span[@class = "andes-money-amount__cents andes-money-amount__cents--superscript-24"][1]/text()').get()
                full = i.xpath('.//div/div/div[2]/div[2]/div[1]/div[3]/div/p').get()
                
                sem_juros = i.xpath('.//div/div/div[2]/div[2]/div[1]/div[1]/span/text()').getall()
                if not link:
                    continue
                if preco:
                    if not centavos:
                        centavos = "0";
                    preco = float(preco.replace(".", "") + "." + centavos)
                    
                
                for item in sem_juros:
                    if "sem juros" in item:
                        is_classico = "premium"
                        break
                    else: 
                        is_classico = "classico"
                # if full:
                #     is_full = "FULL"
                # else:
                #     full = i.xpath('.//div/div/div[2]/div/div[5]/div/p').get()
                #     if full:
                #         is_full = "FULL"
                #     is_full = "NA"

                if not nome:
                    nome = i.xpath('.//div/div/div[2]/div/div[2]/a/@title').get()
                    
                yield scrapy.Request(url=link, callback=self.parse_produto, cb_kwargs={"nome": nome, "preco": preco, "link": link, "is_classico": is_classico})
                
                
        next_page = response.xpath('//li[@class = "andes-pagination__button andes-pagination__button--next"]/a[@class = "andes-pagination__link"]/@href').get()
        if next_page:
            yield scrapy.Request(url=next_page, callback=self.parse_img)

    def closed(self, reason):       
        self.last_part = self.loja
        self.last_part = unidecode(self.last_part.lower())
        df = pandas.DataFrame(self.items)
        
        # Define o caminho para salvar o arquivo
        pasta_dados = 'dados'
        if not os.path.exists(pasta_dados):
            os.makedirs(pasta_dados)
        file_path = os.path.join(pasta_dados, f"{self.last_part}.xlsx")

        try:
            if os.path.exists(file_path):
                with pandas.ExcelWriter(file_path, engine="openpyxl", mode='a', if_sheet_exists='new') as writer:
                    df.to_excel(writer, sheet_name=self.last_part, index=False)
            else:
                # Se o arquivo não existir, cria um novo
                with pandas.ExcelWriter(file_path, engine="openpyxl") as writer:
                    df.to_excel(writer, sheet_name=self.last_part, index=False)
        except (FileNotFoundError, InvalidFileException, zipfile.BadZipFile):
            # Se houver um erro (e.g., arquivo não encontrado ou corrompido), cria um novo arquivo
            print(f"Erro ao manipular o arquivo Excel existente. Criando um novo arquivo: {file_path}")
            with pandas.ExcelWriter(file_path, engine="openpyxl") as writer:
                df.to_excel(writer, sheet_name=self.last_part, index=False)
        except Exception as e:
            print(f"Erro inesperado: {e}")


        # self.last_part = self.loja
        # self.last_part = unidecode(self.last_part.lower())
        # df = pandas.DataFrame(self.items)
        # file_path = "items.xlsx"
        # try:
        #     if os.path.exists(file_path):
        #         with pandas.ExcelWriter(file_path, engine="openpyxl", mode='a', if_sheet_exists='new') as writer:
        #             df.to_excel(writer, sheet_name=self.last_part, index=False)
        #     else:
        #         # If the file doesn't exist, create a new one
        #         with pandas.ExcelWriter(file_path, engine="openpyxl") as writer:
        #             df.to_excel(writer, sheet_name=self.last_part, index=False)
        # except (FileNotFoundError, InvalidFileException, zipfile.BadZipFile):
        #     # If there's an error (e.g., file not found or corrupted), create a new file
        #     print(f"Error handling existing Excel file. Creating a new file: {file_path}")
        #     with pandas.ExcelWriter(file_path, engine="openpyxl") as writer:
        #         df.to_excel(writer, sheet_name=self.last_part, index=False)
        # except Exception as e:
        #     print(f"Unexpected error: {e}")
