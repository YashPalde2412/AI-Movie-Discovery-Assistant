"""
content_based.py

Content-Based Movie Recommendation Engine

Author: Yash Palde
Project: AI Movie Discovery Assistant
"""

from pathlib import Path
from typing import List

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class ContentBasedRecommender:
    """
    Content-based recommender using TF-IDF + On-Demand Cosine Similarity.
    """

    def __init__(self, data_path: str):

        self.data_path = Path(data_path)

        self.movies = None
        self.vectorizer = None
        self.tfidf_matrix = None

        self._load_data()
        self._build_tfidf()

    def _load_data(self):

        self.movies = pd.read_pickle(self.data_path)

        self.movies.fillna("", inplace=True)

        required_columns = [
            "movie_id",
            "title",
            "Concatenate"
        ]

        for column in required_columns:
            if column not in self.movies.columns:
                raise ValueError(f"Missing column: {column}")

    def _build_tfidf(self):

        self.vectorizer = TfidfVectorizer(
            stop_words="english",
            max_features=5000
        )

        self.tfidf_matrix = self.vectorizer.fit_transform(
            self.movies["Concatenate"]
        )

    def get_all_titles(self) -> List[str]:

        return sorted(self.movies["title"].tolist())

    def recommend(
        self,
        movie_title: str,
        top_n: int = 5
    ) -> List[dict]:

        if movie_title not in self.movies["title"].values:
            return []

        movie_index = self.movies[
            self.movies["title"] == movie_title
        ].index[0]

        # Compute similarity only for the selected movie
        similarity_scores = cosine_similarity(
            self.tfidf_matrix[movie_index],
            self.tfidf_matrix
        ).flatten()

        similarity_scores = list(
            enumerate(similarity_scores)
        )

        similarity_scores = sorted(
            similarity_scores,
            key=lambda x: x[1],
            reverse=True
        )

        recommendations = []

        for index, score in similarity_scores[1: top_n + 1]:

            movie = self.movies.iloc[index]

            recommendations.append(
                {
                    "movie_id": movie["movie_id"],
                    "title": movie["title"],
                    "score": round(float(score), 3)
                }
            )

        return recommendations