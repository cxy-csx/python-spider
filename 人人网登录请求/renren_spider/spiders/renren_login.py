import scrapy


class RenrenLoginSpider(scrapy.Spider):
    name = 'renren_login'
    allowed_domains = ['renren.com']
    start_urls = ['http://renren.com/']

    def start_requests(self):
        url = 'http://www.renren.com/PLogin.do'
        data = {
            "email": "",
            "password": ""
        }
        request = scrapy.FormRequest(url, formdata=data, callback=self.parse)

        yield request

    def parse(self, response):
        url = 'http://www.renren.com/880151247/profile'
        request = scrapy.Request(url, callback=self.parse_page)
        yield request

    def parse_page(self, response):
        with open('renren.html', 'w', encoding='UTF-8') as fp:
            fp.write(response.text)
