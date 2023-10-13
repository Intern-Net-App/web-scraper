# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class IndeedScraperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class IndeedJob(scrapy.Item):
    job_title = scrapy.Field()
    job_detail_url = scrapy.Field()
    company_name = scrapy.Field()
    company_link = scrapy.Field()
    company_location = scrapy.Field()
    pass
