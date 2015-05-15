# -*- coding: utf-8 -*-

# Scrapy settings for ScrapySpider project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'ScrapySpider'
CONCURRENT_REQUEST = 200
LOG_LEVEL = 'INFO'
COOKIES_ENABLED = True
RETRY_ENABLED = True

SPIDER_MODULES = ['ScrapySpider.spiders']
NEWSPIDER_MODULE = 'ScrapySpider.spiders'

# JOBDIR = 'jobdir'
ITEM_PIPELINES = {
	'ScrapySpider.pipelines.XmlWritePipeline': 1000,
}
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'ScrapySpider (+http://www.yourdomain.com)'
