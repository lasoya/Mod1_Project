# General Analysis of the Film Industry in the 21st Century


# Project Overview

In this project, we pulled data from The Movie Database (TMDB) via API, Rotten Tomatoes via webscraping with BeautifulSoup, and IMDB using their public datasets to understand recent movie trends based on the popularity, genres, and directors of the top movies in the 21st century. Data collected was cleaned and placed into Pandas dataframes before being stored in CSV files throughout the project. The overall data collected was also stored in a relational database. Data visualizations were displayed using Matplotlib, a Python data visualization library.

<u><b> Key Questions for This Project </b></u>
<br>
* What is the optimal time to release a movie?
* A look into customer vs critic
* What kind of movies do viewers want to watch?
* Which directors are trending in the 21st century?


# SQL Database

The SQL database was created using SQlite3 and the information stored in our database were title, director, release date, revenue, writers, Rotten Tomatoes review, number of Rotten Tomatoes reviews, year, genres, average IMDB rating, number of IMDB votes, popularity, average TMDB rating, number of TMDB votes, and release month.


# Data Collection and Wrangling

Datasets from each source (IMDB, Rotten Tomatoes, and TMDB) were collected, cleaned and finalized into individual dataframes before they were merged into a final dataset. Information on the top movies from 2000-2019 were collected from Rotten Tomatoes and used as the subset of data for analysis. Information from IMDB and TMDB were used for more details about each of the top movies. A total of 1900 data points were identified as top movies in the 21st century.

The IMDB dataframe was first merged with the Rotten Tomatoes dataframe before the TMDB dataframe was finally added. The final dataset contained 1202 data points. The decrease in data points was due to duplicates and the lack of information available in IMDB and TMDB for some of the movies. 

The final dataframe was saved as a csv file and in a SQL database.


# Relationship Between Movie Release Timing and Popularity

<p align="center">
  <img src="release_timings.png" title="Monthly Movie Popularity 2000-2018">
</p>

The above bar graph compared the mean popularity of top movies of each month when top movies were released. It showed that movies were more popular in the summer and winter months specifically June, July, November, and December. This is probably because there are more vacations and free time around the summer and winter months.


# Yearly Review of Ratings Between Movie Critics and Consumers

<p align="center">
  <img src="ratings_comp.png" title="Yearly Review of Ratings Between Critics and Consumers 2000-2018">
</p>

The graph above compared the ratings of top movies from movie critics, represented by the Rotten Tomatoes data, to ratings provided by the general populace, represented by the IMDB data. We wanted to analyze how much, if any, critics and consumers differed in their opinions about movies, which may affect the predictions of movie trends. This showed that critics and consumers on many occasions differed in their ratings about the top movies and therefore, it would be important to weigh everyone's thoughts in estimating what would be a successful movie.


# Top Genres Trending in the 21st Century

<p align="center">
  <img src="genres_count.png" title="Top Genres of the 21st Century">
</p>

In looking at what kinds of movies are trending in the recent century, we wanted to take a snapshot of the genres which make up the top movies in this century. The above bar graph looked at the number of top movies from each genre. It showed that most of the top movies were from the Drama category followed by Comedy movies. However, there were many movies that were unclassifed and therefore, it is important to keep in mind that the conclusion was based on only the data available. More information may change the trend and conclusion.


# Top Directors Trending in the 21st Century

<p align="center">
  <img src="directors_counts.png" title="Top 10 Directors of the 21st Century">
</p>

Finally, we wanted to look at who are the directors who created the top films of this century. The above bar graph showed that Steven Spielberg and Clint Eastwood were tied as the directors of the most top movies of this century. Therefore, future movies from either directors would potentially be good options to consider for investment as they are more most likely to succeed based on the trend seen in the past couple of years. 


# Next Steps:

Due to the budget constraints of this project, we were unable to conduct additional analyses for further insights.

Provided with additional resources, we could conduct further analysis to:
<br>
* Assess the correlation between the writers of the film and the revenue generated
* Determine what genre each director specializes in
* Evaluate the revenue per minute of film to determine the size of the scale to consider when making your next movie
