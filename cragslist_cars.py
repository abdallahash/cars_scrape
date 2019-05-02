from bs4 import BeautifulSoup
import requests 
import lxml
import pandas as pd 

cars_url = 'https://losangeles.craigslist.org/search/sss?query=cars&sort=rel'

cragslist_page = requests.get(cars_url)
if cragslist_page.status_code == requests.codes.ok:

    soup = BeautifulSoup(cragslist_page.text, "lxml")

cars_posts = soup.find('ul', class_='rows')
all_cars = cars_posts.find_all('li', class_='result-row')

# infor mation of the car in car info are the title and the date 

#---------- Needed Results ---------------------------# 

cragslist_cars_data = {
    'Price' : [],
    'Title' : [],
    'Date' : [],
}

for car in all_cars:
    car_info = car.find('p', class_="result-info")

    car_price = car.find('span', class_="result-price").text
    if car_price:
        cragslist_cars_data['Price'].append(car_price)
    else:
        cragslist_cars_data['Price'].append('None')

    date = car_info.find('time', class_="result-date").text 
    if date:
        cragslist_cars_data['Date'].append(date)
    else:
        cragslist_cars_data['Date'].append("None")

    title = car_info.find('a', class_="result-title hdrlnk").text 
    if title:
        cragslist_cars_data['Title'].append(title)
    else:
        cragslist_cars_data['Title'].append("None")



cars_table = pd.DataFrame(cragslist_cars_data, columns=['Price', 'Title', 'Date'])
cars_table.index = cars_table.index+1
#print(cars_table)

cars_table.to_csv('LA_CL_cars.csv')

