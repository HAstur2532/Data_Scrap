import scrapy

class GengSpider(scrapy.Spider):
    name = "geng"
    allowed_domains = ["hddid.com"]
    start_urls = []
    prefix = "https://hddid.com/"
    with open("website.txt", 'r') as txt:
        all_lines = txt.readlines()
        for line in all_lines:
            start_urls.append(prefix + line.strip())
    # start_urls = start_urls[:5]

    def parse(self, response):
        title = response.xpath('//div[@class = "title_thema"]/h1/text()')
        contextList = []
        contexts = response.xpath('//div[@class="content_topp"]//text()').getall()
        contextList += contexts
        assert contextList
        text = str()
        for c in contextList:
            text += c
        filename = "output2.txt"
        open(filename, 'a', encoding='UTF-8').write("Q:" + title.get() + '\n' + "A:" + text + '\n\n')
        pass

