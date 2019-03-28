import json
from selenium import webdriver
import pandas as pd
from bs4 import BeautifulSoup
import requests

reviews = []
titles = []
num_reviews = []
all_data = []

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


#To run the function above to scrape RT for the following years        
years = [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007,
         2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 
         2016, 2017, 2018]

for year in years:
    movie_info(year)

    
#To create pandas dataframe based on the three lists I created    
df = pd.DataFrame(columns = ['Movie Title', 'Review', 'Number of RT Reviews'])
df['Movie Title'] = titles
df['Review'] = reviews
df['Number of RT Reviews'] = num_reviews

#To separate the year from the movie title and make it its own column
df['Year'] = df['Movie Title'].map(lambda x: x[-5:-1])
df['Movie Title'] = df['Movie Title'].map(lambda x: x[:-7])

#To change the data type of the reviews column to numbers for analysis
df['Number of RT Reviews'] = df['Number of RT Reviews'].astype(int)

total_reviews_by_year = df.groupby('Year').sum()['Number of RT Reviews']

#to scrape the individual page of each movie extracted from above for the relevant information
def movie_info(movie):    
    url = 'https://www.rottentomatoes.com/m/' + movie.replace(' ', '_')
    r = requests.get(url)
    c = r.content
    soup = BeautifulSoup(c, 'html.parser')
    director = []
    writer = []
    movies_info = {}
    #To get directors, writers, box office, movie duration, and when it was released in theaters
    info = soup.find_all('div', class_='meta-value')
    
    try:
        for directors in info[2].find_all('a'):
            director.append(directors.text)

        movies_info['Director'] = director

        for writers in info[3].find_all('a'):
            writer.append(writers.text)

        movies_info['Writers'] = writer

        movies_info['Release Date'] = info[4].time.string

        movies_info['Box Office Info'] = info[6].text

        #to get actor information
        actor_info = soup.find_all('section', id='movie-cast')

        all_actors = []
        for name in actor_info[0].find_all('span'):
            all_actors.append(name.string)

        actresses = []
        for names in all_actors[::2]:
            actresses.append(names)
            movies_info['Actors'] = actresses
        return movies_info   
        
        with open("All_Data.json", 'w') as f:
                f.write(str(response.json()))
        
    except:
        pass

#to add all of the information from the movie_info function into a list of dictionaries
for all_movies in movies_search:
    all_data.append(movie_info(all_movies))