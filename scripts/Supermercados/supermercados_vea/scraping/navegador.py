from selenium import webdriver
from selenium.webdriver.firefox.options import Options

def crear_driver():
    options = Options()
    options.add_argument("--headless")
    return webdriver.Firefox(options=options)
