from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst, Join, Compose
# 这一部分loader 就不是太理解了
# Identify, TakeFirst, Join, Compose, MapCompose, SelectJams都是内置的process


class NewsLoader(ItemLoader):
    default_output_processor = TakeFirst()


class ChinaLoader(NewsLoader):
    text_out = Compose(Join(), lambda s: s.strip())
    source_out = Compose(Join(), lambda s: s.strip())

