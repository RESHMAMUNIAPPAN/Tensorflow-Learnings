import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import numpy as np
import pickle
import json
import os

# Load JSON data
with open("data.json", "r") as file:
    data = json.load(file)

# Extract documents and labels
documents = [item["text"] for item in data]
label_map = {"invoice": 0, "resume": 1, "id_card": 2}
labels = [label_map[item["label"]] for item in data] 

# Tokenization
tokenizer = Tokenizer(num_words=1000, oov_token="<OOV>")
tokenizer.fit_on_texts(documents)
sequences = tokenizer.texts_to_sequences(documents)
padded = pad_sequences(sequences, maxlen=20)

# Convert labels to categorical (one-hot encoding)
labels = tf.keras.utils.to_categorical(labels, num_classes=3)

# Build model
model = tf.keras.Sequential([
    tf.keras.layers.Embedding(1000, 16, input_length=20),
    tf.keras.layers.GlobalAveragePooling1D(),
    tf.keras.layers.Dense(24, activation='relu'),
    tf.keras.layers.Dense(3, activation='softmax')
])

# Compile and train model
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(padded, labels, epochs=30)

# Save model and tokenizer
os.makedirs('../backend/model', exist_ok=True)
model.save("../backend/model/classifier_model.h5")
with open("../backend/model/tokenizer.pkl", "wb") as f:
    pickle.dump(tokenizer, f)

print("✅ Model and tokenizer saved in backend/model/")
