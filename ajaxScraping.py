#coding:utf-8


from lxml import html
from time import sleep

flithts = []   #航班
fly_times = [] #起飞时间
fly_airports = [] #起飞机场
land_times = [] #降落时间
land_airports = [] #降落机场
low_prices = [] #最低价格

base_url ='http://jipiao.kuxun.cn/pek-sha.html?date=2016-10-24{}' 
next_page = "http://jipiao.kuxun.cn/pek-sha.html?date=2016-10-24" #酷讯旅游网站

flight_path = "//div[@class='RcFlightInfo'/p/span[@class='c333']/b/test()]"
fly_time_path = "//div[@class='RcGtTime Verdana']/span/text()"
fly_airport_path = "//div[@class='RcGtPlace']/text()"
land_time_path = "//div[@class='RcGtTime Verdana']/br/text()"
land_airport_path = "//div[@class='RcGtTime Verdana']/br/text()"
low_price_path = "//div[@class='RcSalePrice']/span/span/text()"
next_button_page = "//div[@id='Flip']/span[@class='NextPage']/text()"

while next_page:

      dom = html.parse(next_page)
      headFlights = dom.xpath(flight_path)
      headFly_times = dom.xpath(fly_time_path)
      headFly_airports = dom.xpath(fly_airport_path)
      headLand_times = dom.xpath(land_time_path)
      headLand_airports = dom.xpath(land_airport_path)
      headLow_prices = dom.xpath(low_price_path)

      flights += headFlights
      fly_times += headFly_times
      fly_airports += headFly_airports 
      land_times += headLand_times
      land_airports += headLand_airports
      low_prices += headLow_prices

      next_pages = dom.xpath(next_button_page)
	  
      if next_pages:
           next_page = base_url.format(next_pages[0])
      else:
         print "No next button found"
         next_page = None
      sleep(3)

for flight in flights:
      print flight
	  
for fly_time in fly_times:
      print fly_time
	  
for fly_airport in fly_airports:
      print fly_airport
	  
for land_time in land_times:
      print land_time
	  
for land_airport in land_airports:
      print land_airport
	  
for low_price in low_prices:
      print low_prince
	  
