# from splinter import Browser
# from bs4 import BeautifulSoup as bs
# import time
# from webdriver_manager.chrome import ChromeDriverManager


# def init_browser():
#     executable_path = {"executable_path": ChromeDriverManager().install()}
#     return Browser("chrome", **executable_path, headless=False)

# def scrape():
#   if __name__ == "__main__":
#       browser = init_browser()
#       # houses = {}

#       url = "https://honolulu.craigslist.org/search/hhh?areaAbb=honolulu"
#       browser.visit(url)

#       html = browser.html
#       soup = bs(html, "html.parser")

import requests
from requests import get
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

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
          print("Nothing given. Don't approach!")
        else:
          print(price)
        prices.append(price)
        
        bed = places.span.find('span', class_='housing').text
        print(bed)
        beds.append(bed)
        

        # runtime
        # runtime = container.p.find('span', class_='runtime').text if container.p.find('span', class_='runtime').text else '-'
        # time.append(runtime)

#         #IMDb rating
#         imdb = float(container.strong.text)
#         imdb_ratings.append(imdb)

#         #metascore
#         m_score = container.find('span', class_='metascore').text if container.find('span', class_='metascore') else '-'
#         metascores.append(m_score)

#         #there are two NV containers, grab both of them as they hold both the votes and the grosses
#         nv = container.find_all('span', attrs={'name': 'nv'})
        
#         #filter nv for votes
#         vote = nv[0].text
#         votes.append(vote)
        
#         #filter nv for gross
#         grosses = nv[1].text if len(nv) > 1 else '-'
#         us_gross.append(grosses)

# #pandas dataframe        
# movies = pd.DataFrame({
# 'movie': titles,
# 'year': years,
# 'timeMin': time,
# 'imdb': imdb_ratings,
# 'metascore': metascores,
# 'votes': votes,
# 'us_grossMillions': us_gross,
# })









# # houses = []
# # baths = []
# # beds = []
# # links = []



# # for places in house_div:


#     # houses["prop_price"] = soup.find("div", {"data-testid":"property-price"}).get_text()
#     # houses["link"] = soup.find("a", ).get_text()
#     # houses["beds"] = soup.find("div", attrs={"data-testid":"property-beds"}).get_text()
#     # houses["baths"] = soup.find("div", attrs={"data-testid":"property-baths"}).get_text()

#     # Scrape page into Soup

    
    
                
