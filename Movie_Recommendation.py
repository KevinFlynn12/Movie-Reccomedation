# used to import machine learning models
import tensorflow as tf
# Used for mathmatic calculation
import numpy as np
# data fram manipulation
import pandas as pd
# used to plot data
import matplotlib as plt
import warnings
import sklearn
from pip._vendor.distlib.compat import raw_input

warnings.filterwarnings('ignore')

# private variables
movie_fileName = 'ml-1m/movies.dat'
rating_fileName = 'ml-1m/ratings.dat'
user_fileName = 'ml-1m/users.dat'
separator = '::'
rating_header = ['UserID', 'MovieID', 'Rating', 'Timestamp']
user_header = ['UserID', 'Gender', 'Age', 'Occupation', 'Zip-code']
movie_header = ['MovieID', 'Title', 'Genres']
print("Loading Info Please Wait")
movies_df = pd.read_csv(movie_fileName, sep=separator, names=movie_header)
ratings_df = pd.read_csv(rating_fileName, sep=separator, names=rating_header)
users_df = pd.read_csv(user_fileName, sep=separator, names=user_header)
print("Done")

def memory_based_collaborative_filtering():
    user_id = raw_input("Please insert user id: ")
    movie = raw_input("Select A Movie: ")
    movie_list = movies_df[['MovieID', 'Title']]
    merged_rating = pd.merge(ratings_df, movie_list, on='MovieID')
    ratings = pd.DataFrame(merged_rating.groupby('Title')['Rating'].mean())
    ratings['number_of_ratings'] = merged_rating.groupby('Title')['Rating'].count()

    movie_matrix = merged_rating.pivot_table(index='UserID', columns='Title', values='Rating')
    ratings.sort_values('number_of_ratings', ascending=False).head(10)
    movie_user_rating = movie_matrix[movie]
    similar_movie = movie_matrix.corrwith(movie_user_rating)
    print(similar_movie)

    
def get_all_watched_movies(userID):
    return None

def find_recommended_movie(movie_matrix, watchedMovie):
    return None


memory_based_collaborative_filtering()
