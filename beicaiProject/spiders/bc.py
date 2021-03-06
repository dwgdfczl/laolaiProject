# -*- coding: utf-8 -*-
import scrapy
import re
from scrapy.linkextractors import LinkExtractor    
from scrapy.spiders import CrawlSpider, Rule       
from beicaiProject.items import BeicaiprojectItem

class BcSpider(CrawlSpider):
    name = 'bc'
    allowed_domains = ['www.thebetterchinese.com']
    # start_urls = ['http://www.thebetterchinese.com/']
    start_urls = ['https://www.thebetterchinese.com/show/lai.html']
    #/show/lai.html?pageNo=1&pageSize=10
    page_links = LinkExtractor(restrict_xpaths='//div[@class="pagelib"]//a')
    rules = (
        Rule(page_links, callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        content_div = response.xpath('//div[@class="toad_detention_xxcon_left"]/div')
        for content in content_div:
            item = BeicaiprojectItem()
            name = content.xpath('.//p/span[@class="zhen_name1"]/text()').extract()
            item['姓名'] = name[0] if name else '暂无姓名信息'

            danger = content.xpath('.//p/b/text()').extract()
            item['危险等级'] = danger[0] if danger else '暂无危险等级信息'

            money = content.xpath('.//p/span[@class="etention_xqxxaa"]/b/text()').extract()
            item['逾期金额'] = money[0] if money else '暂无逾期金额信息'

            address = content.xpath('.//p[2]/text()').extract_first()
            item['出生地址'] = address.replace('出生地址：','') if address else '暂无出生地址信息'

            agree = content.xpath('.//span[@class="tongyi_bty1"]/input/@value').extract()
            item['同意'] = agree[0] if agree else '暂无同意信息'

            disagree = content.xpath('.//span[@class="tongyi_bty2"]/input/@value').extract()
            item['不同意'] = disagree[0] if disagree else '暂无不同意信息'

            yield item
