# -*- coding: utf-8 -*-
import scrapy
from beicaiProject.items import BeicaiprojectItem

class Bc1Spider(scrapy.Spider):
    name = 'bc1'
    allowed_domains = ['www.thebetterchinese.com']
    start_urls = ['https://www.thebetterchinese.com/show/lai.html']
    url = 'https://www.thebetterchinese.com/show/lai.html?pageNo={}'
    page = 2

    def start_requests(self):
    	url = self.url.format(self.page)
    	yield scrapy.Request(url,callback=self.parse)

    def parse(self, response):

    	content_div = response.xpath('//div[@class="toad_detention_xxcon_left"]/div[@class="detention_all"]')
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

    		if self.page <=25:
    			self.page +=1
    			url = self.url.format(self.page)
    			yield scrapy.Request(url,callback=self.parse)


