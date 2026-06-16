import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


MOVIES_PATH = "../datasets/tmdb_5000_movies.csv"

# Dataset load
movies = pd.read_csv(MOVIES_PATH)

# Missing values handle
movies["overview"] = movies["overview"].fillna("")

# TF-IDF Vectorization
tfidf = TfidfVectorizer(stop_words="english")

tfidf_matrix = tfidf.fit_transform(movies["overview"])

# Similarity Matrix
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Title → Index mapping
indices = pd.Series(
    movies.index,
    index=movies["title"]
).drop_duplicates()


def recommend_movies(title, n=5):
    if title not in indices:
        return f"Movie '{title}' not found."

    idx = indices[title]

    similarity_scores = list(
        enumerate(cosine_sim[idx])
    )

    similarity_scores = sorted(
        similarity_scores,
        key=lambda x: x[1],
        reverse=True
    )

    similarity_scores = similarity_scores[1:n+1]

    movie_indices = [
        i[0] for i in similarity_scores
    ]

    return movies["title"].iloc[
        movie_indices
    ].tolist()

if __name__ == "__main__":
    recommendations = recommend_movies(
        "Avatar"
    )

    print(
        "\n🎬 Recommendations for Avatar:\n"
    )

    for movie in recommendations:
        print(f"• {movie}")