from bs4 import BeautifulSoup
from selenium import webdriver
import lxml
import urllib

url2 = "https://trusculpt.com/find-a-provider"

address = input("Enter The adress you want to search: ")

driver = webdriver.Chrome()

driver.get(url2)
response = driver.execute_script("return document.documentElement.outerHTML")
