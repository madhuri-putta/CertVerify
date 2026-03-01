import requests
import json

BASE_URL = "http://localhost:8000"

def verify_student_issue(student_name):
    print(f"🔍 Checking backend for student: {student_name}...")
    
    try:
        # Fetch from Explorer endpoint which returns all certificates
        res = requests.get(f"{BASE_URL}/api/explorer")
        if res.status_code == 200:
            data = res.json()
            certificates = data.get("certificates", [])
            
            found = False
            for cert in certificates:
                if cert.get("student_name", "").lower() == student_name.lower():
                    print(f"✅ FOUND: Certificate for '{student_name}' is in the backend!")
                    print(json.dumps(cert, indent=2))
                    found = True
                    break
            
            if not found:
                print(f"❌ NOT FOUND: No certificate for '{student_name}' found in backend.")
                print(f"   Total certificates in DB: {len(certificates)}")
                if len(certificates) > 0:
                    print("   Recent entries:")
                    for c in certificates[-3:]:
                        print(f"   - {c.get('student_name')}")
        else:
            print(f"❌ Error fetching data: {res.status_code}")
    except Exception as e:
        print(f"❌ Connection Error: {e}")

if __name__ == "__main__":
    verify_student_issue("Madhuri")
