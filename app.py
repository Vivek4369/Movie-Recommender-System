import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
     data = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=a620731438e0f2b4c5281a55e86394ee&language=en-US'.format(movie_id))
     data = data.json()
     return "https://image.tmdb.org/t/p/w300/" + data['poster_path']

def recommend(movie):
     index = movies[movies['title'] == movie].index[0]
     movies_list = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])[1:6]

     recommended_movies = []
     recommended_movies_poster = []
     for i in movies_list:
          movie_id = movies.iloc[i[0]].id
          #fetch poster from API
          recommended_movies.append(movies.iloc[i[0]].title)
          recommended_movies_poster.append(fetch_poster(movie_id))
     return recommended_movies,recommended_movies_poster

movies_dict = pickle.load(open('movie_list.pkl','rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl','rb'))

st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
     'Select Movie',
     movies['title'].values)

if st.button('Recommend'):
     names,posters = recommend(selected_movie_name)
     # for i in range (5):
     #      st.text(names[i])
     #      st.image(posters[i])

     col1, col2, col3, col4, col5 = st.columns(5)
     with col1:
          st.text(names[0])
          st.image(posters[0])
     with col2:
          st.text(names[1])
          st.image(posters[1])

     with col3:
          st.text(names[2])
          st.image(posters[2])
     with col4:
          st.text(names[3])
          st.image(posters[3])
     with col5:
          st.text(names[4])
          st.image(posters[4])
