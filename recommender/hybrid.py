# Hybrid recommender module
class HybridRecommender:

    def __init__(self,
                 content_model,
                 collaborative_model):

        self.content_model = content_model
        self.collaborative_model = collaborative_model

    def recommend(self,
                  movie_title,
                  movie_id,
                  top_n=10):

        # Content-Based Recommendations
        content_results = self.content_model.recommend(
            movie_title,
            top_n=top_n * 2
        )

        # Collaborative Recommendations
        collaborative_results = self.collaborative_model.recommend(
            movie_id,
            top_n=top_n * 2
        )

        # Convert to dictionaries
        content_scores = {
            movie["movie_id"]: movie
            for movie in content_results
        }

        collaborative_scores = {
            movie["movie_id"]: movie
            for movie in collaborative_results
        }

        all_movie_ids = set(content_scores.keys()) | set(collaborative_scores.keys())

        final_results = []

        for mid in all_movie_ids:

            content_score = content_scores.get(mid, {}).get("score", 0)
            collaborative_score = collaborative_scores.get(mid, {}).get("score", 0)

            hybrid_score = (
                0.6 * content_score +
                0.4 * collaborative_score
            )

            if mid in content_scores:
                movie = content_scores[mid]
            else:
                movie = collaborative_scores[mid]

            movie["score"] = hybrid_score

            final_results.append(movie)

        final_results.sort(
            key=lambda x: x["score"],
            reverse=True
        )

        return final_results[:top_n]