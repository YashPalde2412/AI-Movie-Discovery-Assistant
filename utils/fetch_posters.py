# TMDB poster utilities
import requests

# ----------------------------
# Replace with your TMDB API Key
# ----------------------------
TMDB_API_KEY = "b1941392dd680e11ec44f9f17c356f63"

from functools import lru_cache
@lru_cache(maxsize=1000)

def get_movie_details(movie_id: int):
    """
    Fetch movie details from TMDB.
    """

    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={TMDB_API_KEY}"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException:
        return None

    if response.status_code != 200:
        return None

    movie = response.json()

    poster = ""

    if movie.get("poster_path"):
        poster = (
            "https://image.tmdb.org/t/p/w500"
            + movie["poster_path"]
        )

    genres = ", ".join(
        [genre["name"] for genre in movie.get("genres", [])]
    )

    return {
        "poster": poster,
        "overview": movie.get("overview", "Not Available"),
        "rating": movie.get("vote_average", "N/A"),
        "release_date": movie.get("release_date", "N/A"),
        "genres": genres
    }