import scrapy
import re
from qq.items import QQItem

class QQSpider(scrapy.Spider):
    name = 'qq'
    allowed_domains = ['hr.tencent.com']
    start_urls = ['https://hr.tencent.com/position.php?&start=0#a']

    def parse(self, response):
        for each in response.xpath('//*[@class="even"]'):
            item = QQItem()
            name = each.xpath('./td[1]/a/text()').extract()[0]
            detaillink = each.xpath('./td[1]/a/@href').extract()[0]
            # positionInfo = each.xpath('./td[2]/text()').extract()[0]
            # workLocation = each.xpath('./td[4]/text()').extract()[0]

            item['name'] = name.encode('utf-8')
            item['detaillink'] = detaillink.encode('utf-8')
            # item['positionInfo'] = positionInfo.encode('utf-8')
            # item['workLocation'] = workLocation.encode('utf-8')

            curpage = re.search('(\d+)', response.url).group(1)
            page = int(curpage)+10
            url = re.sub('\d+', str(page), response.url)

            yield scrapy.Request(url, callback=self.parse)

            yield item
