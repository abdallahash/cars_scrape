from bs4 import BeautifulSoup
import urllib 
from selenium import webdriver 
import pandas as pd
import time 
import lxml 
import re 
# drrrr = 'C:\Users\Dell\chromedriver_win32\chromedriver.exe' 
url1 = "https://play.google.com/store/apps" #google play store

url2 = "https://trusculpt.com/find-a-provider"

address = input("Enter The adress you want to data from: ")

driver = webdriver.Chrome()
driver.get(url2)
address_box = driver.find_element_by_id('address')
address_box.send_keys(address)
search_button = driver.find_element_by_class_name('btn-fad-submit')
search_button.submit()
time.sleep(5) 
response = driver.execute_script("return document.documentElement.outerHTML")
# driver.quit() 

soup = BeautifulSoup(response, 'lxml')
# print(soup)

Specialists_list = soup.find_all("div",class_="physician-office")

Specialists_Data = {
    "Name": [],
    "Address": [],
    "City": [],
    "Phone Number":[],
    "Website":[],
}

for specialist in Specialists_list:
    Name = specialist.find("p", class_="name").text 
    Specialists_Data['Name'].append(Name)

    Address = specialist.find("p", class_="address").text
    Specialists_Data['Address'].append(Address)

    City_zip_code = specialist.find("p", class_="city-state-zip").text
    Specialists_Data['City'].append(City_zip_code)

    try: Phone_number = specialist.find("a").text
    except: Phone_number = "None" 
    Specialists_Data['Phone Number'].append(Phone_number)
    
    try: 
        site = specialist.find("p", class_="website").find("a")['href']
        Website = site 
    except:
        Website = "None" 
    Specialists_Data['Website'].append(Website)
    

    print(Name)
    print(Address)
    print(City_zip_code)
    print(Phone_number)     
    print(Website,"\n--------------------------------------------------\n")

Specialists_Tabe = pd.DataFrame(Specialists_Data, columns=['Name','Address','City','Phone Number','Website'])
print(Specialists_Tabe)
Specialists_Tabe.to_csv('Specialist_Data.csv')




# Apps = soup.find_all("div", class_="WsMG1c nnK0zc")

# for app in Apps:
    
#     print(app.text)




