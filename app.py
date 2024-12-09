import pickle
import streamlit as st
import pandas as pd
import requests

import requests

def fetch_poster(movie_name):
    api_key = "30df306"  # Replace with your OMDb API key
    url = f"http://www.omdbapi.com/?apikey={api_key}&t={movie_name}"
    
    response = requests.get(url)
    
    if response.status_code == 200:  # Check if the request was successful
        try:
            data = response.json()
            if 'Poster' in data and data['Poster'] != 'N/A':
                return data['Poster']
            else:
                return "https://via.placeholder.com/150"  # Fallback image
        except ValueError:
            return "Error parsing JSON"
    else:
        return f"Error: {response.status_code}"  # Return error status code if not 200
 
    

def recommend(movie):
    movie_index=movies[movies['title']==movie].index[0]
    distances=similarity[movie_index]
    movies_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
    recommend_movies=[]
    recommended_movie_posters = []
    for i in movies_list:
       recommend_movies.append(movies.iloc[i[0]].title)
       recommended_movie_posters.append(fetch_poster(movies.iloc[i[0]].title))
    return recommend_movies,recommended_movie_posters

st.title('Movie Recommender System')
movies = pickle.load(open('movies.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))

movies=pd.DataFrame(movies)

selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movies['title'].values
)

if st.button("Recommend"):
    recommended_movie_names, recommended_movie_posters=recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])
    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])


