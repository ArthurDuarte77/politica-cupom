import json
import requests
import zipfile
import os
from openpyxl.utils.exceptions import InvalidFileException
from unidecode import unidecode
import scrapy
import pandas
from datetime import datetime



class MlSpider(scrapy.Spider):
    name = "ml"
    allowed_domains = ["mercadolivre.com.br"]
    start_urls = ["https://lista.mercadolivre.com.br/fonte-60a-jfa"]
    items = []
    loja = ""
    last_part = ""
    contagem = 0
    is_full = ""
    fullis = ""

    def __init__(self, palavra=None, *args, **kwargs):
        super(MlSpider, self).__init__(*args, **kwargs)
        self.palavra = palavra
        
    def parse(self, response, **kwargs):
        yield scrapy.Request(url=self.palavra, callback=self.parse_img, cookies=json.load(open('cookies.json')))

    def parse_produto(self, response, nome, link):
        loja = response.xpath('/html/body/main/div[2]/div[3]/div[2]/div[2]/div[2]/div/div[1]/form/div[6]/div/div/div[1]/div/button/span[2]/text()')      
        price = response.xpath('/html/body/main/div[2]/div[3]/div[2]/div[2]/div[1]/div/div[1]/div[2]/div[2]/div[1]/div[1]/span[1]/span/span[@class="andes-money-amount__fraction"]/text()')
        cents = response.xpath('/html/body/main/div[2]/div[3]/div[2]/div[2]/div[1]/div/div[1]/div[2]/div[2]/div[1]/div[1]/span[1]/span/span[@class="andes-money-amount__cents andes-money-amount__cents--superscript-36"]/text()')
        if not loja:
            print(response.url)
        requests.post("http://134.122.29.170:3000/api/sendText", {
            "chatId": "120363336339920249@g.us",
            "text": f"{loja} - {nome} - {link} - {price},{cents}",
            "session": "default"
        })
        
    
    def parse_img(self, response):
        self.contagem += 1
            
        for i in response.xpath('//*[@id="root-app"]/div/div[3]/section/ol/li'):
            nome = i.xpath('.//div/div/div[2]/h2/a/text()').get()
            link = i.xpath('.//div/div/div[2]/h2/a/@href').get()
            if not nome:
                continue
            if "jfa" not in nome.lower():
                continue
            
            requests.post("http://134.122.29.170:3000/api/sendText", {
                "chatId": "120363336339920249@g.us",
                "text": f"{nome} \n {link}",
                "session": "default"
            })

            # yield scrapy.Request(url=link, callback=self.parse_produto, cb_kwargs={"nome": nome, "link": link})
                
                
        next_page = response.xpath('//li[@class = "andes-pagination__button andes-pagination__button--next"]/a[@class = "andes-pagination__link"]/@href').get()
        if next_page:
            yield scrapy.Request(url=next_page, callback=self.parse_img)
