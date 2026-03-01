import requests
import hashlib

BASE_URL = "http://localhost:8000"
FILE_PATH = "C:\\Users\\dp419\\Desktop\\IDP\\real_cert.png"

def issue_real_certificate():
    print("🚀 Issuing Real Certificate via API...\n")
    
    try:
        with open(FILE_PATH, "rb") as f:
            dummy_content = f.read()
        file_hash = hashlib.sha256(dummy_content).hexdigest()
        print(f"📄 File Hash: {file_hash}")
        
        print("\n1️⃣ Issuing Certificate (Uploading File)...")
        files = {'file': ('real_cert.png', dummy_content, 'image/png')}
        data = {
            'student_id': 'DEMO-001',
            'student_name': 'Browser Demo',
            'course': 'Test',
            'institute': 'Test',
            'year': '2025',
            'issuer_email': 'demo@test.com'
        }
        
        res = requests.post(f"{BASE_URL}/api/issue", files=files, data=data)
        if res.status_code == 200:
            resp_data = res.json()
            print(f"   ✅ Certificate Issued! Returned Hash: {resp_data.get('hash')}")
            if resp_data.get('hash') == file_hash:
                print("   ✅ Hash Match Confirmed!")
            else:
                print(f"   ❌ Hash Mismatch! Expected {file_hash}, got {resp_data.get('hash')}")
        else:
            print(f"   ❌ Issue Failed: {res.status_code} - {res.text}")
    except Exception as e:
        print(f"   ❌ Error: {e}")

if __name__ == "__main__":
    issue_real_certificate()
