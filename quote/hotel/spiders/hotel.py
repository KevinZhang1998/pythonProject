import scrapy
from bs4 import BeautifulSoup
from hotel.items import HotelItem
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class StartHotel(CrawlSpider):
    name = "hotel"
    start_urls = ['http://quotes.toscrape.com/page/1/']
    custom_settings = {
        'LOG_LEVEL': 'ERROR'
    }
    rules = (Rule(LinkExtractor(allow=('http://quotes.toscrape.com/page/')), follow=True, callback='parse_page'),
             )

    def parse_page(self, response):
        soup = BeautifulSoup(response.body, 'lxml')
        for i in soup.select('div.quote'):
            quote = self.extract_title(i)
            author = self.extract_author(i)
            tags = self.extract_tags(i)
            item = HotelItem(quote=quote, author=author, tags=tags)
            print("%s  %s  %s \n" % (item['quote'], item['author'], item['tags']))
            yield item

    @staticmethod
    def extract_title(soup):
        selectors = ['span.text']
        for selector in selectors:
            if len(soup.select(selector)) > 0:
                return soup.select(selector)[0].text.strip()

    @staticmethod
    def extract_author(soup):
        selectors = ['small.author']
        for selector in selectors:
            if len(soup.select(selector)) > 0:
                return soup.select(selector)[0].text.strip()

    @staticmethod
    def extract_tags(soup):
        selectors = ['a.tag']
        for selector in selectors:
            if len(soup.select(selector)) > 0:
                return ','.join([a.text.strip() for a in soup.select(selector)])
