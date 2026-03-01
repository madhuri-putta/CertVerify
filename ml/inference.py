import joblib
import os
import numpy as np

MODEL_PATH = os.path.join(os.path.dirname(__file__), "..", "models", "certificate_model.pkl")

def predict(image_path):
    # In a real scenario, we would extract features from the image using OpenCV
    # For now, we generate random features to simulate analysis
    # Features: [text_clarity, edge_sharpness, logo_presence, watermark_intensity]
    
    # Simulate feature extraction (randomized for demo)
    features = np.random.rand(1, 4) 
    
    try:
        model = joblib.load(MODEL_PATH)
        prediction = model.predict(features)[0]
        probability = model.predict_proba(features)[0][1] # Probability of being Real
        
        is_real = probability > 0.5
        reason = "High confidence in certificate authenticity" if is_real else "Anomalies detected in text clarity or watermark"
        
        return {
            "is_fake": not is_real,
            "confidence": float(probability),
            "reason": reason
        }
    except Exception as e:
        print(f"Error loading model: {e}")
        # Fallback if model not trained
        return {"is_fake": False, "confidence": 0.0, "reason": "Model not loaded"}
