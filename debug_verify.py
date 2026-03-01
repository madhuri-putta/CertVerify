import requests

BASE_URL = "http://localhost:8000"
FILE_PATH = "C:\\Users\\dp419\\Desktop\\IDP\\real_cert.png"

def debug_verify():
    print("🚀 Debugging Verification...\n")
    try:
        with open(FILE_PATH, "rb") as f:
            content = f.read()
            
        files = {'file': ('real_cert.png', content, 'image/png')}
        
        print(f"📤 Uploading {FILE_PATH}...")
        res = requests.post(f"{BASE_URL}/api/upload", files=files)
        
        if res.status_code == 200:
            print("✅ Response Received:")
            print(res.json())
        else:
            print(f"❌ Error: {res.status_code} - {res.text}")
            
    except Exception as e:
        print(f"❌ Exception: {e}")

if __name__ == "__main__":
    debug_verify()
