# movie_semantic_search
This is a simple web-based Movie Search Engine that allows users to search for movies based on a text description. The application uses semantic similarity to find and display the most relevant movies from a precomputed dataset.

## Features

- Search for movies by entering a text description.
- Displays the top 5 most similar movies based on semantic similarity.
- Shows movie details such as title, type, genres, production countries, and similarity score.
- Fetches and displays movie posters using IMDbPY.

## Requirements

### Python Version

- Python 3.7 or later

### Dependencies

- `streamlit==1.24.0`
- `sentence-transformers==2.2.2`
- `scikit-learn==1.3.0`
- `imdbpy==2023.5.1`
- `pandas==2.0.3`
- `numpy==1.24.2`

### Data

- The precomputed movie embeddings are stored in a file named `movie_semantic.pkl`, which should be placed in the same directory as the script.

## Installation

1. **Clone the Repository (if applicable):**

   ```bash
   git clone https://github.com/your-repository/movie-search-engine.git
   cd movie-search-engine

**Create a Virtual Environment (Optional but Recommended):

python3 -m venv movie_search_env
source movie_search_env/bin/activate

**Install the Required Libraries:

pip install -r requirements.txt

**Run the Streamlit Application:
streamlit run movie_search.py


