from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from google_sheet_create_class import GoogleSheet
from selenium.common.exceptions import ElementClickInterceptedException

# Filter Input Required
city = input('In which city do you want the apartment for rent-> ')
bhk = input('Enter the BHK you want-> ') + 'BHK'
max_price = input('Enter the Maximum price in X,00,00,000 format-> ')
# bhk = f'{bhk_num}BHK'


# defining Our web driver and setting browser and url setting
Chrome_driver = "../chromedriver.exe"
browser = webdriver.Chrome(executable_path=Chrome_driver)
browser.get(url='https://www.commonfloor.com/')
browser.maximize_window()

# Setting Home tab
home = browser.current_window_handle


# Setting City
time.sleep(3)
city_input = browser.find_element(by=By.XPATH, value='//*[@id="citySuggestInputHomePopup"]')
city_input.send_keys(city)
city_input.click()



# Choosing from drop-down list

time.sleep(2)
drop_down = browser.find_elements(by=By.CSS_SELECTOR, value='.dropdown-menu li')
for i in drop_down:
    if i.text == city.title():
        i.click()


# Selecting Rent Apartments
try:
    time.sleep(3)
    rent_select = browser.find_element(by=By.XPATH, value='//*[@id="browse-links"]/div/div/div[4]/ul/li/h2/a')
    rent_select.click()
except ElementClickInterceptedException:
    browser.quit()
    print('City is not listed in the web-site, Sorry for inconvenience')
    exit()

# Changing to new Tab if Generated
for tab in browser.window_handles:
    if tab != home:
        browser.switch_to.window(tab)

# Selecting BHK For Rent Apartment
bhk_select = browser.find_element(by=By.XPATH, value='//*[@id="bed_rooms"]')
bhk_select.click()
bhk_drop_down = browser.find_elements(by=By.CSS_SELECTOR, value='#multicheck_filter li')
for i in bhk_drop_down:
    if i.text == bhk:
        i.click()
browser.find_element(by=By.XPATH, value='//*[@id="bed_rooms"]')

# Selecting Price
time.sleep(2)
browser.find_element(by=By.XPATH, value='//*[@id="allfilter"]/div[1]/div/div[5]/div/button').click()
browser.find_element(by=By.XPATH, value='//*[@id="Maxlist"]').click()
price_list = browser.find_elements(by=By.CSS_SELECTOR, value='#Maxlist option')
for price in price_list:
    if price.text == max_price:
        price.click()
        break

# Sorting the result from low to high
time.sleep(3)
sorting_list = browser.find_element(by=By.XPATH, value='//*[@id="sortByLabel"]')
sorting_list.click()
selecting_the_sort = browser.find_elements(by=By.CSS_SELECTOR, value='#sortBy li')
for i in selecting_the_sort:
    if i.text == 'Price (Low to High)':
        i.click()
        break


# Gathering the Name of the resident and storing it in a list
time.sleep(4)
resident_name = []
gathering_name = browser.find_elements(by=By.CSS_SELECTOR, value='.img-wrap')
for data in gathering_name:
    resident_name.append(data.get_attribute('title'))

if len(resident_name) == 0:
    print('No Apartment is Available with Current Filters')
    browser.quit()
    exit()

# Gathering the Price of the resident and storing it in a list
time.sleep(3)
resident_price = []
gathering_price = browser.find_elements(by=By.CSS_SELECTOR, value='.s_p')
for data in gathering_price:
    resident_price.append(data.text)


# Gathering links to the apartment
time.sleep(1)
links = []
link_data = browser.find_elements(by=By.CSS_SELECTOR, value='.st_title h2 a')
for data in link_data:
    links.append(data.get_attribute('href'))
print(resident_name)
print(resident_price)
print(links)

browser.quit()

# Creating Google Sheet Object
my_sheet = GoogleSheet(name_list=resident_name, price_list=resident_price, link_list=links)
my_sheet.create_sheet()
