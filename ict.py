import scrapy
import json


class IctSpider(scrapy.Spider):
    name = 'ict'
    allowed_domains = ['ictnews.ir']
    start_urls = ['http://ictnews.ir/']

    # Custom Settings are needed to send the User Agent.
    custom_settings = {
        'USER_AGENT' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
    }

    def parse(self, response):
        json_response = json.loads(response.text)
        listings = json_response["data"]
        for listing in listings:
            yield {
                "title-post": listing["title-post"],
                "date": listing["post-tags"],
                "lead": listing["lead-holder"],
                "content": listing["post-content"],
            }