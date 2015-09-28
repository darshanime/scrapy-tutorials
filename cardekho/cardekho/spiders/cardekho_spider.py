from cardekho.items import CardekhoItem
from scrapy import Spider
from scrapy.http.request import Request

class CardekhoSpider(Spider):
    name = "cardekho"
    allowed_domains = ["http://www.cardekho.com"]
    start_urls = ["http://www.cardekho.com/used-cars+in+mumbai-all/"]
    
    #This is to not get redirected by CarDekho. We are identifying ourselves as a web-browser. 
    custom_settings = {'USER_AGENT' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.111 Safari/537.36'}
    
    def start_requests(self):
        #There are 162 pages, we are asking Scrapy to get us all of them.
        for i in range(162):
            yield Request("http://www.cardekho.com/used-cars+in+mumbai-all/" + str(i), self.parse)

    def parse(self, response):
        for sel in response.xpath('/html/body/main/div/div[2]/div[2]/div[9]/form/ul/li'):
            item = CardekhoItem()
            item ['title'] = sel.xpath('div[1]/div[2]/div[1]/a/text()').extract()
            item ['price'] = sel.xpath('div[1]/div[3]/div[1]/text()').extract()
            item ['distance'] = sel.xpath('div[1]/div[2]/div[3]/ul/li[1]/div[2]/span/text()').extract()                      
            yield item