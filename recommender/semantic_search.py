from pathlib import Path
from typing import List

import numpy as np
import pandas as pd

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


class SemanticSearch:

    def __init__(
        self,
        data_path="data/movie_list.pkl",
        embedding_path="data/movie_embeddings.npy"
    ):

        self.movies = pd.read_pickle(Path(data_path))

        self.embeddings = np.load(
            Path(embedding_path)
        )

        self.model = SentenceTransformer(
            "all-MiniLM-L6-v2"
        )

    def search(
        self,
        query,
        top_n=5
    ):

        query_embedding = self.model.encode(
            [query],
            convert_to_numpy=True
        )

        similarity = cosine_similarity(
            query_embedding,
            self.embeddings
        )[0]

        indices = similarity.argsort()[::-1][:top_n]

        recommendations = []

        for idx in indices:

            movie = self.movies.iloc[idx]

            recommendations.append(
                {
                    "movie_id": movie["movie_id"],
                    "title": movie["title"],
                    "score": round(float(similarity[idx]), 3)
                }
            )

        return recommendations