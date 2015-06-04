import scrapy

from tutorial.items import wishctItem

from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor


class wishctSpider(scrapy.Spider):
	name = "wishct"
	allowed_domains = ["www.wishct.com"]
	start_urls = [
		"http://www.wishct.com/x2/forum.php/",
		#"http://www.wishct.com/x2/forum.php?mod=forumdisplay&fid=84"
		]
	link_extractor = {
		"forum": SgmlLinkExtractor(allow = 'forum.php.*'),
		"page": SgmlLinkExtractor(allow = ''),
		"nextforum": SgmlLinkExtractor(allow = ''),
		"nextpage": SgmlLinkExtractor(allow = ''),
	}

	"""
	def parse(self, response):
		filename = response.url.split("/")[-2]
		with open(filename, 'wb') as f:
			f.write(response.body)

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
			self.log("Login failed", level = log.ERROR)
			return
		
		if self.link_extractor['forum'].extract_links(response):
			print self.link_extractor['forum'].extract_links(response)
		else:
			print 'Nothing found'
		#for link in self.link_extractor['forum'].extract_links(response):
			#yield Request(url = link.url, callback = self.forum)
		"""
		from scrapy.shell import inspect_response
		inspect_response(response)
		"""

	def forum(self, response):
		"""
		for link in self.link_extractor['nextforum'].extract_links(response):
			yield Request(url = link.url, callback = self.forum)
		for link in self.link_extractor['page'].extract_links(response):
			yield Request(url = link.url, callback = self.page)
		"""
		filename = response.url.split("/")[-2]
		with open(filename, 'wb') as f:
			f.write(response.body)

	def page(self, response):
		pass












