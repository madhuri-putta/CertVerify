import requests
import hashlib

BASE_URL = "http://localhost:8000"
# This is the file the user uploaded to the chat
USER_FILE_PATH = "C:\\Users\\dp419\\.gemini\\antigravity\\brain\\25e00aff-521f-48d7-877b-e3f650df6e2c\\uploaded_image_1764302979525.png"

def issue_user_file():
    print("🚀 Issuing User's Specific File...\n")
    
    try:
        with open(USER_FILE_PATH, "rb") as f:
            content = f.read()
            
        file_hash = hashlib.sha256(content).hexdigest()
        print(f"📄 User File Hash: {file_hash}")
        
        files = {'file': ('user_upload.png', content, 'image/png')}
        data = {
            'student_id': 'USER-FIX-001',
            'student_name': 'User Fix',
            'course': 'Debug Course',
            'institute': 'Debug Institute',
            'year': '2025',
            'issuer_email': 'debug@test.com'
        }
        
        print("📤 Sending Issue Request...")
        res = requests.post(f"{BASE_URL}/api/issue", files=files, data=data)
        
        if res.status_code == 200:
            resp_data = res.json()
            print(f"✅ Success! Hash Registered: {resp_data.get('hash')}")
            
            # Verify immediately
            print("\n🔍 Verifying immediately...")
            files_verify = {'file': ('user_upload.png', content, 'image/png')}
            res_verify = requests.post(f"{BASE_URL}/api/upload", files=files_verify)
            print(f"   Verification Result: {res_verify.json().get('is_real')}")
            
        else:
            print(f"❌ Failed: {res.status_code} - {res.text}")
            
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    issue_user_file()
