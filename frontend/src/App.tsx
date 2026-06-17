import axios from "axios";

import { useState } from "react";
import "./App.css";

function App() {
  const [movie, setMovie] = useState("");

  const [recommendations, setRecommendations] = useState<string[]>([]);
  const [loading, setLoading] = useState(false);


  const getRecommendations = async () => {
  try {
    setLoading(true);

    const response = await axios.get(
      `http://127.0.0.1:8000/recommend?movie=${movie}`
    );

    console.log(response.data);

    setRecommendations(
      response.data.recommendations
    );

  } catch (error) {
    console.error(error);
    alert("Failed to fetch recommendations.");
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
          {loading ? "Loading..." : "Recommend"}
        </button>
      </div>

      <p>
        Searching for: <strong>{movie}</strong>
      </p>

      {
        recommendations.length > 0 && (
          <div style={{ marginTop: "30px" }}>
            <h2>Recommendations</h2>

            {recommendations.map((movie, index) => (
              <p key={index}>
                🎬 {movie}
              </p>
            ))}
          </div>
        )
      }

    </div>
  );
}

export default App;