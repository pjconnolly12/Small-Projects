import requests
from bs4 import BeautifulSoup
import random

#A random generator for picking a girls name using bs4

page = requests.get('https://www.verywellfamily.com/top-1000-baby-girl-names-2757832')
soup = BeautifulSoup(page.text, 'lxml')

#List of baby names, used the inspect option on the html to see that the list of 1000 girl names was located in an <ol> tag
baby_names_raw = soup.find_all('ol')

#had to remove the tags from the list
baby_name = []
for name in baby_names_raw:
    li = name.find_all('li')
    for node in li:
        baby_name.append(node.text)

#User input to select what last name the girl should have
last_name = input('Enter Last Name Here: ')

#create the full name
girl_name = baby_name[random.randint(0, len(baby_name))] + ' ' + last_name

print(girl_name)