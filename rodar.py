import sys
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from lojasMercadolivre.spiders.ml import MlSpider

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python start_scrapy.py <palavra>")
        sys.exit(1)

    palavra = sys.argv[1]
    loja = sys.argv[2]

    settings = get_project_settings()
    settings.set('LOG_LEVEL', 'ERROR')

    process = CrawlerProcess(settings)
    process.crawl(MlSpider, palavra=palavra, loja = loja)
    process.start()
