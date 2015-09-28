from scrapy import Item, Field

class HousingItemBuy(Item):
    ad_id = Field()
    ad_title = Field()
    ad_price = Field()
    ad_area = Field()
    ad_url = Field()
    ad_date_added = Field()
    ad_coordinates = Field()
    ad_bedrooms = Field()
    ad_toilets = Field()
    ad_gas_pipeline = Field()
    ad_lift = Field()
    ad_parking = Field()                                   
    ad_gym = Field()
    ad_swimming_pool = Field()
    ad_city = Field()
    ad_locality = Field()
    ad_contact_persons_name = Field()
    ad_contact_persons_number = Field()
    ad_contact_persons_id = Field()
    count = Field()