from gc import callbacks
from urllib.request import Request
import scrapy


class TopmoviesSpider(scrapy.Spider):
    name = 'topMovies'
    allowed_domains = ['imdb.com']
    start_urls = ['https://www.imdb.com/chart/top/?ref_=nv_mv_250']
    count=1

    def parse(self, response):
        for i in response.css('td.titleColumn a::attr(href)').getall():
            #if self.count <2:
                #self.count+=1
            yield scrapy.Request('http://imdb.com' + i, callback=self.movie_parse)

        
    def movie_parse(self, response):
        yield {
            "Title" : response.xpath('//*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[1]/div[1]/h1/text()').get(),
            "Director" : response.xpath('//*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[3]/div[2]/div[1]/div[3]/ul/li[1]/div/ul/li/a/text()').get(),
            "Year" : response.xpath('//*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[1]/div[1]/div[2]/ul/li[1]/a/text()').get(),
            "Score" : response.xpath('//*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[3]/div[2]/div[1]/div[2]/div/div[1]/a/div/div/div[2]/div[1]/span[1]/text()').get()
        }