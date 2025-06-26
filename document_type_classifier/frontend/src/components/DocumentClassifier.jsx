import React, { useState } from "react";
import axios from "axios";

const DocumentClassifier = () => {
  const [text, setText] = useState("");
  const [result, setResult] = useState(null);
  const [error, setError] = useState("");

  const handleSubmit = async () => {
    try {
      const response = await axios.post("http://127.0.0.1:5000/predict", {
        text: text,
      });
      setResult(response.data);
      setError("");
    } catch (err) {
      setError("Prediction failed. Please check the server or input.");
      setResult(null);
    }
  };

  return (
    <div className="min-h-screen flex flex-col items-center justify-center bg-gray-100 p-4">
      <div className="bg-white p-8 rounded-xl shadow-md w-full max-w-xl">
        <h2 className="text-2xl font-bold mb-4 text-center">
          Document Type Classifier
        </h2>

        <textarea
          className="w-full p-3 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-400"
          rows={6}
          placeholder="Enter document text here..."
          value={text}
          onChange={(e) => setText(e.target.value)}
        />

        <button
          onClick={handleSubmit}
          className="mt-4 w-full bg-blue-600 text-white py-2 px-4 rounded-md hover:bg-blue-700 transition"
        >
          Predict
        </button>

        {result && (
          <div className="mt-6 p-4 bg-green-100 border border-green-400 rounded-md">
            <p>
              <strong>Prediction:</strong> {result.prediction}
            </p>
            <p>
              <strong>Confidence:</strong> {result.confidence}
            </p>
          </div>
        )}

        {error && (
          <div className="mt-4 p-3 bg-red-100 border border-red-400 text-red-800 rounded-md">
            {error}
          </div>
        )}
      </div>
    </div>
  );
};

export default DocumentClassifier;