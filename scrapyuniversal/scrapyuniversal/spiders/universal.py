# -*- coding: utf-8 -*-
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapyuniversal.items import NewsItem
from scrapyuniversal.loaders import *
from scrapyuniversal.utils import get_config
from scrapyuniversal import urls
from scrapyuniversal.rules import rules


class UniversalSpider(CrawlSpider):
    name = 'universal'

    def __init__(self, name, *args, **kwargs):
        config = get_config(name)  # 获取配置文件
        self.config = config
        self.rules = rules.get(config.get('rules'))  # 爬取规则
        start_urls = config.get('start_urls')  # 开始url
        if start_urls:
            if start_urls.get('type') == 'static':
                self.start_urls = start_urls.get('value')
            elif start_urls.get('type') == 'dynamic':
                self.start_urls = list(eval('urls.' + start_urls.get('method'))(*start_urls.get('args', [])))
        self.allowed_domains = config.get('allowed_domains')  # 爬取域
        super(UniversalSpider, self).__init__(*args, **kwargs)  # 这里需要深入理解一下

    def parse_item(self, response):
        item = self.config.get('item')
        if item:
            cls = eval(item.get('class'))()  # 相当于初始化NewsItem()，这样写好处是能够动态获取
            loader = eval(item.get('loader'))(cls, response=response)  # 相当于传入NewsItem实例，初始化ChinaLoader()
            # 动态获取属性配置
            for key, value in item.get('attrs').items():
                # value又是一个字典，可迭代
                for extractor in value:
                    if extractor.get('method') == 'xpath':
                        loader.add_xpath(key, *extractor.get('args'), **{'re': extractor.get('re')})
                    if extractor.get('method') == 'css':
                        loader.add_css(key, *extractor.get('args'), **{'re': extractor.get('re')})
                    if extractor.get('method') == 'value':
                        loader.add_value(key, *extractor.get('args'), **{'re': extractor.get('re')})
                    if extractor.get('method') == 'attr':
                        loader.add_value(key, getattr(response, *extractor.get('args')))
            yield loader.load_item()
