import scrapy
from urllib import  request

from e17_xiaohua.items import XiaohuaItem


class XiaohuaSpider(scrapy.Spider):

    name = 'xiaohua'
    allowed_domains = ['xiaohua100.cn']

    start_urls = ['http://xiaohua100.cn']


    def parse(self, response):

        bookmarks = response.xpath('//div[@data-uid="1"')

        for bm in bookmarks:
            item = XiaohuaItem()

            title = bm.xpath('.//h3/span[@class="cellTit"]/a/text()').extract()[0]
            href = bm.xpath('.//h3/span[@class="cellTit"]/a/@href').extract()[0]
            src = bm.xpath('.//div[@class="pic"]/a/img/@src').extract()[0]


            item['title'] = title
            item['href'] = request.urljoin(response.url, href)
            item['src'] = request.urljoin(response.url, src)

            yield item
