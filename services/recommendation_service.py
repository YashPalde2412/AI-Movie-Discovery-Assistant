from recommender.content_based import ContentBasedRecommender
from recommender.semantic_search import SemanticSearch
from recommender.collaborative import CollaborativeRecommender
from recommender.hybrid import HybridRecommender
from llm.gemini import GeminiClient
from llm.prompts import SYSTEM_PROMPT


class RecommendationService:

    def __init__(self):
        self.content_model = ContentBasedRecommender("data/movie_list.pkl")
        self.semantic_model = SemanticSearch()
        self.gemini = GeminiClient()

        # Hybrid Models
        self.collaborative_model = CollaborativeRecommender()
        self.hybrid_model = HybridRecommender(
            self.content_model,
            self.collaborative_model
        )

    def get_all_titles(self):
        return self.content_model.get_all_titles()

    # ---------------------------------------------------------
    # Content-Based Recommendation
    # ---------------------------------------------------------
    def recommend_by_movie(self, movie_name, top_n=5):
        return self.content_model.recommend(movie_name, top_n)

    # ---------------------------------------------------------
    # Semantic Search + Gemini
    # ---------------------------------------------------------
    def recommend_by_prompt(self, prompt, top_n=5):

        movies = self.semantic_model.search(prompt, top_n)

        movie_list = ""

        for movie in movies:
            movie_list += f"- {movie['title']}\n"

        final_prompt = f"""
{SYSTEM_PROMPT}

User Request:
{prompt}

Available Movies:
{movie_list}

Recommend the best movies and explain why they fit.
"""

        explanation = self.gemini.generate(final_prompt)

        return {
            "movies": movies,
            "ai_response": explanation
        }

    # ---------------------------------------------------------
    # Hybrid Recommendation
    # ---------------------------------------------------------
    def recommend_hybrid(self, movie_title, top_n=10):

        movie = self.content_model.movies[
            self.content_model.movies["title"] == movie_title
        ]

        if movie.empty:
            return []

        movie_id = movie.iloc[0]["movie_id"]

        return self.hybrid_model.recommend(
            movie_title,
            movie_id,
            top_n
        )