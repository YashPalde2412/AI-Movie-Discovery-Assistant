from recommender.collaborative import CollaborativeRecommender

model = CollaborativeRecommender()

recommendations = model.recommend(19995)

for movie in recommendations:
    print(movie)