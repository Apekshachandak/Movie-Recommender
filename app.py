import streamlit as st
import pickle
import pandas as pd

# Load data
movies = pickle.load(open('movies.pkl', 'rb'))  # Expecting a DataFrame with at least a 'title' column
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Function to recommend movies
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = []
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies

# Streamlit app
st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
    'What would you like to watch?',
    movies['title'].values
)

if st.button('Recommend Movies'):
    recommendations = recommend(selected_movie_name)
    for movie in recommendations:
        st.write(movie)
