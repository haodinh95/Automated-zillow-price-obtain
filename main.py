# beautiful soup to scrape all the listing
from bs4 import BeautifulSoup
import requests
from get_data import Get_data
import lxml
import random
from fill_the_form import SELENIUM

hrf_class = "list-card-link list-card-link-top-margin"
address_class = "list-card-addr"
price_class = "list-card-price"
link = 'https://www.zillow.com/guelph-on/rentals/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%22Guelph%2C%20ON%22%2C%22mapBounds%22%3A%7B%22west%22%3A-80.44101181103515%2C%22east%22%3A-80.03932418896484%2C%22south%22%3A43.43050708565053%2C%22north%22%3A43.63808604708041%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A792670%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Afalse%2C%22filterState%22%3A%7B%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22mp%22%3A%7B%22max%22%3A2200%7D%2C%22price%22%3A%7B%22max%22%3A487833%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D'
x_path_1 = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input'
x_path_2 = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input'
x_path_3 = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input'

get_data = Get_data(link)
soup = get_data.get_htmldata()

all_href_links_data = soup.find_all("a", attrs={"class": [hrf_class]}, href=True)
all_href_links = get_data.get_href(all_href_links_data)
print(all_href_links)

all_address_links_data = soup.find_all("address", attrs={"class": [address_class]})
all_addresses = get_data.get_text(all_address_links_data)
print(all_addresses)

price_data = soup.find_all("div", attrs={"class": [price_class]})
all_prices = get_data.get_text(price_data)
print(all_prices)

selenium = SELENIUM()
for i in range(0, len(all_prices)):
    selenium.form_input(x_path_1, all_addresses[i])
    selenium.form_input(x_path_2, all_prices[i])
    selenium.form_input(x_path_3, all_href_links[i])
    selenium.send_form()
    selenium.back_to_form()
selenium.quit()

# use selenium to fill in the form
