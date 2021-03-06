# -*- coding: utf-8 -*-
"""Movie-Recommender-System

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1haAZ3KjjB9LSnDtLGL59e0tXgbGlxh9T
"""

import numpy as np
import pandas as pd

#Load both movies dataset
movies = pd.read_csv('tmdb_5000_movies.csv')

movies = movies[['id','title','overview','genres','keywords']]

movies.dropna(inplace=True)

# we have to fix the genres and keywords data
import ast
def convert(text):
    L = []
    for i in ast.literal_eval(text):
        L.append(i['name']) 
    return L

movies['genres'] = movies['genres'].apply(convert)
movies['keywords'] = movies['keywords'].apply(convert)

# removing the space between names or keywords
def collapse(L):
    L1 = []
    for i in L:
        L1.append(i.replace(" ",""))
    return L1

# movies['title'] = movies['title'].apply(collapse)
movies['genres'] = movies['genres'].apply(collapse)
movies['keywords'] = movies['keywords'].apply(collapse)

movies['overview'] = movies['overview'].apply(lambda x:x.split())

movies['tags'] = movies['overview'] + movies['genres'] + movies['keywords']

new = movies.drop(columns=['overview','genres','keywords'])

new['tags'] = new['tags'].apply(lambda x: " ".join(x))

from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features=5000,stop_words='english')
# above line we are removing stop words(i.e, 'to','how')
# and max_features is for maximum words

vector = cv.fit_transform(new['tags']).toarray()

from sklearn.metrics.pairwise import cosine_similarity

similarity = cosine_similarity(vector)

#Recommend Function

def recommend(movie):
    index = new[new['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])),reverse=True,key = lambda x: x[1])
    for i in distances[1:6]:
        print(new.iloc[i[0]].title)

# Now search the movie and it will give 5 recommendations
recommend('Spider-Man')

# This portion of code is to create pkl file of movie sets
# which will be used in building the website for MRS
#import pickle
#pickle.dump(new.to_dict(),open('movie_list.pkl','wb'))
#pickle.dump(similarity,open('similarity.pkl','wb'))