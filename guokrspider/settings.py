# -*- coding: utf-8 -*-

# Scrapy settings for guokrspider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'guokrspider'

SPIDER_MODULES = ['guokrspider.spiders']
NEWSPIDER_MODULE = 'guokrspider.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'guokrspider (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
# }

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'guokrspider.middlewares.GuokrspiderSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    'guokrspider.middlewares.MyCustomDownloaderMiddleware': 543,
# }

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'guokrspider.pipelines.GuokrspiderPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

MONGO_HOST = '192.168.192.128'
MONGO_PORT = 27017
MONGO_DB = 'spider'
MONGO_COLL = 'guokr'


class transCookie:
    def __init__(self, cookie):
        self.cookie = cookie

    def stringToDict(self):
        """
            将从浏览器上Copy来的cookie字符串转化为Scrapy能使用的Dict
        """
        itemDict = {}
        items = self.cookie.split(';')
        for item in items:
            key = item.split('=')[0].replace(' ', '')
            value = '='.join(item.split('=')[1:])
            itemDict[key] = value
        return itemDict


cookie = "support=1; post_like=1; Hm_lvt_95dfd07652f91dffd9647f46a3ca9fab=1485877213,1487750503;" \
         " toast_ban_create_user=true; isN=1; __utmt=1;" \
         " __utma=253067679.2027234800.1478413245.1502358164.1502420041.272; __utmb=253067679.14.8.1502420974033;" \
         " __utmc=253067679; __utmz=253067679.1478413245.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none);" \
         " __utmv=253067679.|1=Is%20Registered=Yes=1;" \
         " _32382_access_token=129cd19f9720e0e1a38320595afca220457e1989537c8adfcaf8e24f35485744; _32382_ukey=5mq7qr;" \
         " _32382_auto_signin=1;" \
         " _32353_access_token=795220465c300d6f03343882ce5d41b642cacd2e1e55e077215e9063cd3d6c3b;" \
         " _32353_ukey=5mq7qr; _32353_auto_signin=1"
trans = transCookie(cookie)
# print(trans.stringToDict())
COOKIE = trans.stringToDict()
