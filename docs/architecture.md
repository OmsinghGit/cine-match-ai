# CineMatch AI Architecture

```text
+----------------------+
|   React Frontend     |
|  (TypeScript + Vite) |
+----------+-----------+
           |
           | Axios HTTP Requests
           v
+----------------------+
|    FastAPI Backend   |
|      REST APIs       |
+----------+-----------+
           |
           | Calls
           v
+----------------------+
| Recommendation Engine|
| TF-IDF + Cosine Sim. |
+----------+-----------+
           |
           | Reads Data
           v
+----------------------+
|   TMDB Movie Dataset |
+----------------------+
```

## Flow

1. User enters a movie title.
2. React frontend sends a request using Axios.
3. FastAPI receives the request.
4. Recommendation engine processes movie similarity.
5. TF-IDF and Cosine Similarity calculate related movies.
6. Results are returned to the frontend.
7. Recommendations are displayed as movie cards.
