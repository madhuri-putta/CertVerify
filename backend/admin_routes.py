from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from typing import List
import datetime

router = APIRouter()

# Mock Database
certificates_db = []

class CertificateIssueRequest(BaseModel):
    student_id: str
    student_name: str
    course: str
    institute: str
    year: str
    issuer_email: str

from fastapi import Form, File, UploadFile

@router.post("/issue")
async def issue_certificate(
    file: UploadFile = File(...),
    student_id: str = Form(...),
    student_name: str = Form(...),
    course: str = Form(...),
    institute: str = Form(...),
    year: str = Form(...),
    issuer_email: str = Form(...)
):
    # Calculate File Hash (Critical for matching Verify logic)
    import hashlib
    sha256_hash = hashlib.sha256()
    content = await file.read()
    sha256_hash.update(content)
    cert_hash = sha256_hash.hexdigest()
    
    # Store on Blockchain
    from .blockchain_utils import store_on_blockchain
    tx_hash = store_on_blockchain(
        cert_hash, 
        student_name, 
        course, 
        institute, 
        issuer_email
    )
    
    # Store in DB
    cert_record = {
        "hash": cert_hash,
        "student_id": student_id,
        "student_name": student_name,
        "course": course,
        "institute": institute,
        "year": year,
        "issuer_email": issuer_email,
        "timestamp": datetime.datetime.now().isoformat(),
        "status": "Issued",
        "tx_hash": tx_hash
    }
    certificates_db.append(cert_record)
    
    return {
        "message": "Certificate Issued Successfully",
        "hash": cert_hash,
        "transaction_hash": tx_hash
    }

@router.get("/admin/stats")
def get_admin_stats():
    return {
        "total_issued": len(certificates_db),
        "total_verified": 150, # Mock
        "fake_attempts": 5, # Mock
        "recent_activity": certificates_db[-5:]
    }

@router.get("/explorer")
def blockchain_explorer():
    return {
        "certificates": certificates_db,
        "latest_block": 12345
    }
