import axios from "axios";
import { useState } from "react";
import "./App.css";

function App() {
  const [movie, setMovie] = useState("");
  const [recommendations, setRecommendations] = useState<string[]>([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const getRecommendations = async () => {
    try {
      setLoading(true);
      setError("");

      const response = await axios.get(
        `https://cine-match-ai-backend.onrender.com/recommend?movie=${movie}`
      );

      console.log(response.data);

      setRecommendations(
        response.data.recommendations
      );

    } catch (error) {
      console.error(error);

      setRecommendations([]);

      setError(
        "Movie not found. Try another title."
      );

    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="container">
      <h1>CineMatch AI 🎬</h1>

      <p>
        Your AI-powered movie recommendation engine
      </p>

      <div className="search-box">
        <input
          type="text"
          placeholder="Enter movie name..."
          value={movie}
          onChange={(e) => setMovie(e.target.value)}
        />

        <button onClick={getRecommendations}>
          {loading ? "Finding Movies..." : "Recommend"}
        </button>
      </div>

      <p>
        Searching for: <strong>{movie}</strong>
      </p>

      {
        error && (
          <p style={{ color: "#ef4444" }}>
            {error}
          </p>
        )
      }

      {
        recommendations.length > 0 && (
          <div style={{ marginTop: "30px" }}>
            <h2>Recommendations</h2>

            <div className="recommendations-grid">
              {recommendations.map((movie, index) => (
                <div key={index} className="movie-card">
                  <img
                    src={`https://placehold.co/300x450/1e293b/ffffff?text=${encodeURIComponent(movie)}`}
                    alt={movie}
                    className="movie-poster"
                  />

                  <h3>{movie}</h3>
                </div>
              ))}
            </div>
          </div>
        )
      }

    </div>
  );
}

export default App;