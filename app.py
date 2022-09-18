import streamlit as st
import pickle
import requests
import pandas as pd


def movie_poster(movie_id):
    data = requests.get(
        "https://api.themoviedb.org/3/movie/{}?api_key=cb7b7466f7273409d6a65fcbbaf28560&language=en-US".format(
            movie_id))
    data = data.json()
    return "https://image.tmdb.org/t/p/w500/" + data["poster_path"]


def recommend(movie):
    # find the index of the movie given and access similarity[movie_index]
    # sort similarity[i] from highest to lowest similarity
    # need to keep index position even if it's sorted by using enumerate
    # lambda is used so that the sorting is based on the similarity not the index

    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:16]

    recommended_movies_titles = []
    recommended_movies_posters = []
    # get the poster from API
    for i in movies_list:
        movie_id = movies.iloc[i[0]].id
        recommended_movies_titles.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(movie_poster(movie_id))
    return recommended_movies_titles, recommended_movies_posters


movies_dict = pickle.load(open("movie_dict.pkl", "rb"))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open("similarity.pkl", "rb"))
st.title("Movie Ideas")

my_movie = st.selectbox("Enter a movie you like", movies["title"].values)

if st.button("Similar Movies"):
    titles, posters = (recommend(my_movie))
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.image(posters[0])
        st.text(titles[0])
    with col2:
        st.image(posters[1])
        st.text(titles[1])
    with col3:
        st.image(posters[2])
        st.text(titles[2])
    with col4:
        st.image(posters[3])
        st.text(titles[3])
    with col5:
        st.image(posters[4])
        st.text(titles[4])

    col6, col7, col8, col9, col10 = st.columns(5)
    with col6:
        st.image(posters[5])
        st.text(titles[5])
    with col7:
        st.image(posters[6])
        st.text(titles[6])
    with col8:
        st.image(posters[7])
        st.text(titles[7])
    with col9:
        st.image(posters[8])
        st.text(titles[8])
    with col10:
        st.image(posters[9])
        st.text(titles[9])

    col11, col12, col13, col14, col15 = st.columns(5)
    with col11:
        st.image(posters[10])
        st.text(titles[10])
    with col12:
        st.image(posters[11])
        st.text(titles[11])
    with col13:
        st.image(posters[12])
        st.text(titles[12])
    with col14:
        st.image(posters[13])
        st.text(titles[13])
    with col15:
        st.image(posters[14])
        st.text(titles[14])
