from bs4 import BeautifulSoup
from selenium import webdriver
import lxml
import urllib
import time

url2 = "https://trusculpt.com/find-a-provider"

url3 = "https://play.google.com/store/apps"

# address = input("Enter The adress you want to search: ")

driver = webdriver.Chrome()

driver.get(url3)
# address_box = driver.find_element_by_id('address')
# address_box.send_keys(address)
# search_button = driver.find_element_by_class_name('btn-fad-submit')
# search_button.submit()
time.sleep(5)
response = driver.execute_script("return document.documentElement.outerHTML")

soup = BeautifulSoup(response, "lxml")

apps = soup.find_all("div", class_="WsMG1c nnK0zc")
for app in apps:

    print(app.text)
# print(soup)
physician_office = soup.find("div", class_="physician-office")

# Name = soup.find("p", class_="name")
# print(physician_office)
