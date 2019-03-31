import pandas as pd

### --------------------------- Main Dataset of All Movies --------------------------- ###

# load, read imdb titles tsv file to pandas dataframe and assign to a variable
imdb = pd.read_csv('imdbtitle_akas.tsv', delimiter='\t', dtype=str)

# drop duplicates in dataframe based on titleid
imdb_nodup = imdb.drop_duplicates(subset=['titleId'])

# remove unneeded columns from dataframe
imdb_reduced = imdb_nodup.drop(['isOriginalTitle', 'attributes', 'language', 'ordering', 'types'], axis=1)

# rename titleID column
imdb_reduced = imdb_reduced.rename(columns = {'titleId':'tconst'})

# only movies with region noted as US
imdb_us = imdb_reduced[imdb_nodup['region'] == 'US']

# list of IMDB movie titleID - US only
imdb_us_titleID = imdb_reduced['titleId'].values.tolist()

# list of IMDB movie titleid
imdb_titleID = imdb_reduced['titleId'].values.tolist()

### --------------------------- IMDB Dataset of Movie Ratings --------------------------- ###

# load and read imdb ratings file into a pandas dataframe and assign to a variable
imdb_ratings = pd.read_csv('./imdbtitle_ratings.tsv', delimiter='\t')

### --------------------------- IMDB Dataset of Basic Movie Information --------------------------- ###

# load and read imdb basic movie info dataset into pandas database and assign to a variable
imdb_genres = pd.read_csv('./imdbtitle_basics.tsv', delimiter='\t')

# drop unneeded columns from dataframe
genres_reduced = imdb_genres.drop(['titleType', 'originalTitle', 'isAdult', 'endYear', 'runtimeMinutes'], axis=1)

### --------------------------- IMDB Dataset of Directors to Movies --------------------------- ###

# load and read imdb information of directors to movie titles into pandas dataframe and assign to a variable
imdb_crew = pd.read_csv('./imdbtitle_crew.tsv', delimiter='\t')

# drop writers column from dataframe
imdbmov_directors = imdb_crew.drop(['writers'], axis=1)

# rename directors column in dataframe
directors = imdbmov_directors.rename(columns={'directors': 'nconst'})

### --------------------------- IMDB Dataset of Actors' and Directors' Details  --------------------------- ###

# load and read imdb dataset of actors and directors details to pandas dataframe and assign to variable
imdb_team = pd.read_csv('./imdbname_basics.tsv', delimiter='\t')

# drop unneeded columns from dataframe
imdbteam_names = imdb_team.drop(['birthYear', 'deathYear', 'primaryProfession', 'knownForTitles'], axis=1)

### --------------------------- Join IMDB Datasets  --------------------------- ###

# merge the dataframe with titles, year, genre to dataframe with ratings, number of votes
imdbtitles_ratings_genres = genres_reduced.merge(imdb_ratings, on='tconst')

# merge dataframe with connection between movie title with director ID and dataframe with director names
imdb_directors = directors.merge(imdbteam_names, on='nconst', how='left')

# merge the database with titles, year, ratings to database with director information
imdb_all = imdbtitles_ratings_genres.merge(imdb_directors, on='tconst', how='left')

# rename columns in the dataframe
imdb_all = imdb_all.rename(columns = {'tconst':'movie_ID', 'primaryTitle':'movie_title', 'startYear':'year', 'averageRating':'avg_rating', 'nconst':'directorID', 'primaryName':'director_name'})

