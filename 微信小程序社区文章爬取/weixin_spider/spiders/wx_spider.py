import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from weixin_spider.items import WeixinSpiderItem


class WxSpiderSpider(CrawlSpider):
    name = 'wx_spider'
    allowed_domains = ['wxapp-union.com']
    start_urls = ['http://www.wxapp-union.com/portal.php?mod=list&catid=1&page=1']

    rules = (
        Rule(LinkExtractor(allow=r'.+mod=list&catid=1&page=\d'), follow=True),
        Rule(LinkExtractor(allow=r'.+article.+.html'), callback='parse_data', follow=True)
    )

    def parse_data(self, response):
        title = response.xpath("//h1[@class='ph']/text()").get()
        p = response.xpath("//p[@class='authors']")
        author = p.xpath("./a/text()").get()
        pub_time = p.xpath("./span/text()").get()
        content = "".join(response.xpath("//td[@id='article_content']//text()").getall()).strip()
        # print(title, author, pub_time, content)
        yield WeixinSpiderItem(title=title, author=author, pub_time=pub_time, content=content)
        # return item
