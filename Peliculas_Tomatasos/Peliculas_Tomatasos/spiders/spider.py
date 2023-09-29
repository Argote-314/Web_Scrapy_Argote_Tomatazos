import scrapy
from ..items import PeliculasTomatasosItem


class Peliculas(scrapy.Spider):
    name = "peliculas"
    start_urls = ["https://www.tomatazos.com/peliculas/genre/Drama/orden/hits"]

    def parse(self, response):
        item = PeliculasTomatasosItem()

        all_div_li = response.css("#catalogContainer ul:nth-child(1) li")

        for li in all_div_li:
            title = li.xpath('article/p/a/text()').get()
            tomates = li.xpath("article/div/p/text()").get()
            item["title"] = title
            item["tomates"] = tomates

            yield item