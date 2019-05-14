from bs4 import BeautifulSoup
import requests 
import lxml
import pandas as pd 



cars_url_start = 'https://losangeles.craigslist.org/search/sss?query=cars&sort=rel'
next_url = 'https://losangeles.craigslist.org{}'

cragslist_page = requests.get(cars_url_start)
if cragslist_page.status_code == requests.codes.ok:

    soup = BeautifulSoup(cragslist_page.text, "lxml")
else:
    print("request code denied")

cars_posts = soup.find('ul', class_='rows')
#List of all the cars post on craiglist
all_cars_list = cars_posts.find_all('li', class_='result-row')
print(all_cars_list[0])
print("_____________________________________________________\n")


while len(all_cars_list) <= 1000: 
    next_button = str(soup.find('span', class_='buttons').find('a', class_='button next')['href'])
    soup = BeautifulSoup(requests.get(next_url.format(next_button)).text, 'lxml')
    cars_posts = soup.find('ul', class_='rows')
    all_cars = cars_posts.find_all('li', class_='result-row')
    for car in all_cars:
         all_cars_list.append(car)
    print(all_cars[0].find('span', class_='result-price'))
    print(next_button)


# infor mation of the car in car info are the title and the date 

print(next_button)

print(len(all_cars_list))
#---------- Needed Results ---------------------------# 

cragslist_cars_data = {
    'Price' : [],
    'Title' : [],
    'Date' : [],
}

for car in all_cars_list:
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
print(cars_table)

cars_table.to_csv('All_cars_in_LA.csv')
