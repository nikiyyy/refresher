import scrapy


class TopmoviesSpider(scrapy.Spider):
    name = 'topMovies'
    allowed_domains = ['imdb.com']
    start_urls = ['http://imdb.com/']

    def parse(self, response):

        for i in  response.css('td.titleColumn a::attr(href)').getall():
            yield response.follow('http://imdb.com' + i, callback = self.parse)
        
    def parse_movie(self, response):
        #response.xpath('//*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[3]/div[2]/div[1]/div[3]/ul/li[1]/div/ul/li/a/text()').get()
        pass
#change