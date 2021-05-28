from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import datetime
#capturing time when the program is going to be executed
currentDT = datetime.datetime.now()
time = str(currentDT)
#placing the target url in a variable
my_url = 'https://www.flipkart.com/search?q=laptops&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&p%5B%5D=facets.price_range.from%3DMin&p%5B%5D=facets.price_range.to%3D70000&p%5B%5D=facets.serviceability%5B%5D%3Dtrue&p%5B%5D=facets.processor%255B%255D%3DCore%2Bi7'
#using urlopen function as uReq
uClient= uReq(my_url)
#storing the html code in a variable
page_html = uClient.read()
#closing the url
uClient.close()
#parsing the html data using an html parser
page_soup = soup(page_html,'html.parser')
#finding all items containing information about the laptop and storing it as a list
containers=page_soup.findAll("div",{"class":"bhgxx2 col-12-12"})
#creating a file
filename="laptops.csv"
#opening the csv file
f = open(filename, "w")
#setting headers for our spreadsheet
headers = "Laptop, Price \n"
clock = "Performed scraping at " + time + "\n"
f.write(clock)
f.write(headers)
length = len(containers) - 1
print("Performing scraping at " + time + "\n")
#for loop to extract data from all items from the list containers
for i in range(2,length):
	container = containers[i]
	title = container.findAll("div",{"class":"_3wU53n"})
	title_name = title[0].text
	specify =container.findAll("li",{"class":"tVe95H"})
	price= container.findAll("div",{"class":"_1vC4OE _2rQ-NK"})
	cost = price[0].text
	print(title_name)
	for speci in specify:
		print(speci.text)
	print(cost)
	print("\n")
	f.write(title_name.replace(",","|") + "," + cost.replace(",","")+ "\n")
	
f.close()
	
	
