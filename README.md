# Movie Recommendation System

This is a content-based movie recommendation system that suggests movies based on their similarity to a user's chosen movie. The system uses a machine learning approach to analyze and compare movie features, providing a personalized list of recommendations.

The project is built entirely in Python, leveraging popular data science libraries to process and model the data.

## Key Features

- **Content-Based Filtering:** Recommends movies based on shared genres, keywords, cast members, and director.
- **Fast and Efficient:** Uses a pre-computed similarity matrix to provide instant recommendations.
- **Extensive Dataset:** Utilizes the TMDB 5000 movie dataset for a wide range of movies.
- **Interactive CLI:** Includes a simple command-line interface for easy user interaction.

## Technologies Used

- **Python:** The core programming language for the project.
- **Pandas:** Used for data manipulation and cleaning.
- **Scikit-learn:** Provides tools for text vectorization (`CountVectorizer`) and similarity calculation (`cosine_similarity`).
- **Pickle:** Used to serialize and save the final data and model objects for later use.

## How to Run the Project

Follow these steps to run the project on your local machine:

### Step 1: Prerequisites

Make sure you have Python installed. Then, install the required libraries:

```bash
pip install pandas scikit-learn
```

### Step 2: Get the Data

Download the tmdb_5000_movies.csv and tmdb_5000_credits.csv datasets.
Place these files in your project directory.

### Step 3: Run the Jupyter Notebook

Run the original Jupyter Notebook `bash(Movie_Recommendation_System.ipynb)` to perform data processing and create the `bash movies.pkl ` and `bash similarity.pkl ` files.

### Step 4: Run the Command-Line Application

After generating the model files, run the CLI application:

```bash
python app.py

```

You will be prompted to enter a movie title to receive recommendations.

### Example Usage

```bash
Welcome to the Movie Recommender!
Type 'exit' to quit.
Enter a movie title: Avatar

Recommendations for 'Avatar':
- Aliens
- Alien³
- Alien
- Star Trek Into Darkness
- Silent Running
```
