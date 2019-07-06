import sys
from scrapy.utils.project import get_project_settings
from scrapy.crawler import CrawlerProcess
from scrapyuniversal.spiders.universal import UniversalSpider
from scrapyuniversal.utils import get_config


def run():
    name = sys.argv[1]  # 获取命令行参数，这里就是china
    custom_settings = get_config(name)  # 相当于拿到china.json配置文件
    # 爬取使用的spider名称
    spider = custom_settings.get('spider', 'universal')
    project_settings = get_project_settings()
    settings = dict(project_settings.copy())  # 弄个副本然后搞成一个字典什么意思呢？
    # 合并配置 这一块理解的不好
    # 应该是把china.json配置文件里面的settings设置，更新到项目配置里面去
    settings.update(custom_settings.get('settings'))
    process = CrawlerProcess(settings)
    # 启动爬虫
    process.crawl(spider, **{'name': name})  # 这里是勾上了spider--universal--UniversalSpider
    process.start()

    name = sys.argv[1]
    custom_settings = get_config(name)
    spider = custom_settings.get('spider', 'universal')
    project_settings = get_project_settings()
    settings = dict(project_settings.copy())
    settings.update(custom_settings.get('settings'))
    process = CrawlerProcess(settings)
    process.crawl(spider, **{'name': name})
    process.start()

if __name__ == '__main__':
    run()


