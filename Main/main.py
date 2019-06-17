import pandas as pd 
import requests as requests
from bs4 import BeautifulSoup

page = requests.get('https://www.wetter.de/deutschland/wetter-aachen-18220677.html')
soup =  BeautifulSoup(page.content,'html.parser')

week = soup.find(class_ = 'large-8 small-12')


items = week.find_all(class_ = 'forecast-item-day')


days = [item.find(class_ = 'forecast-item-day').get_text() for item in items]
dates =[item.find(class_ = 'text-day').get_text() for item in items]
tem_max = [item.find(class_ = 'wt-color-temperature-max').get_text() for item in items]
tem_min = [item.find(class_ = 'wt-color-temperature-min').get_text() for item in items]
txt = [item.find(class_ = 'forecast-day-text').get_text() for item in items]

print(days)