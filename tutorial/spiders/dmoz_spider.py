import scrapy

from tutorial.items import DmozItem

class DmozSpider(scrapy.Spider):
	name = "dmoz"
	allowed_domains = ["dmoz.org"]
	start_urls = [
		"http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
		"http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
		]

	"""
	def start_requests(self):
		return [scrapy.FormRequest("http://www.example.com/login",
									formdata={'user':'john','pass':'secret'},
									callback=self.logged_in)]

	def logged_in(self, response):
		# here you would extract links to follow and return Requests for
		# each of them, with another callback
		pass
	"""

	def parse(self, response):
		for sel in response.xpath('//ul/li'):
			item = DmozItem()
			item['title'] = sel.xpath('a/text()').extract()
			item['link'] = sel.xpath('a/@href').extract()
			item['desc'] = sel.xpath('text()').extract()
			yield item