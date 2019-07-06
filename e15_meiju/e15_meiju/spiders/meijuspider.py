import scrapy

from e15_meiju.items import MeijuItem


class MeijuSpider(scrapy.Spider):
    name = "meiju"
    start_urls = ["https://www.meijutt.com/new100.html"]

    def parse(self, response):

        movies = response.xpath('//ul[@class="top-list  fn-clear"]/li')
        for movie in movies:
            item = MeijuItem()
            item['name'] = movie.xpath('./h5/a/@title').extract()[0]
            item['href'] = movie.xpath('./h5/a/@href').extract()[0]
            tv = movie.xpath('./span[@class="mjtv"]/text()')
            if len(tv):
                item['tv'] = tv
            else:
                item['tv'] = ""

            yield item

