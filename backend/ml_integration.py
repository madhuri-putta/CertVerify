import sys
import os
import random
try:
    import pytesseract
    from PIL import Image
except ImportError:
    pytesseract = None
    Image = None

# Add project root to sys.path to access ml module
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from ml.inference import predict as ml_predict

def extract_text(image_path: str):
    """
    Extracts text from the certificate image using OCR.
    """
    if pytesseract and Image:
        try:
            return pytesseract.image_to_string(Image.open(image_path))
        except Exception as e:
            print(f"OCR Error: {e}")
            return "OCR Failed or Tesseract not installed."
    else:
        # Simulate OCR for prototype if libs missing
        return "Simulated Extracted Text: John Doe, Computer Science, 2023"

def detect_forgery(image_path: str):
    """
    Advanced forgery detection (simulated CNN).
    """
    # In a real app, this would load a ResNet model
    # For now, we simulate a score based on random factors or file properties
    tamper_score = random.uniform(0, 20) # 0-100% chance of tampering
    
    # If file name contains "fake", simulate high tampering
    if "fake" in image_path.lower():
        tamper_score = random.uniform(80, 99)
        
    return {
        "is_tampered": tamper_score > 50,
        "tamper_score": round(tamper_score, 2),
        "areas_flagged": ["Signature", "Date"] if tamper_score > 50 else []
    }

def analyze_certificate(file_path: str):
    # 1. Basic ML Analysis (from original prototype)
    basic_result = ml_predict(file_path)
    
    # 2. OCR Text Extraction
    extracted_text = extract_text(file_path)
    
    # 3. Advanced Forgery Detection
    forgery_result = detect_forgery(file_path)
    
    return {
        "basic_analysis": basic_result,
        "ocr_text": extracted_text,
        "forgery_detection": forgery_result
    }
