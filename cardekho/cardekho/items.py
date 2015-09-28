from scrapy import Item, Field

class CardekhoItem(Item):
    title = Field()
    price = Field()
    distance = Field()