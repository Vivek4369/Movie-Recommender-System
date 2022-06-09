# Movie-Recommender-System

This project is based on a content based movie recommendation system.
It recommends 5 movies similar to a movie you have watched. I have used “TMDB 500 Movie Dataset” for this recommendation system.


Following python libraries are used in this project :
numpy 
pandas
sklearn.feature_extraction.text -> countVectorizer
sklearn.metrics.pairwise - > CosineSimilarity

For the algorithm part , I have taken certain columns like ‘title’ , ‘genre’ , ‘overview’ from the dataset and combined them into a new set.
Then I have used the python module - ‘countVectorizer’ to convert text into vector form. Then I am measuring similarity between two vectors using ‘Cosine Similarity’ . At the end we got the recommender system which recommends 5 similar movies.






'app.py' consist the code for website deployment.
For website deployment I have used Pycharm IDE in which I am using 'streamlit' python library to build the webpage.
I have fetched posters for movies from 'IMDB API'.

For deploying I have used ‘heroku’ which is a cloud Application platform.

You can access the website from : 
https://mrs-vivek.herokuapp.com/
