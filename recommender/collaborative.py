# Collaborative filtering module
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity


class CollaborativeRecommender:

    def __init__(self,
                 ratings_path="data/ratings.csv",
                 movies_path="data/movie_list.pkl"):

        self.ratings = pd.read_csv(ratings_path)
        self.movies = pd.read_pickle(movies_path)

        # User-Movie Rating Matrix
        self.user_movie_matrix = self.ratings.pivot_table(
            index="userId",
            columns="movieId",
            values="rating"
        ).fillna(0)

        # Movie-Movie Similarity Matrix
        self.movie_similarity = cosine_similarity(
            self.user_movie_matrix.T
        )

        self.movie_ids = self.user_movie_matrix.columns.tolist()

    def recommend(self, movie_id, top_n=10):

        if movie_id not in self.movie_ids:
            return []

        idx = self.movie_ids.index(movie_id)

        similarity_scores = list(
            enumerate(self.movie_similarity[idx])
        )

        similarity_scores = sorted(
            similarity_scores,
            key=lambda x: x[1],
            reverse=True
        )[1:top_n + 1]

        recommendations = []

        for index, score in similarity_scores:

            mid = self.movie_ids[index]

            movie = self.movies[
                self.movies["movie_id"] == mid
            ]

            if len(movie):

                recommendations.append({
                    "movie_id": mid,
                    "title": movie.iloc[0]["title"],
                    "score": float(score)
                })

        return recommendations