# from splinter import Browser
# from bs4 import BeautifulSoup as bs
# from webdriver_manager.chrome import ChromeDriverManager
# from requests import get
# import pandas as pd
# import numpy as np
# import requests

# from time import sleep
# from random import randint

# def init_browser():
#     executable_path = {"executable_path": ChromeDriverManager().install()}
#     return Browser("chrome", **executable_path, headless=False)

# # def scrape():
# # if __name__ == "__main__":
# #     browser = init_browser()
# #     houses = {}

# #     url = "https://www.trulia.com/for_rent/San_Diego,CA/"
# #     browser.visit(url)

# #     pages = np.arange(1, 1001, 50)

# url = "https://www.trulia.com/for_rent/San_Diego,CA/"
# headers = {"Accept-Language": "en-US, en;q=0.5"}
# results = requests.get(url, headers=headers)

# pages = np.arange(1, 40, 20)

# for page in pages: 
  
#   page = requests.get("https://www.trulia.com/for_rent/San_Diego,CA/" + str(page) + "_p/", headers=headers)
  
#   soup = bs(page.text, 'html.parser')
  
#   house_div = soup.find_all('div', class_='Grid__GridContainer-sc-5ig2n4-1 eVbKXM')
  
#   sleep(randint(2,10))

# # html = browser.html
# # soup = bs(html, "html.parser")

# houses = []
# baths = []
# beds = []
# links = []

# i += 
# house_div = soup.find_all('div', attrs={"data-testid":"home-card-{i}"}) #class_="Box-sc-8ox7qa-0 jDcCbK PropertyCard__PropertyCardContainer-sc-1ush98q-2 hQvvnw")

# for places in house_div:


#     # houses["prop_price"] = soup.find("div", {"data-testid":"property-price"}).get_text()
#     # houses["link"] = soup.find("a", ).get_text()
#     # houses["beds"] = soup.find("div", attrs={"data-testid":"property-beds"}).get_text()
#     # houses["baths"] = soup.find("div", attrs={"data-testid":"property-baths"}).get_text()

#     # bed = places.find('div', {"data-testid": "property-baths"}).text
#     # <div data-testid="property-beds" class="Text__TextBase-sc-1i9uasc-0-div Text__TextContainerBase-sc-1i9uasc-1 SSeMC">1bd</div>
#     bed = places.find('div', attrs={"data-testid":"property-beds"}).get_text()
#     print(bed)
#     # beds.append(bed)

# # print(beds)

# #     links = soup.find_all('a')
# #     for link in links:
# #         if link.has_attr('href'):
# #             if(link.attrs['href'][0:5]=="/c/ca"):
# #                 print(link.attrs['href'])


# #     bathrooms = soup.find_all("div", {"data-testid": "property-baths"})
# #     for bath in bathrooms:
# #         if bath.get_text().find("1-2ba") >= 0:
# #                 print(bath.get_text())

# #     bedrooms = soup.find_all("div", {"data-testid": "property-beds"})
# #     for bed in bedrooms:
# #         if bed.get_text().find("1-2bd") >= 0:
# #                 print(bed.get_text())

# #     # for house in houses

# # # house = 
# # # houses = soup.find_all("div", {"data-testid" : "srp-home-card-{house}"})
# # # print(houses)
# #         # if houses[0].get_text().find("1-3ba") >= 0:
# #         #     print(houses[0].get_text())
# #         # print(house[0])



# #     # bedrooms = soup.find_all("div", {"data-testid": "property-beds"})
# #     # links = soup.find_all('a')
# #     # for bed in bedrooms:
# #     #     if bed.get_text().find("1-3bd") >= 0:
# #     #         print(bath.get_text())
# #     #         for link in links:
# #     #             if link.has_attr('href'):
# #     #                 if(link.attrs['href'][0:5]=="/c/ca"):
# #     #                     print(link.attrs['href'])

# # # for number in num_list:
# # #     print(number)
# # #         for letter in alpha_list:
# # #             print(letter)
    

#     # def scrape():
# #   if __name__ == "__main__":
# #       browser = init_browser()
# #       # houses = {}

# #       url = "https://honolulu.craigslist.org/search/hhh?areaAbb=honolulu"
# #       browser.visit(url)

# #       html = browser.html
# #       soup = bs(html, "html.parser")


#========================================================

import requests
from requests import get
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

def init_browser():
    executable_path = {"executable_path": ChromeDriverManager().install()}
    return Browser("chrome", **executable_path, headless=False)

url = "https://honolulu.craigslist.org/search/hhh?areaAbb=honolulu"
headers = {"Accept-Language": "en-US, en;q=0.5"}
results = requests.get(url, headers=headers)

soup = BeautifulSoup(results.text, "html.parser")

#initiate data storage
prices = []
beds = []
baths = []

house_div = soup.find_all('li', class_='result-row')

#our loop through each container
for places in house_div:

        # #name
        # beds = places.h3.a.text
        # titles.append(name)
        
        #year
        price = places.find('span', class_='result-price').text
        if price == "$0":
          print("$0")
        else:
          print(price)
        prices.append(price)

        loc = places.span.find('span', class_='result-hood')
        print(loc)
        
        bed = places.div.find('span', class_='housing')
        print(bed)
        # txt = bed

        # x = txt.split()

        # print(x)    
        # print(bed.find("1br"))

        # if word in list_of_words:
        #   print 'success'
        
        
        # if "2br" in bed: 
        #   print('2br')
        # else:
        #   print(" ")
        # # print(bed)
        # beds.append(bed)
                
