from pathlib import Path

import numpy as np
import pandas as pd
from sentence_transformers import SentenceTransformer

print("=" * 50)
print("Building Movie Embeddings...")
print("=" * 50)

DATA_PATH = Path("data/movie_list.pkl")
OUTPUT_PATH = Path("data/movie_embeddings.npy")

movies = pd.read_pickle(DATA_PATH)

model = SentenceTransformer("all-MiniLM-L6-v2")

embeddings = model.encode(
    movies["Concatenate"].tolist(),
    show_progress_bar=True,
    convert_to_numpy=True
)

np.save(OUTPUT_PATH, embeddings)

print("\n✅ Embeddings saved successfully!")
print(f"Location: {OUTPUT_PATH}")
print(f"Shape: {embeddings.shape}")