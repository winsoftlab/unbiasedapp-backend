#!C:/bin
from selenium.webdriver.common.by import By
from app.controllers.Ecommerce.driverConfig import set_driver_config
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#from waitress import serve
from bs4 import BeautifulSoup

#url = 'https://www.konga.com/product/samsung-galaxy-a03-core-6-5-32gb-rom-2gb-ram-dual-sim-4g-lte-5000mah-black-5577143'

def begin_konga_search(url):
    """Takes the url of the product review page and recursively get the review"""
    driver = set_driver_config() #get the driver from the config 
    driver.get(url)

    driver.find_element(By.LINK_TEXT,'Reviews').click()

    element = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.CLASS_NAME, "cfc8e_RM54f")))
    element_text = driver.page_source

    print('------------------------------------------------------------------')
    print(element_text)

    result = konga_beautiful_soup_search(element_text) #calling the beautifulsoup method to extract the text 
    driver.quit()
    return result

def konga_beautiful_soup_search(resp):

    data_str =""

    soup = BeautifulSoup(resp, 'html.parser')
    for item in soup.findAll("p", class_="a397c_2uBaY"):
        data_str = data_str + item.get_text()
    result = data_str.split('\n')

    return result