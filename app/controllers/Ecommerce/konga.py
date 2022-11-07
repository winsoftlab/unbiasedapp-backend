#!C:/bin
from selenium.webdriver.common.by import By
from app.errors.handlers import internal_server_error
from app.controllers.Ecommerce.driver_config import set_driver_config
from bs4 import BeautifulSoup
import time

# url = 'https://www.konga.com/product/samsung-galaxy-a03-core-6-5-32gb-rom-2gb-ram-dual-sim-4g-lte-5000mah-black-5577143'
def begin_konga_search(url):
    """Takes the url of the product review page and recursively get the review"""
    driver = set_driver_config()  # get the driver from the config
    driver.get(url)

    time.sleep(1)

    driver.find_element(By.XPATH, "// h3[contains(text(),'Reviews')]").click()

    element_text = driver.page_source

    result = konga_beautiful_soup_search(
        element_text
    )  # calling the beautifulsoup method to extract the text
    driver.quit()
    return result


def konga_beautiful_soup_search(resp):

    data_str = ""

    soup = BeautifulSoup(resp, "html.parser")
    for item in soup.findAll("p", class_="a397c_2uBaY"):
        data_str = data_str + item.get_text() + "\n"
    result = data_str.split("\n")

    return result
