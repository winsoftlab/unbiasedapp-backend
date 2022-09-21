from selenium import webdriver
from selenium.webdriver.firefox.options import Options

def set_driver_config():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("enable-automation")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument('--incoginito')
    options.add_argument('-lang=en-US')
    driver = webdriver.Firefox(options=options)
    return driver

