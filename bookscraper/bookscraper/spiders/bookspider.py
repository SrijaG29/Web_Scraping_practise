import scrapy


class BookspiderSpider(scrapy.Spider):
    name = "bookspider"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com"]

    def parse(self, response):
        books = response.css("article.product_pod")
        for book in books:
            relative_url = book.css('h3 a::attr(href)').get()
            
            if 'catalogue' in relative_url:
                relative_url_page = 'https://books.toscrape.com/' + relative_url
            else:
                relative_url_page = 'https://books.toscrape.com/catalogue/' + relative_url
                
            yield response.follow(relative_url_page,callback = self.parse_books)

        next_page = response.css('.next a::attr(href)').get()
        
        if next_page is not None:
            if 'catalogue' in next_page:
                next_url_page = 'https://books.toscrape.com/' + next_page
            else:
                next_url_page = 'https://books.toscrape.com/catalogue/' + next_page
            yield response.follow(next_url_page,callback = self.parse) 

    
    def parse_books(self,response):
        table_rows = response.css(".table.table-striped tr")
        yield{
            'url': response.url,
            'title':response.css('.product_main h1::text').get(),
            'product_type':table_rows[1].css('td::text').get(),
            'price':table_rows[3].css('td::text').get()
        }
        
        

    

