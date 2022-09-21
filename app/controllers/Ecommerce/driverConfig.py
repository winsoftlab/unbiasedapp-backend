from config import Config
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

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
    driver = webdriver.Firefox(options=options, executable_path=Config.GECKODRIVER_PATH,firefox_binary=FirefoxBinary(Config.FIREFOX_BIN))
    return driver

#, 