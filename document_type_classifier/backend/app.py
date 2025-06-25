from flask import Flask, request, jsonify
from flask_cors import CORS
import tensorflow as tf
import numpy as np
import os

# Initialize Flask app
app = Flask(__name__)

# Enable CORS for all domains (or restrict to React's origin if preferred)
CORS(app)  # You can use: CORS(app, origins=["http://localhost:3000"])

# Load the trained model (make sure model is in the same folder or adjust path)
model = tf.keras.models.load_model('model.h5')

# Define a dictionary for class labels (customize as per your trained classes)
class_labels = {
    0: "invoice",
    1: "resume",
    2: "id_card"
    # Add more if needed
}

# Prediction endpoint
@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()

        if 'text' not in data:
            return jsonify({'error': 'No input text provided'}), 400

        input_text = data['text']

        # Basic preprocessing (adjust according to your model’s preprocessing logic)
        # Example: tokenize and pad
        # You must use the same tokenizer/vocabulary as during training
        # This is a placeholder — update with your real tokenizer
        from tensorflow.keras.preprocessing.text import Tokenizer
        from tensorflow.keras.preprocessing.sequence import pad_sequences

        tokenizer = Tokenizer(num_words=10000, oov_token='<OOV>')
        tokenizer.fit_on_texts([input_text])  # Ideally, load saved tokenizer
        seq = tokenizer.texts_to_sequences([input_text])
        padded = pad_sequences(seq, maxlen=100)

        prediction = model.predict(padded)
        predicted_class = np.argmax(prediction, axis=1)[0]

        return jsonify({
            'prediction': class_labels.get(predicted_class, "Unknown")
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
