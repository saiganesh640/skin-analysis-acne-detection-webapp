# flask_model_api.py
from flask import Flask, request, jsonify
from flask_cors import CORS
import tensorflow as tf
from PIL import Image
import numpy as np
import io, json, os

app = Flask(__name__)
CORS(app)

MODEL_PATH = "acne_detection_model.h5"  # change only if filename differs
if not os.path.exists(MODEL_PATH):
    raise RuntimeError(f"Model file not found: {MODEL_PATH}")

# Load model once
model = tf.keras.models.load_model(MODEL_PATH)

# Update labels to match how your model was trained (3-class example)
CLASS_NAMES = ["Clear", "Moderate", "Severe"]

def preprocess_image(pil_image):
    # adapt to the preprocessing used during training
    img = pil_image.convert("RGB").resize((224, 224))
    arr = np.array(img).astype(np.float32) / 255.0
    arr = np.expand_dims(arr, axis=0)  # shape (1, 224, 224, 3)
    return arr

@app.route("/predict", methods=["POST"])
def predict():
    # Expect multipart/form-data with image file and optional 'quiz' field (JSON string)
    if "image" not in request.files:
        return jsonify({"error": "no image uploaded"}), 400

    file = request.files["image"]
    try:
        img = Image.open(io.BytesIO(file.read()))
    except Exception as e:
        return jsonify({"error": "invalid image", "detail": str(e)}), 400

    # optional quiz JSON (string)
    quiz_json = request.form.get("quiz", "{}")
    try:
        quiz_data = json.loads(quiz_json)
    except Exception:
        quiz_data = {}

    # preprocess and model predict
    x = preprocess_image(img)
    preds = model.predict(x)  # shape (1, N)
    probs = preds[0].tolist()

    # pick best class
    best_idx = int(np.argmax(probs))
    best_label = CLASS_NAMES[best_idx] if best_idx < len(CLASS_NAMES) else str(best_idx)
    confidence = float(probs[best_idx]) * 100.0

    # Optionally combine quiz features here (you can extend)
    result = {
        "severity": best_label,
        "confidence": round(confidence, 2),
        "probs": probs,
        "quiz": quiz_data
    }
    return jsonify(result)

if __name__ == "__main__":
    # debug False in production
    app.run(host="0.0.0.0", port=5000, debug=True)
