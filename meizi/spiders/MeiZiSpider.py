import scrapy
from ..items import MeiziItem
class MeiZiSpider(scrapy.Spider):
    name = 'meizi'
    allowed_domains = ['www.mm131.com']
    start_urls = ['http://www.mm131.com/xinggan/']
    wrap_urls = set()
    def parse(self, response):
        wrap_htmls = response.css('.list-left dd:not(.page) a::attr(href)').extract()
        for wrap_html in wrap_htmls:
            yield scrapy.Request(url=wrap_html, callback=self.main_parse) 

    def main_parse(self, response):
        meizi_name = response.css('.content h5::text').extract()[0]
        meizi_url = response.css('.content-pic img::attr(src)').extract()[0]
        item = MeiziItem(meizi_name=meizi_name, meizi_url=meizi_url)
        yield item
        main_htmls = response.css('.page-en::attr(href)').extract()
        for main_html in main_htmls:
            yield response.follow(url=main_html, callback=self.main_parse)
            

        

