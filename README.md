# AI Movie Discovery Assistant

# 🎬 AI Movie Discovery Assistant

An AI-powered Movie Recommendation System built using **Machine Learning**, **Semantic Search**, and **Google Gemini AI**. The application helps users discover movies through content similarity, natural language queries, and hybrid recommendations while displaying real-time movie information from TMDB.

---

## 📸 Project Preview

> Add screenshots here after deployment.

| Home | AI Search | Hybrid Recommendation |
|------|-----------|----------------------|
| Add Screenshot | Add Screenshot | Add Screenshot |

---

# 🚀 Features

### 🎬 Content-Based Recommendation
- Recommends similar movies using **TF-IDF Vectorization** and **Cosine Similarity**.
- Finds movies with similar genres, cast, keywords, directors, and plot.

### 🤖 AI Semantic Search
- Search movies using natural language.
- Example:
  - "I want an emotional sci-fi movie."
  - "Recommend a funny family movie."
  - "Mind-bending psychological thriller."

- Uses **Sentence Transformers** for semantic understanding.

### ✨ Gemini AI Recommendations
- Integrates **Google Gemini API**.
- Generates human-like explanations for recommended movies.
- Explains why each recommendation matches the user's query.

### 🧠 Hybrid Recommendation
Combines:

- Content-Based Recommendation
- Collaborative Filtering

to improve recommendation quality.

### 🎥 TMDB Integration
Displays:

- Movie Poster
- Overview
- Rating
- Genres
- Release Date

using the TMDB API.

---

# 🏗️ System Architecture

```
                User
                  │
                  ▼
          Streamlit Interface
                  │
      ┌───────────┼───────────┐
      ▼           ▼           ▼
Content      Semantic      Hybrid
Filtering     Search    Recommendation
      │           │           │
      └──────┬────┴───────────┘
             ▼
        Gemini AI
             │
             ▼
    AI Generated Explanation
             │
             ▼
     TMDB Movie Information
             │
             ▼
        Final Recommendation
```

---

# 📂 Project Structure

```
AI-Movie-Discovery/
│
├── app.py
├── requirements.txt
├── README.md
├── .env
│
├── data/
│   ├── movie_list.pkl
│   ├── movie_embeddings.npy
│   └── ratings.csv
│
├── recommender/
│   ├── content_based.py
│   ├── semantic_search.py
│   ├── collaborative.py
│   └── hybrid.py
│
├── llm/
│   ├── gemini.py
│   └── prompts.py
│
├── services/
│   └── recommendation_service.py
│
└── utils/
    └── fetch_posters.py
```

---

# 🛠️ Technologies Used

## Programming Language
- Python

## Frontend
- Streamlit

## Machine Learning
- Scikit-learn
- TF-IDF Vectorizer
- Cosine Similarity

## NLP

- Sentence Transformers
- all-MiniLM-L6-v2

## LLM

- Google Gemini API

## Data Processing

- Pandas
- NumPy

## APIs

- TMDB API

---

# 📊 Machine Learning Pipeline

```
Movie Dataset
      │
      ▼
Feature Engineering
      │
      ▼
TF-IDF Vectorization
      │
      ▼
Cosine Similarity
      │
      ▼
Content Recommendation
```

---

# 🤖 AI Search Pipeline

```
User Query
      │
      ▼
Sentence Transformer
      │
      ▼
Semantic Embeddings
      │
      ▼
Semantic Similarity
      │
      ▼
Relevant Movies
      │
      ▼
Gemini AI Explanation
```

---

# 🧠 Hybrid Recommendation Pipeline

```
Movie
   │
   ├───────────────┐
   ▼               ▼
Content       Collaborative
Filtering        Filtering
   │               │
   └──────┬────────┘
          ▼
 Weighted Hybrid Score
          ▼
 Final Recommendation
```

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/AI-Movie-Discovery.git

cd AI-Movie-Discovery
```

---

## Create Virtual Environment

### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

### Linux / Mac

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Create .env File

```env
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
TMDB_API_KEY=YOUR_TMDB_API_KEY
```

---

## Run Application

```bash
streamlit run app.py
```

---

# 📈 Future Improvements

- User authentication
- Personalized user profiles
- Watchlist management
- Movie trailers
- Actor recommendations
- Movie sentiment analysis
- Cloud deployment
- Real-time trending movies

---

# 📌 Notes

The project uses the **TMDB 5000 Movies Dataset** for movie metadata.

Since the TMDB dataset does not contain individual user ratings, a **synthetic ratings dataset** was generated to demonstrate the collaborative filtering component used in the hybrid recommendation system.

---

# 🎯 Learning Outcomes

This project demonstrates practical implementation of:

- Machine Learning
- Recommendation Systems
- Information Retrieval
- Semantic Search
- Large Language Models (LLMs)
- Prompt Engineering
- API Integration
- Streamlit Application Development
- Modular Python Programming

---

# 👨‍💻 Author

**Yash Palde**

Final Year Information Technology Student

Interested in:

- Artificial Intelligence
- Machine Learning
- Generative AI
- LLM Applications
- Data Science

---

## ⭐ If you like this project

Please consider giving it a **Star ⭐** on GitHub.