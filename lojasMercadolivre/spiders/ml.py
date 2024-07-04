import zipfile
import os
from openpyxl.utils.exceptions import InvalidFileException
from unidecode import unidecode
import scrapy
import pandas as pd

class MlSpider(scrapy.Spider):
    name = "ml"
    allowed_domains = ["mercadolivre.com.br"]
    start_urls = ["https://lista.mercadolivre.com.br/pagina/radicalsom/"]
    items = []
    loja = ""
    last_part = ""
    contagem = 0

    def __init__(self, palavra=None, loja=None, *args, **kwargs):
        super(MlSpider, self).__init__(*args, **kwargs)
        self.palavra = palavra
        self.loja = loja
        
    def parse(self, response, **kwargs):
        yield scrapy.Request(url=self.palavra, callback=self.parse_img)

    def parse_img(self, response):
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
                    is_classico = "Premium"
                    break
                else: 
                    is_classico = "Classico"
            if full:
                is_full = "FULL"
            else:
                full = i.xpath('.//div/div/div[2]/div/div[5]/div/p').get()
                is_full = "NA"

            if not nome:
                nome = i.xpath('.//div/div/div[2]/div/div[2]/a/@title').get()


            self.items.append({
                "nome": nome,
                "preco": preco,
                "full": is_full,
                "tipo": is_classico,
                "link": link,
            })
        
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
                        is_classico = "Premium"
                        break
                    else: 
                        is_classico = "Classico"
                if full:
                    is_full = "FULL"
                else:
                    full = i.xpath('.//div/div/div[2]/div/div[5]/div/p').get()
                    is_full = "NA"

                if not nome:
                    nome = i.xpath('.//div/div/div[2]/div/div[2]/a/@title').get()


                self.items.append({
                    "nome": nome,
                    "preco": preco,
                    "full": is_full,
                    "tipo": is_classico,
                    "link": link,
                })
        next_page = response.xpath('//li[@class = "andes-pagination__button andes-pagination__button--next"]/a[@class = "andes-pagination__link"]/@href').get()
        if next_page:
            yield scrapy.Request(url=next_page, callback=self.parse_img)

    def closed(self, reason):       
        self.last_part = self.loja
        self.last_part = unidecode(self.last_part.lower())
        df = pd.DataFrame(self.items)
        
        # Define o caminho para salvar o arquivo
        pasta_dados = 'dados'
        if not os.path.exists(pasta_dados):
            os.makedirs(pasta_dados)
        file_path = os.path.join(pasta_dados, f"{self.last_part}.xlsx")

        try:
            if os.path.exists(file_path):
                with pd.ExcelWriter(file_path, engine="openpyxl", mode='a', if_sheet_exists='new') as writer:
                    df.to_excel(writer, sheet_name=self.last_part, index=False)
            else:
                # Se o arquivo não existir, cria um novo
                with pd.ExcelWriter(file_path, engine="openpyxl") as writer:
                    df.to_excel(writer, sheet_name=self.last_part, index=False)
        except (FileNotFoundError, InvalidFileException, zipfile.BadZipFile):
            # Se houver um erro (e.g., arquivo não encontrado ou corrompido), cria um novo arquivo
            print(f"Erro ao manipular o arquivo Excel existente. Criando um novo arquivo: {file_path}")
            with pd.ExcelWriter(file_path, engine="openpyxl") as writer:
                df.to_excel(writer, sheet_name=self.last_part, index=False)
        except Exception as e:
            print(f"Erro inesperado: {e}")


        # self.last_part = self.loja
        # self.last_part = unidecode(self.last_part.lower())
        # df = pd.DataFrame(self.items)
        # file_path = "items.xlsx"
        # try:
        #     if os.path.exists(file_path):
        #         with pd.ExcelWriter(file_path, engine="openpyxl", mode='a', if_sheet_exists='new') as writer:
        #             df.to_excel(writer, sheet_name=self.last_part, index=False)
        #     else:
        #         # If the file doesn't exist, create a new one
        #         with pd.ExcelWriter(file_path, engine="openpyxl") as writer:
        #             df.to_excel(writer, sheet_name=self.last_part, index=False)
        # except (FileNotFoundError, InvalidFileException, zipfile.BadZipFile):
        #     # If there's an error (e.g., file not found or corrupted), create a new file
        #     print(f"Error handling existing Excel file. Creating a new file: {file_path}")
        #     with pd.ExcelWriter(file_path, engine="openpyxl") as writer:
        #         df.to_excel(writer, sheet_name=self.last_part, index=False)
        # except Exception as e:
        #     print(f"Unexpected error: {e}")
