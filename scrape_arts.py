from bs4 import BeautifulSoup 
from selenium import webdriver 
import  requests 
import lxml
import numpy as np 
import pandas as pd 
import time 
import re 

def get_random_ua():
    random_ua = ''
    ua_file = 'ua_file.txt'
    try:
        with open(ua_file) as f:
            lines = f.readlines()
        if len(lines) > 0:
            prng = np.random.RandomState()
            index = prng.permutation(len(lines) - 1)
            idx = np.asarray(index, dtype=np.integer)[0]
            random_proxy = lines[int(idx)]
    except Exception as ex:
        print('Exception in random_ua')
        print(str(ex))
    finally:
        return random_ua



url = 'https://www.artsy.net/galleries-a-z' 
page = requests.get(url)

soup = BeautifulSoup(page.content, "lxml")

all_gallaries = soup.find("ul", class_="a-to-z-column")

gallary_list = all_gallaries.find_all("li", class_="a-to-z-item")

contacts_url = "https://www.artsy.net/{}/contact"
artists_genaral = "https://www.artsy.net/{}/artists"

driver = webdriver.Chrome()

pattern = "\w+(?:(?:\.?|\_?|\-?)\w)+@\w(?:(?:\.?|\_?|\-?)\w)+\.[a-zA-z]{2,}"
regex = re.compile(pattern)

Gallery_Data = {
    "Name": [],
    "Email": [],
    "Artists" :[],
} 


for gallary in gallary_list:

    user_agent = get_random_ua()
    headers={'User-Agent': user_agent}
    
    contact_url = contacts_url.format(gallary.a['href'])
    artists_url = artists_genaral.format(gallary.a['href'])

    driver.get(contact_url)
    time.sleep(5)
    contact_page = driver.execute_script("return document.documentElement.outerHTML")

    driver.get(artists_url)
    time.sleep(7)
    artists_page = driver.execute_script("return document.documentElement.outerHTML")
    # time.sleep(10) 

    contact_soup = BeautifulSoup(contact_page, "lxml")
    artists_soup = BeautifulSoup(artists_page, "lxml")
    
    # parsed_tree = lxml.etree.parse(gallary_url)
    # time.sleep(10) 

    # the_path = "//a[@class='email-gallery'][@href]"
    # email = parsed_tree.xpath(the_path)
   
    try:
        Email = contact_soup.find("a", class_="email-gallery")['href']
        # names_html = artists_soup.find_all("a", class_="partner2-route-link")
        artists_columns = artists_soup.find_all('ul', class_="artists-column")
        names_list = []

        for names_column in artists_columns:
            name_column = names_column.find_all('a', class_="partner2-route-link")
            for name in name_column:
                artist = name.text 
                names_list.append(artist)

        match = regex.findall(Email)[0]
        
        gallary_name = gallary.a.text 

        print("Name:",gallary_name,"Email:", match)

        print(names_list)
        Gallery_Data['Name'].append(gallary_name)
        Gallery_Data['Email'].append(match)
        Gallery_Data['Artists'].append(",".join(names_list))
        print(Gallery_Data)
    except:
        pass 

driver.quit() 
# print(gallary_list.prettify())

Galleries_Table = pd.DataFrame(Gallery_Data, columns=['Name', 'Email','Artists'])
Galleries_Table.index = Galleries_Table.index+1

print(Galleries_Table)

Galleries_Table.to_csv('Galleries_Data.csv')




