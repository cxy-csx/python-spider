import scrapy
from qsbk_spider.items import QsbkSpiderItem

class QsbkSpider(scrapy.Spider):
    name = 'qsbk'
    allowed_domains = ['qiushibaike.com']
    start_urls = ['https://www.qiushibaike.com/text/page/1/']

    def parse(self, response):
        divs = response.xpath("//div[@class='col1 old-style-col1']/div")
        for div in divs:
            author = div.xpath("./div[@class='author clearfix']//h2/text()").get().strip()
            content = "".join("".join(div.xpath(".//div[@class='content']//text()").getall()).strip().split())
            link = "https://www.qiushibaike.com" + div.xpath('./a/@href').get()
            # yield {
            #     'author': author,
            #     'content': content,
            #     'link': link
            # }
            yield QsbkSpiderItem(author=author, content=content, link=link)

