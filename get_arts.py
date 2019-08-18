from bs4 import BeautifulSoup
import urllib 
from selenium import webdriver 
import lxml 
import re 
# drrrr = 'C:\Users\Dell\chromedriver_win32\chromedriver.exe' 
driver = webdriver.Chrome()
driver.get("https://play.google.com/store/apps")
response = driver.execute_script("return document.documentElement.outerHTML")
# driver.quit() 

soup = BeautifulSoup(response, 'lxml')
Apps = soup.find_all("div", class_="WsMG1c nnK0zc")

# pattern = "\w+(?:(?:\.?|\_?|\-?)\w)+@\w(?:(?:\.?|\_?|\-?)\w)+\.[a-zA-z]{2,}"
# regex = re.compile(pattern)
# match = regex.findall(Email)
for app in Apps:
    
    print(app.text)

