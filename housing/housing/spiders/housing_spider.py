from housing.items import HousingItemBuy
from scrapy import Spider
from scrapy.http.request import Request

#To parse the JSON received
import json

class HousingSpider(Spider):
    name = "housing"
    allowed_domains = ["housing.com"]
    custom_settings = {'USER_AGENT' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.111 Safari/537.36'}
    

    def start_requests(self):
        #We have 1080 pages to fetch
        for count in range(1,1081):
            
            print "Getting page : %s" %count
            
            yield Request("https://buy.housing.com/api/v1/buy/index/filter?poly=f97f947ffae6408ac295&results_per_page=30&p=" + str(count) + "&resale_total_count=30045&np_total_count=2329", self.parse_buy)

           
    def parse_buy(self, response):
        
        #Since the response is purely JSON
        text =  response.body

        #Parsing it using the builtin json utility
        parsed_json = json.loads(text)
        
        #For each entry, we will store all the information we defined earlier in items.py
        #The parsed json can be read as a dict. Examining the JSON, we can easily navigate 
        #to where we have the data we need.

        for iter in range(30):
            item = HousingItemBuy()
            item['ad_price'] = parsed_json["hits"][iter]["formatted_price"]
            item['ad_url'] = parsed_json["hits"][iter]["inventory_canonical_url"]
            item['ad_title'] = parsed_json["hits"][iter]["title"]
            item['ad_coordinates'] = parsed_json["hits"][iter]["location_coordinates"]
            item['ad_date_added'] = parsed_json["hits"][iter]["date_added"]
            item['ad_area'] = parsed_json["hits"][iter]["inventory_configs"][0]["area"]
            item['ad_bedrooms'] = parsed_json["hits"][iter]["inventory_configs"][0]["number_of_bedrooms"]
            item['ad_toilets'] = parsed_json["hits"][iter]["inventory_configs"][0]["number_of_toilets"]
            item['ad_contact_persons_number'] = parsed_json["hits"][iter]["contact_persons_info"][0]["contact_no"]
            item['ad_contact_persons_id'] = parsed_json["hits"][iter]["contact_persons_info"][0]["profile_id"]
            item['ad_contact_persons_name'] = parsed_json["hits"][iter]["contact_persons_info"][0]["name"]
            
            #Some entries do not have the ad_city/ad_locality variable. 
            try:
                item['ad_city'] = parsed_json["hits"][iter]["display_city"][0]
            except :
                item['ad_city'] = "None given"
                
            try:
                item['ad_locality'] = parsed_json["hits"][iter]["display_city"][1]
            except :
                item['ad_locality'] = "None given"
                
            item['ad_gas_pipeline'] = parsed_json["hits"][iter]["inventory_amenities"]["has_gas_pipeline"]
            item['ad_lift'] = parsed_json["hits"][iter]["inventory_amenities"]["has_lift"]
            item['ad_parking'] = parsed_json["hits"][iter]["inventory_amenities"]["has_parking"]
            item['ad_gym'] = parsed_json["hits"][iter]["inventory_amenities"]["has_gym"]
            item['ad_swimming_pool'] = parsed_json["hits"][iter]["inventory_amenities"]["has_swimming_pool"]
            item['ad_id'] = parsed_json["hits"][iter]["id"]
            yield item