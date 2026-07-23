import pandas as pd
import numpy as np

movies = pd.read_pickle("data/movie_list.pkl")

movie_ids = movies["movie_id"].tolist()

np.random.seed(42)

ratings = []

num_users = 200

for user in range(1, num_users + 1):

    watched = np.random.choice(
        movie_ids,
        size=np.random.randint(20, 50),
        replace=False
    )

    for movie in watched:

        ratings.append([
            user,
            movie,
            np.random.randint(3, 6)
        ])

ratings_df = pd.DataFrame(
    ratings,
    columns=[
        "userId",
        "movieId",
        "rating"
    ]
)

ratings_df.to_csv(
    "data/ratings.csv",
    index=False
)

print(ratings_df.head())
print("\nRatings generated:", len(ratings_df))