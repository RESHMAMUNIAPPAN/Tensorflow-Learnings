from flask import Flask, request, jsonify
from flask_cors import CORS
import tensorflow as tf
import numpy as np
import pickle
import os
import traceback
from pymongo import MongoClient
from datetime import datetime
import certifi  # ✅ For trusted SSL certificate

app = Flask(__name__)
CORS(app)

# Load the model
model = tf.keras.models.load_model('model/classifier_model.h5')

# Load the tokenizer
with open("model/tokenizer.pkl", "rb") as f:
    tokenizer = pickle.load(f)

# Class labels
class_labels = {
    0: "invoice",
    1: "resume",
    2: "id_card"
}

# ✅ Secure MongoDB connection using certifi
client = MongoClient(
    "mongodb+srv://pmreshma2004:pyLT7XTOY6j4o74o@tensorflow-project.5uiajhn.mongodb.net/?retryWrites=true&w=majority&appName=TensorFlow-Project",
    tls=True,
    tlsCAFile=certifi.where()
)
db = client["document_classifier"]
collection = db["predictions"]

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()

        if 'text' not in data:
            return jsonify({'error': 'No input text provided'}), 400

        input_text = data['text']
        seq = tokenizer.texts_to_sequences([input_text])
        padded = tf.keras.preprocessing.sequence.pad_sequences(seq, maxlen=20)

        prediction = model.predict(padded)
        predicted_class_index = int(np.argmax(prediction))
        confidence_score = float(np.max(prediction)) * 100

        label = class_labels.get(predicted_class_index, "Unknown")

        # Insert into MongoDB
        result_doc = {
            "text": input_text,
            "predicted_label": label,
            "confidence": round(confidence_score, 2),
            "timestamp": datetime.utcnow()
        }
        collection.insert_one(result_doc)

        return jsonify({
            "prediction": label,
            "confidence": f"{confidence_score:.2f}%"
        })

    except Exception as e:
        print("⚠️ Error during prediction:")
        traceback.print_exc()
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
