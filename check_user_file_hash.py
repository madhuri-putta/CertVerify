import hashlib

USER_FILE_PATH = "C:\\Users\\dp419\\.gemini\\antigravity\\brain\\25e00aff-521f-48d7-877b-e3f650df6e2c\\uploaded_image_1764302979525.png"
REGISTERED_HASH = "1db2a43913f90236482452b538ea14349316e5de3755e23205a0fd03005ad616"

def check_hash():
    print(f"🔍 Checking Hash of User's File: {USER_FILE_PATH}")
    
    try:
        with open(USER_FILE_PATH, "rb") as f:
            content = f.read()
            
        file_hash = hashlib.sha256(content).hexdigest()
        print(f"📄 User File Hash:       {file_hash}")
        print(f"✅ Registered Hash:      {REGISTERED_HASH}")
        
        if file_hash == REGISTERED_HASH:
            print("\n🎉 MATCH! The file is correct. The issue is in the System.")
        else:
            print("\n❌ MISMATCH! The user uploaded a different file.")
            print("   This explains why it says FAKE.")
            
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    check_hash()
