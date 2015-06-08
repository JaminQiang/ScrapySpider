import scrapy

from tutorial.items import wishctItem

from scrapy.http import Request
from scrapy.selector import Selector
from scrapy.contrib.spiders import CrawlSpider
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.loader import ItemLoader

class wishctSpider(scrapy.Spider):
	name = "wishct"
	allowed_domains = ["www.wishct.com"]
	start_urls = [
		"http://www.wishct.com/",
		#"http://www.wishct.com/x2/forum.php/",
		#"http://www.wishct.com/x2/forum.php?mod=forumdisplay&fid=84"
		]
	link_extractor = {
		"forum": SgmlLinkExtractor(allow = 'forum\.php\?mod\=forumdisplay\&fid\=84$'),
		"page": SgmlLinkExtractor(allow = 'forum\.php\?mod\=viewthread&tid\=\d{6}&extra\=page\%3D1$'),
		"nextforum": SgmlLinkExtractor(allow = 'forum\.php\?mod\=forumdisplay\&fid\=84&page\=\d+$'),
		"nextpage": SgmlLinkExtractor(allow = 'forum\.php\?mod\=viewthread&tid\=\d{6}&extra\=page\%3D1$'),
	}

	_x_query = {
		'title': '//h1/a/text()',
		'poster': '//div[@class="authi"]/a[@class="xw1"]/text()',
		'content': '//div[@class="t_fsz"]/table/tr/td/text()',
	}

	"""
		for sel in response.xpath('//ul/li'):
			item = DmozItem()
			item['title'] = sel.xpath('a/text()').extract()
			item['link'] = sel.xpath('a/@href').extract()
			item['desc'] = sel.xpath('text()').extract()
			yield item
	"""

	def parse(self, response):
		return scrapy.FormRequest.from_response(
			response,
			formdata = {'username':'sunwayhotel', 'password':'4216wow521'},
			callback = self.homepage
			)

	def homepage(self, response):
		# check login succeed before going on
		if "authentication failed" in response.body:
			#self.log("Login failed", level = log.ERROR)
			print "login failed"
			return

		for link in self.link_extractor['forum'].extract_links(response):
			yield Request(url = link.url, callback = self.forum)
		"""
		# save the data scrapy got and check the data
		filename = response.url.split("/")[-2]
		with open(filename, 'wb') as f:
			f.write(response.body)
		"""

		"""
		# stop the program and insert shell to check the data online
		from scrapy.shell import inspect_response
		inspect_response(response)
		"""

	def forum(self, response):
		
		for link in self.link_extractor['nextforum'].extract_links(response):
			yield Request(url = link.url, callback = self.forum)
		
		for link in self.link_extractor['page'].extract_links(response):
			yield Request(url = link.url, callback = self.page)


		"""
		# test whether extract_links can get urls correctly
		if self.link_extractor['page'].extract_links(response):
			print self.link_extractor['page'].extract_links(response)
		else:
			print 'Nothing found'
		"""

	def page(self, response):
		
		#for link in self.link_extractor['nextpage'].extract_links(response):
		#	yield Request(url = link.url, callback = self.page)

		wishctItem_loader = ItemLoader(item = wishctItem(), response = response)
		url = str(response.url)
		wishctItem_loader.add_value('url', url)
		wishctItem_loader.add_xpath('title', self._x_query['title'])
		poster = response.xpath(self._x_query['poster']).extract()[0]
		wishctItem_loader.add_value('poster', poster)
		#wishctItem_loader.add_xpath('content', self._x_query['content'])

		return wishctItem_loader.load_item()
		"""
		# stop the program and insert shell to check the data online
		from scrapy.shell import inspect_response
		inspect_response(response)
		"""		

