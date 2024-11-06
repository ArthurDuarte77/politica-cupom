# Scrapy settings for lojasMercadolivre project

BOT_NAME = "lojasMercadolivre"

SPIDER_MODULES = ["lojasMercadolivre.spiders"]
NEWSPIDER_MODULE = "lojasMercadolivre.spiders"

# Use um User-Agent mais comum
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Reduzir o número de requisições concorrentes
CONCURRENT_REQUESTS = 8

# Adicionar um delay entre as requisições
DOWNLOAD_DELAY = 2

# Reduzir o número de requisições concorrentes por domínio e IP
CONCURRENT_REQUESTS_PER_DOMAIN = 4
CONCURRENT_REQUESTS_PER_IP = 4

# Manter os cookies habilitados
COOKIES_ENABLED = True

# Manter os middlewares de cookies
SPIDER_MIDDLEWARES = {
   'scrapy.downloadermiddlewares.cookies.CookiesMiddleware': 700,
}

DOWNLOADER_MIDDLEWARES = {
   'scrapy.downloadermiddlewares.cookies.CookiesMiddleware': 700,
}

# Configurar o AutoThrottle para ser mais conservador
AUTOTHROTTLE_ENABLED = True
AUTOTHROTTLE_START_DELAY = 5
AUTOTHROTTLE_MAX_DELAY = 60
AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
AUTOTHROTTLE_DEBUG = False

# Manter as configurações padrão para o restante
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"