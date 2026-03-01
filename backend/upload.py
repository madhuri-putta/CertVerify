from fastapi import APIRouter, UploadFile, File, HTTPException
import shutil
import os
import hashlib
from .ml_integration import analyze_certificate
from .blockchain_utils import verify_on_blockchain

router = APIRouter()

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

def calculate_hash(file_path):
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    # 1. Analyze with ML
    ml_result = analyze_certificate(file_path)
    
    # 2. Verify on Blockchain
    file_hash = calculate_hash(file_path)
    print(f"DEBUG: Uploaded File Hash: {file_hash}")
    
    blockchain_result = verify_on_blockchain(file_hash)
    print(f"DEBUG: Blockchain Result: {blockchain_result}")
    
    is_verified = blockchain_result["verified"]
    
    # Combine results
    # ml_result now contains { "basic_analysis": ..., "ocr_text": ..., "forgery_detection": ... }
    
    basic = ml_result["basic_analysis"]
    forgery = ml_result["forgery_detection"]
    
    # Determine if real based on basic confidence and forgery score
    # CRITICAL UPDATE: If Blockchain says verified, it IS verified. ML is just supplementary.
    if is_verified:
        is_ml_real = True
        basic["confidence"] = 1.0 # Force 100% confidence
        basic["reason"] = "Verified by Blockchain" # Clear any ML anomaly warnings
    else:
        is_ml_real = (basic["confidence"] > 0.8) and (not forgery["is_tampered"])
    
    final_result = {
        "filename": file.filename,
        "ml_analysis": basic, 
        "ocr_text": ml_result["ocr_text"],
        "forgery_detection": forgery,
        "blockchain_verified": is_verified,
        "blockchain_data": blockchain_result if is_verified else None,
        "is_real": is_verified, # Trust Blockchain as ultimate source of truth
        "calculated_hash": file_hash  # Debugging field
    }
    
    return final_result
