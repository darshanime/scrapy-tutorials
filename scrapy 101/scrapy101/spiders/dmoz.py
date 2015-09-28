from scrapy.spiders import BaseSpider
from scrapy101.items import Scrapy101Item

class Scrapy101Spider(BaseSpider):
    name = "dmoz"
    allowed_domains = ["dmoz.org/"]
    start_urls = ["http://www.dmoz.org/"]
    
    def parse(self, response):
        for div in response.xpath('/html/body/div[3]/div[3]/div[1]/div'):
            for entry in div.xpath('span'):
                item = Scrapy101Item()
                item['title'] = entry.xpath('a/text()').extract()
                print item['title']