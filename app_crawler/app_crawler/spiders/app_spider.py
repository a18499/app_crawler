from scrapy.spider import Spider 

class Appspider(Spider):
	name = "app"
	allowed_domains = ["app.hiapk.com"]  
    	start_urls = [  
        		"http://app.hiapk.com/category/"
    	]	
    	def parse(self, response):  
        		filename = response.url.split("/")[-2]
        		open(filename, 'wb').write(response.body)