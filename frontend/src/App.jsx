import { useState } from "react";
import axios from "axios";

function App() {
  const [result, setResult] = useState(null);

  const handlePredict = async () => {
    try {
      const response = await axios.post("http://127.0.0.1:8000/predict", {
        day: 10,
        month: 4,
        day_of_week: 2,
        is_weekend: 0,
        lag_1: 120,
        lag_7: 110,
        rolling_mean_7: 115,
        quarter: 2,
        day_of_year: 100,
        rolling_std_7: 8
      });
      setResult(response.data);
    } catch (error) {
      console.error("Prediction failed:", error);
    }
  };

  return (
    <div style={{ padding: "30px", fontFamily: "Arial" }}>
      <h1>Medicine Demand Forecast Dashboard</h1>

      <button onClick={handlePredict}>
        Predict
      </button>

      {result && (
        <div style={{ marginTop: "20px" }}>
          <h2>Predicted Demand: {result.prediction}</h2>
          <h3>
            Range: {result.lower} - {result.upper}
          </h3>
          <h3>
            Recommended Stock: {result.recommended_stock}
          </h3>
          <h3>Risk: {result.risk}</h3>
          <p>{result.insight}</p>
        </div>
      )}
    </div>
  );
}

export default App;