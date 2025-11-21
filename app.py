import pickle
import streamlit as st
import requests
import pandas as pd

# Load the processed data and similarity matrix
movies = pickle.load(open('Internship_Project/movie_list.pkl', 'rb'))
similarity = pickle.load(open('Internship_Project/similarity.pkl', 'rb'))

# Function to get movie recommendations
def get_recommendations(title, cosine_sim=similarity):
    idx = movies[movies['title'] == title].index[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:6]  # Get top 5 similar movies
    movie_indices = [i[0] for i in sim_scores]
    return movies[['title', 'movie_id']].iloc[movie_indices]

# Fetch movie poster from TMDB API
def fetch_poster(movie_id):
    api_key = '233d375f0465870c2fa43bd8290fe4ed'  # Replace with your TMDB API key
    url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}'
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
        if 'poster_path' in data and data['poster_path']:
            poster_path = data['poster_path']
            return f"https://image.tmdb.org/t/p/w500{poster_path}"
        else:
            return "https://via.placeholder.com/500x750?text=No+Image+Available"
    except requests.exceptions.RequestException as e:
        print(f"Error fetching poster for movie ID {movie_id}: {e}")
        return "https://via.placeholder.com/500x750?text=No+Image+Available"

# Streamlit UI
st.title("Movie Recommendation System")

# Dropdown for selecting a movie
selected_movie = st.selectbox("Select a movie:", movies['title'].values)

# Button to show recommendations
if st.button('Recommend'):
    recommendations = get_recommendations(selected_movie)
    st.write("Top 5 recommended movies:")

    # Create a 1x5 grid layout
    cols = st.columns(5)
    for i, col in enumerate(cols):
        if i < len(recommendations):
            movie_title = recommendations.iloc[i]['title']
            movie_id = recommendations.iloc[i]['movie_id']
            poster_url = fetch_poster(movie_id)
            with col:
                st.image(poster_url, width=130)
                st.write(movie_title)
