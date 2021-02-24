import scrapy
from qsbk.items import QsbkItem


class QsbkSpiderSpider(scrapy.Spider):
    name = 'qsbk_spider'
    allowed_domains = ['qiushibaike.com']
    start_urls = ['https://www.qiushibaike.com/text/page/1/']
    base_domain = 'https://www.qiushibaike.com'

    def parse(self, response):
        html = response
        divs = html.xpath("//div[@class='col1 old-style-col1']/div")
        for div in divs:
            author = div.xpath("./div[@class='author clearfix']//h2/text()").get().strip()
            content = "".join(div.xpath(".//div[@class='content']//span/text()").getall()).strip()

            # yield {
            #     'author': author,
            #     'content': content
            # }
            yield QsbkItem(author=author, content=content)

        next_url = html.xpath("//ul[@class='pagination']/li[last()]/a/@href").get()

        if next_url:
            full_url = self.base_domain + next_url
            yield scrapy.Request(full_url, callback=self.parse)
