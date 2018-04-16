#测试一下
import csv,numpy
import scrapy,urllib.request
import os

home = os.environ['HOME']
data_dir = home + r"/data/"
dividend_dir = data_dir + r"dividend/"

class TestSpider(scrapy.Spider):
    name = "quotes"
    allowed_domains = ["nasdaq.com"]


    custom_settings = {
        'CONCURRENT_REQUESTS': 1,
        'DOWNLOAD_DELAY': 3,
        'AUTOTHROTTLE_ENABLED': True,
        'RANDOMIZE_DOWNLOAD_DELAY': True
    }
    def __init__(self, *args, **kw):
        self.timeout = 10

    def start_requests(self):
        csvfile = open(data_dir + 'stock.csv')
        reader = csv.reader(csvfile)
        stocks = [row[0] for row in reader]  
        x=numpy.arange(len(stocks)-1)
        numpy.random.shuffle(x)
        new_stocks=[]
        for i in x:
            new_stocks.append(stocks[i].lower())
        stocks=new_stocks              

        for s in stocks:
             url = "http://www.nasdaq.com/symbol/" + s + "/dividend-history"
             yield scrapy.Request(url, callback=self.parse)
       
    def parse(self, response):
        try:
            content = response.body
            target = response.url
            fn = target.replace("http://www.nasdaq.com/symbol/","").split(r"/")[0]
            with open(dividend_dir + fn , 'wb') as downloaded:
                downloaded.write(content)
        except : 
            print(fn)
