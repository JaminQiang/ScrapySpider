import scrapy

from tutorial.items import wishctItem

class wishctSpider(scrapy.Spider):
	name = "wishct"
	allowed_domains = ["www.wishct.com"]
	start_urls = [
		"http://www.wishct.com/x2/forum.php/"
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
		filename = response.url.split("/")[-2]
		with open(filename, 'wb') as f:
			f.write(response.body)
		"""
		for sel in response.xpath('//ul/li'):
			item = DmozItem()
			item['title'] = sel.xpath('a/text()').extract()
			item['link'] = sel.xpath('a/@href').extract()
			item['desc'] = sel.xpath('text()').extract()
			yield item
		"""