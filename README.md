# 🔐 CertVerify – Blockchain-Based Certificate Verification System

CertVerify is a secure certificate issuing and verification system built using:

- 🐍 Python (Backend API)
- ⛓️ Ethereum Blockchain (Web3)
- 🔐 SHA-256 File Hashing
- 🌐 REST APIs
- 🧪 Debug & Testing Utilities

It ensures academic certificates cannot be forged or modified.

---

## 🚀 Features

✅ Issue certificates with blockchain registration  
✅ SHA-256 hash-based certificate integrity  
✅ Verify certificates via uploaded file  
✅ Blockchain smart contract verification  
✅ Admin stats & explorer APIs  
✅ Student ID integration  
✅ Debug scripts for testing & validation  

---

## 🏗️ Project Structure

```
IDP/
│
├── backend/                      # FastAPI backend application
│
├── frontend/                     # Frontend interface (UI)
│
├── ml/                           # Machine learning components
│
├── models/                       # Saved ML models
│
├── uploads/                      # Uploaded certificate files
│
├── backend_test.py               # Backend API testing script
├── check_blockchain_direct.py    # Direct blockchain verification script
├── check_user_file_hash.py       # SHA-256 hash comparison utility
├── debug_store.py                # Debug blockchain storage
├── debug_verify.py               # Debug certificate verification
├── issue_real_cert.py            # Issue sample certificate via API
├── issue_user_file.py            # Issue user-uploaded certificate
├── verify_issue.py               # Verify certificate issue status
├── verify_student_id.py          # Student ID verification test
│
├── users.json                    # JSON-based user database
├── real_cert.png                 # Sample certificate image
│
└── README.md                     # Project documentation
```
---

## 🔧 Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/CertVerify.git
cd CertVerify
```

---

### 2️⃣ Create Virtual Environment (Recommended)

```bash
python -m venv venv
venv\Scripts\activate   # For Windows
```

---

### 3️⃣ Install Required Dependencies

```bash
pip install -r requirements.txt
```

If requirements.txt is not available, install manually:

```bash
pip install fastapi uvicorn web3 requests hashlib python-multipart
```

---

### 4️⃣ Start Backend Server

```bash
uvicorn main:app --reload
```

Backend runs at:

```
http://localhost:8000
```

API documentation available at:

```
http://localhost:8000/docs
```

---

## ⛓️ Blockchain Setup

Make sure you are running a local Ethereum node (Hardhat or Ganache):

```
http://127.0.0.1:8545
```

Smart contract interaction is handled through Web3.

---

## 📜 How Certificate Verification Works

1. Certificate file is uploaded
2. SHA-256 hash is generated
3. Hash is stored on blockchain
4. During verification:
   - File is re-hashed
   - Compared with blockchain record
   - Validity is returned (Real / Fake)

---

## 🧪 Testing & Debug Scripts

Run backend test:

```bash
python backend_test.py
```

Debug blockchain storage:

```bash
python debug_store.py
```

Verify certificate upload:

```bash
python debug_verify.py
```

Direct blockchain verification:

```bash
python check_blockchain_direct.py
```

---

## 📊 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | /api/issue | Issue certificate |
| POST | /api/upload | Verify certificate |
| GET | /api/explorer | View certificates |
| GET | /api/admin/stats | Admin statistics |
| POST | /auth/register | Register user |
| POST | /auth/login | Login user |

---

## 🔐 Security Features

- SHA-256 file hashing
- Blockchain immutability
- Secure REST APIs
- Student ID validation
- Certificate integrity checking

---

## 🎯 Use Case

- Universities
- Online Certification Platforms
- Skill Training Institutes
- Digital Credential Verification Systems

---

## 👩‍💻 Author

**Madhuri Putta**  
Blockchain & Backend Developer  

---

## ⭐ Future Enhancements

- Deploy smart contract on public Ethereum testnet
- IPFS integration for decentralized storage
- QR code based certificate validation
- Frontend UI improvements
- AI-based forged certificate detection
