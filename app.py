import streamlit as st
import pickle
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer
from imdb import IMDb  # Import IMDbPY
# Streamlit UI for Movie Search
st.set_page_config(page_title="Movie Search Engine", page_icon=":clapper:", layout="wide")
# Set up IMDb instance
ia = IMDb()

# Cache the loading of the model and data to avoid redundant operations
@st.cache_resource
def load_model_and_data():
    # Load pre-trained model (only for generating new embeddings, if needed)
    model_name = "all-MiniLM-L6-v2"
    model = SentenceTransformer(model_name)
    
    # Load the DataFrame with precomputed embeddings
    with open('movie_semantic.pkl', 'rb') as f:
        movie_data_df = pickle.load(f)
    
    return model, movie_data_df

model, movie_data_df = load_model_and_data()

# Function to generate embedding for the user's query using SentenceTransformer
def generate_embedding(text):
    return model.encode([text])[0]



st.title('Movie Search Engine')
query = st.text_input('Enter a movie description:')

if st.button('Search'):
    if query:
        # st.subheader("Movie Description")
        # st.write(query)
        # Generate embedding for the user's query
        query_embedding = generate_embedding(query)

        # Compute cosine similarity between the query embedding and all stored embeddings
        similarities = cosine_similarity(
            [query_embedding],  # Reshape to 2D array as required by cosine_similarity
            movie_data_df['embeddings'].tolist()
        )

        # Flatten the similarity scores array and get the indices of top matches
        similarities = similarities.flatten()
        top_indices = similarities.argsort()[::-1][:5]  # Get indices of top 5 similar movies

        # Display the top results with movie posters
        cols = st.columns(5)  # Create 5 columns for the top 5 results

        for i, index in enumerate(top_indices):
            movie_title = movie_data_df.iloc[index]['title']
            with cols[i]:  # Place each result in its own column
                st.write(f"*Title:* {movie_title}")
                st.write(f"*Type:* {movie_data_df.iloc[index]['type']}")
                st.write(f"*Genres:* {movie_data_df.iloc[index]['genres']}")
                st.write(f"*Countries:* {movie_data_df.iloc[index]['production_countries']}")
                st.write(f"*Similarity Score:* {similarities[index]}")

                # Fetch movie poster using IMDbPY
                search_results = ia.search_movie(movie_title)
                if search_results:
                    movie = ia.get_movie(search_results[0].movieID)
                    if 'cover url' in movie:
                        st.image(movie['cover url'], width=150)  # Display poster with smaller size
                else:
                    st.write("Poster not available.")