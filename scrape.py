from bs4 import BeautifulSoup
import requests
import lxml 
import pandas as pd 

base_url = "https://en.wikipedia.org/wiki/World_Soccer_(magazine)"

#Sending a request to the web page.
page = requests.get(base_url)

#print(type(page))

if page.status_code == requests.codes.ok:
    #get the whole web page in beautiful soup format 
    soup = BeautifulSoup(page.text, 'lxml')

all_players = soup.find('table', class_='multicol').find('ul').find_all('li')
last_top_10_players = all_players[-10:]

name = [item.find_all('a')[1].text for item in last_top_10_players]

player_data = {
    'Year' : [],
    'Country' : [],
    'Name': name,
    'Team' : [],
}



for player in last_top_10_players:

    #Get the player year and save it to the player_data Dict
    year = player.find('span').previousSibling.split()[0]
    if year:
        player_data['Year'].append(year)
    else:
        player_data['Year'].append('none')

    #Get the player country and save it to the player_data Dict
    country = player.find('span').find('a')['title']
    if country:
        player_data['Country'].append(country)
    else:
        player_data['Country'].append('none')

    #Get the player name and save it to the player_data Dict
    """
    player_name = player.find_all('a')[1].text 
    if player_name:
        player_data['Name'].append(player_name)
    else:
        player_data['Name'].append('none')
    """
    #Get the player team and save it to the player_data Dict
    team = player.find_all('a')[2].text
    if team:
        player_data['Team'].append(team)
    else:
        player_data['Team'].append('none')

players_table = pd.DataFrame(player_data, columns=['Year', 'Country', ' Name', 'Team'])
players_table.index = players_table.index + 1  
print(players_table)
print(name)

print(player_data)
