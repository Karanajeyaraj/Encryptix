from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

print("Karana's Movie Recommendation site")
print('Top movies You Watched:')
print('a. Harry Potter')
print('b. Pirates of Carribbean')
print('c. Fantastic Beast')
print('d. Mission Majnu')

# Input for recently watched movie
m = input("Select recently watched movie (a/b/c/d): ").strip().lower()

# Mapping the input to the movie names
movie_mapping = {
    'a': 'Harry Potter',
    'b': 'Pirates of Carribbean',
    'c': 'Fantastic Beast',
    'd': 'Mission Majnu'
}

if m not in movie_mapping:
    print("Invalid choice. Please select a valid option (a/b/c/d).")
else:
    # Get the movie name based on user input
    movie_to_recommend = movie_mapping[m]

    # Sample movie dataset with descriptions
    movies = {
        'Movie': ['Harry Potter', 'Pirates of Carribbean', 'Fantastic Beast', 'Mission Majnu'],
        'Description': [
            'thriller',
            'Adventure',
            'Fantasy, Fiction movie',
            'Action thriller with a secret agent'
        ]
    }

    movies_df = pd.DataFrame(movies)

    # Step 1: Convert text descriptions into vectors using TF-IDF
    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(movies_df['Description'])

    # Step 2: Compute cosine similarity between movies
    cosine_sim = cosine_similarity(tfidf_matrix)

    # Step 3: Function to get recommendations based on movie description similarity
    def content_based_recommend(movie, num_recommendations=2):
        movie_idx = movies_df[movies_df['Movie'].str.lower() == movie.lower()].index

        if len(movie_idx) == 0:
            return "Movie not found. Please enter a valid movie name."
        
        movie_idx = movie_idx[0]
        sim_scores = list(enumerate(cosine_sim[movie_idx]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        sim_scores = sim_scores[1:num_recommendations + 1]  # Skip the input movie itself
        movie_indices = [i[0] for i in sim_scores]
        return movies_df['Movie'].iloc[movie_indices]

    # Step 4: Get recommendations for the specific movie
    recommendations = content_based_recommend(movie_to_recommend)

    # Handle output
    if isinstance(recommendations, str):
        print(recommendations)  # Print error message if movie not found
    else:
        print(f"Movies similar to {movie_to_recommend}:")
        print(recommendations)
