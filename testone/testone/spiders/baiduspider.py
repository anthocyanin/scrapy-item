import scrapy


class BaiduSpider(scrapy.Spider):
    name = "baidu"
    start_urls = ["http://www.baidu.com"]


    def parse(self, response):

        with open('baidu.html', 'w', encoding='utf-8') as f:
            f.write(response.body.decode('utf-8'))
