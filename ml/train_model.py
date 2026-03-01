import os
import joblib
from sklearn.ensemble import RandomForestClassifier
import numpy as np

# Create a dummy dataset
# Features: [text_clarity, edge_sharpness, logo_presence, watermark_intensity]
X = np.array([
    [0.9, 0.9, 1, 0.8], # Real
    [0.8, 0.9, 1, 0.7], # Real
    [0.4, 0.5, 0, 0.2], # Fake
    [0.3, 0.4, 0, 0.1], # Fake
])
y = np.array([1, 1, 0, 0]) # 1: Real, 0: Fake

def train():
    print("Training model...")
    model = RandomForestClassifier()
    model.fit(X, y)
    
    # Save model
    os.makedirs("models", exist_ok=True)
    joblib.dump(model, "models/certificate_model.pkl")
    print("Model saved to models/certificate_model.pkl")

if __name__ == "__main__":
    train()
