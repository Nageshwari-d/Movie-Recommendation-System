import pandas as pd
import pickle

# Load the saved data and model
movies = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

def recommend(movie_title):
    """
    Recommends top 5 movies similar to the given movie title.
    """
    # Check if the movie exists in our dataset
    if movie_title not in movies['title'].values:
        print("Sorry, that movie is not in our dataset.")
        return

    # Find the index of the input movie
    movie_index = movies[movies['title'] == movie_title].index[0]

    # Get the similarity scores for the input movie
    distances = similarity[movie_index]

    # Sort and get the top 5 most similar movies
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    print(f"\nRecommendations for '{movie_title}':")
    for i in movie_list:
        print(movies.iloc[i[0]].title)

# Main execution loop
if __name__ == "__main__":
    print("Welcome to the Movie Recommender!")
    print("Type 'exit' to quit.")
    while True:
        user_input = input("Enter a movie title: ")
        if user_input.lower() == 'exit':
            break
        recommend(user_input)