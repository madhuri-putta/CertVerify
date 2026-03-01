import requests
import json
import os

BASE_URL = "http://localhost:8000"
TEST_EMAIL = "backend_test_user@example.com"
TEST_PASSWORD = "password123"

def print_result(name, success, details=""):
    status = "✅ PASS" if success else "❌ FAIL"
    print(f"{status} - {name}")
    if details:
        print(f"   {details}")

def test_backend():
    print("🚀 Starting Backend Verification...\n")
    
    token = None

    # 1. Test Registration
    try:
        payload = {
            "email": TEST_EMAIL,
            "password": TEST_PASSWORD,
            "confirm_password": TEST_PASSWORD
        }
        res = requests.post(f"{BASE_URL}/auth/register", json=payload)
        if res.status_code == 200 or (res.status_code == 400 and "already exists" in res.text):
            print_result("Registration", True)
        else:
            print_result("Registration", False, f"Status: {res.status_code}, Body: {res.text}")
    except Exception as e:
        print_result("Registration", False, str(e))

    # 2. Test Login
    try:
        payload = {"email": TEST_EMAIL, "password": TEST_PASSWORD}
        res = requests.post(f"{BASE_URL}/auth/login", json=payload)
        if res.status_code == 200:
            data = res.json()
            token = data.get("access_token")
            print_result("Login", True, f"Token received: {token[:10]}...")
        else:
            print_result("Login", False, f"Status: {res.status_code}, Body: {res.text}")
    except Exception as e:
        print_result("Login", False, str(e))

    # 3. Test Admin Stats
    try:
        res = requests.get(f"{BASE_URL}/api/admin/stats")
        if res.status_code == 200:
            stats = res.json()
            print_result("Admin Stats", True, f"Issued: {stats.get('total_issued')}, Verified: {stats.get('total_verified')}")
        else:
            print_result("Admin Stats", False, f"Status: {res.status_code}")
    except Exception as e:
        print_result("Admin Stats", False, str(e))

    # 4. Test Blockchain Explorer
    try:
        res = requests.get(f"{BASE_URL}/api/explorer/blocks")
        if res.status_code == 200:
            blocks = res.json()
            print_result("Blockchain Explorer", True, f"Blocks found: {len(blocks)}")
        else:
            print_result("Blockchain Explorer", False, f"Status: {res.status_code}")
    except Exception as e:
        print_result("Blockchain Explorer", False, str(e))

    # 5. Test Certificate Issue (Mock)
    try:
        payload = {
            "student_name": "Backend Test Student",
            "course": "Computer Science",
            "institute": "Test Institute",
            "year": "2024",
            "issuer_email": TEST_EMAIL
        }
        # Note: Assuming /api/issue endpoint exists based on previous context
        res = requests.post(f"{BASE_URL}/api/issue", json=payload)
        if res.status_code == 200:
            print_result("Issue Certificate", True)
        else:
            # It might fail if not implemented or different path, but we check availability
            print_result("Issue Certificate", res.status_code in [200, 201], f"Status: {res.status_code}")
    except Exception as e:
        print_result("Issue Certificate", False, str(e))

    print("\n🏁 Backend Verification Complete.")

if __name__ == "__main__":
    test_backend()
