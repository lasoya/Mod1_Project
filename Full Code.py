import json
from selenium import webdriver
import pandas as pd
from bs4 import BeautifulSoup
import requests

reviews = []
titles = []
num_reviews = []

def movie_info(year):
    url = 'https://www.rottentomatoes.com/top/bestofrt/?year=' + str(year)
    r = requests.get(url)
    c = r.content
    soup = BeautifulSoup(c, 'html.parser')
    
    all_movies = soup.find('div', class_ = 'panel-body content_body allow-overflow')
    
    for movies in all_movies.find_all('a', class_='unstyled articleLink'):
        titles.append(movies.text.split('\n')[1].strip())
    
    for movies in all_movies.find_all('span', class_='tMeterScore'):
        reviews.append(movies.text.split('\xa0')[1])
    
    for movies in all_movies.find_all('td', class_='right hidden-xs'):
        num_reviews.append(movies.text)