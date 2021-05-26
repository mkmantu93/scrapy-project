import scrapy

class JobsSpider(scrapy.Spider):

    name = 'jobs'

    # allowed_domains = ['https://www.amazon.de']

    custom_settings = {
        'FEED_URI': 'Amazone.csv',
        'FEED_FORMAT': 'csv'
    }

    start_urls = ['https://www.amazon.de/s?bbn=3597086031&rh=n%3A3167641%2Cn%3A%213169011%2Cn%3A3597086031%2Cn%3A13528286031%2Cp_36%3A2000-99999999&dc&fst=as%3Aoff&qid=1507905316&rnid=3597086031&ref=sr_nr_n_0']

    def parse(self, response):
        url_size = response.xpath('//div[@class="a-section a-spacing-medium"]/span/a').get()
        if url_size:
            url_size = response.xpath('//div[@class="a-section a-spacing-medium"]/span/a/@href').extract()
            for url in url_size:
                url = 'https://www.amazon.de' + url
                yield scrapy.Request(response.url, callback=self.parseDetails)
        # else:
        #
        #     yield scrapy.FormRequest(response.url, method="GET", callback=self.parseDetails)


    def parseDetails(self, response):

            title = response.xpath('//*[@id="productTitle"]/text()').get()
            coc = response.xpath('//span[@id="priceblock_ourprice"]/text()').get()
            # mpn = response.xpath('//span[contains(text(),"MPN")]/strong/text()').get()
            # imgUrl = response.xpath('//a[@id="ProductImage"]/@href').getall()
            # datasheetUrl = response.xpath('//div[@id="dataSheets"]/a/@href').getall()
            # catpath = response.xpath('//ul[@class="breadcrumbs"]//li//span/text()').getall()
            # catpath = list(map( lambda x:x.replace('\n','').strip(), catpath))
            # catpath = '/'.join(catpath)


            item = {
                        'Title':title,
                        # 'categorypath':catpath,
                        # 'page':page,
                        'Coc':coc,
                        # 'MPN':mpn,
                        # 'image_urls':list(map( lambda x: 'https:'+x, imgUrl)),
                        # 'file_urls':list(map( lambda x: 'https:'+x, datasheetUrl)),

                    }
            print(item)

            yield item

