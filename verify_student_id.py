import requests
import json

BASE_URL = "http://localhost:8000"

def verify_student_id_flow():
    print("🚀 Verifying Student ID Integration...\n")
    
    # 1. Issue Certificate with Student ID
    payload = {
        "student_id": "STU-9999",
        "student_name": "Test Student With ID",
        "course": "Blockchain Engineering",
        "institute": "Tech University",
        "year": "2024",
        "issuer_email": "issuer@test.com"
    }
    
    print("1️⃣ Issuing Certificate...")
    try:
        res = requests.post(f"{BASE_URL}/api/issue", json=payload)
        if res.status_code == 200:
            print("   ✅ Certificate Issued Successfully")
        else:
            print(f"   ❌ Issue Failed: {res.status_code} - {res.text}")
            return
    except Exception as e:
        print(f"   ❌ Connection Error: {e}")
        return

    # 2. Verify Backend Storage
    print("\n2️⃣ Checking Backend Storage...")
    try:
        res = requests.get(f"{BASE_URL}/api/explorer")
        if res.status_code == 200:
            data = res.json()
            certificates = data.get("certificates", [])
            
            found = False
            for cert in certificates:
                if cert.get("student_id") == "STU-9999":
                    print("   ✅ FOUND: Certificate with Student ID 'STU-9999' is in the backend!")
                    print(json.dumps(cert, indent=2))
                    found = True
                    break
            
            if not found:
                print("   ❌ NOT FOUND: Certificate with Student ID 'STU-9999' not found.")
        else:
            print(f"   ❌ Error fetching explorer data: {res.status_code}")
    except Exception as e:
        print(f"   ❌ Connection Error: {e}")

if __name__ == "__main__":
    verify_student_id_flow()
