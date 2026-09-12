import scrapy

class BaikeSpider(scrapy.Spider):
    name = "baike"
    allowed_domains = ["hddid.com"]
    start_urls = ["https://hddid.com/category-view-1-1.html"]
    prefix = "https://hddid.com/category-view-1"
    for i in range(2, 194):
        start_urls.append(prefix + "-" + str(i) + ".html")


    def parse(self, response):
        context = response.xpath('//dt[@class="h2"]/a/@href')
        filename = "website.txt"
        for i in context:
            open(filename, 'a').write(i.get()+'\n')
        # open(filename, 'wb+').write(response.body)

