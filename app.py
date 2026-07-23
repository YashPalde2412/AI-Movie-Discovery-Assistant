import streamlit as st

from services.recommendation_service import RecommendationService
from utils.fetch_posters import get_movie_details

# -------------------------------------------------------
# Page Config
# -------------------------------------------------------

st.set_page_config(
    page_title="AI Movie Discovery Assistant",
    page_icon="🎬",
    layout="wide"
)

# -------------------------------------------------------
# Load Models
# -------------------------------------------------------

@st.cache_resource
def load_content_model():
    return ContentBasedRecommender(
        "data/movie_list.pkl"
    )


@st.cache_resource
def load_semantic_model():
    return SemanticSearch()


@st.cache_resource
def load_service():
    return RecommendationService()

service = load_service()

# -------------------------------------------------------
# Sidebar
# -------------------------------------------------------

st.sidebar.title("🎬 AI Movie Discovery")

mode = st.sidebar.radio(
    "Recommendation Mode",
    [
        "🎬 Similar Movie",
        " Hybrid AI",
        "🤖 AI Search"
    ]
)

st.sidebar.markdown("---")

st.sidebar.success("AI Features")

st.sidebar.write("✅ Content-Based Recommendation")
st.sidebar.write("✅ Semantic Search")
st.sidebar.write("✅ Hybrid(Content Based + Collaborative)")

# -------------------------------------------------------
# Title
# -------------------------------------------------------

st.title("🎬 AI Movie Discovery Assistant")

st.write(
    "Discover movies using AI."
)

st.divider()

# =======================================================
# MOVIE BASED MODE
# =======================================================

if mode == "🎬 Similar Movie":

    movie_titles = service.get_all_titles()

    selected_movie = st.selectbox(
        "Choose a Movie",
        movie_titles
    )

    if st.button(
        "Recommend",
        use_container_width=True
    ):

        with st.spinner("Finding recommendations..."):

            recommendations = service.recommend_by_movie(
                selected_movie
            )

        cols = st.columns(len(recommendations))

        for col, movie in zip(cols, recommendations):

            details = get_movie_details(
                movie["movie_id"]
            )

            with col:

                if details:

                    if details["poster"]:

                        st.image(
                            details["poster"],
                            use_container_width=True
                        )

                    st.markdown(
                        f"### {movie['title']}"
                    )

                    st.metric(
                        "Similarity",
                        movie["similarity"]
                    )

                    st.write(
                        f"⭐ {details['rating']}"
                    )

                    st.write(
                        details["genres"]
                    )

                else:

                    st.write(movie["title"])


elif mode == "Hybrid AI":

    movie = st.selectbox(
        "Choose a movie",
        service.get_all_titles()
    )

    if st.button("Recommend"):

        recommendations = service.recommend_hybrid(movie)

        cols = st.columns(5)

        for idx, recommendation in enumerate(recommendations):

            details = get_movie_details(
                recommendation["movie_id"]
            )

            with cols[idx % 5]:

                if details and details["poster"]:
                    st.image(details["poster"])

                st.markdown(
                    f"**{recommendation['title']}**"
                )

                st.caption(
                    f"Hybrid Score: {recommendation['score']:.2f}"
                )
# =======================================================
# SEMANTIC SEARCH MODE
# =======================================================

else:

    query = st.text_area(
        "Describe the movie you want",
        placeholder="Example:\nI want a mind-bending sci-fi movie with emotional storytelling."
    )

    if st.button(
        "Search",
        use_container_width=True
    ):

        if query.strip() == "":

            st.warning(
                "Please enter a description."
            )

        else:

            with st.spinner(
                "AI is understanding your request..."
            ):

                
                result = service.recommend_by_prompt(query)

                recommendations = result["movies"]

                ai_response = result["ai_response"]

            st.subheader("🤖 AI Recommendation")
            st.markdown(ai_response)
            st.divider()

            cols = st.columns(len(recommendations))

            for col, movie in zip(cols, recommendations):

                details = get_movie_details(
                    movie["movie_id"]
                )

                with col:

                    if details:

                        if details["poster"]:

                            st.image(
                                details["poster"],
                                use_container_width=True
                            )

                        st.markdown(
                            f"### {movie['title']}"
                        )

                        st.metric(
                            "Match Score",
                            movie["score"]
                        )

                        st.write(
                            f"⭐ {details['rating']}"
                        )

                        st.write(
                            details["genres"]
                        )

                    else:

                        st.write(
                            movie["title"]
                        )