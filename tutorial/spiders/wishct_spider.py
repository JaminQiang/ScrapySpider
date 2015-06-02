import scrapy

from tutorial.items import wishctItem

class wishctSpider(scrapy.Spider):
	name = "wishct"
	allowed_domains = ["www.wishct.com"]
	start_urls = [
		#"http://www.wishct.com/x2/forum.php/",
		"http://www.wishct.com/x2/forum.php?mod=viewthread&tid=272858&extra=page%3D1"
		]

	"""
	def start_requests(self):
		return [scrapy.FormRequest("http://www.wishct.com/x2/forum.php?mod=viewthread&tid=272858&extra=page%3D1",
									formdata={'user':'sunwayhotel','pass':'4216wow521'},
									callback=self.logged_in)]

	def logged_in(self, response):
		# here you would extract links to follow and return Requests for
		# each of them, with another callback
		pass
	"""

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
			callback = self.after_login
			)

	def after_login(self, response):
		# check login succeed before going on
		if "authentication failed" in response.body:
			self.log("Login failed", level = log.ERROR)
			return

		filename = response.url.split("/")[-2]
		with open(filename, 'wb') as f:
			f.write(response.body)