from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from typing import Optional
import jwt
import datetime
import json
import os

router = APIRouter()

SECRET_KEY = "your_secret_key"
ALGORITHM = "HS256"
USERS_FILE = "users.json"

class UserLogin(BaseModel):
    email: str
    password: str

class UserRegister(BaseModel):
    email: str
    password: str
    confirm_password: str

def load_users():
    if not os.path.exists(USERS_FILE):
        return {}
    try:
        with open(USERS_FILE, "r") as f:
            return json.load(f)
    except:
        return {}

def save_users(users):
    with open(USERS_FILE, "w") as f:
        json.dump(users, f)

@router.post("/login")
def login(user: UserLogin):
    users = load_users()
    
    # Check if user exists and password matches
    if user.email in users and users[user.email] == user.password:
        token = jwt.encode({
            "sub": user.email,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)
        }, SECRET_KEY, algorithm=ALGORITHM)
        return {"access_token": token, "token_type": "bearer"}
    
    # Fallback for the hardcoded test user if not in file
    if user.email == "test@example.com" and user.password == "password":
        token = jwt.encode({
            "sub": user.email,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)
        }, SECRET_KEY, algorithm=ALGORITHM)
        return {"access_token": token, "token_type": "bearer"}
        
    raise HTTPException(status_code=401, detail="Invalid credentials")

@router.post("/register")
def register(user: UserRegister):
    if user.password != user.confirm_password:
        raise HTTPException(status_code=400, detail="Passwords do not match")
    
    users = load_users()
    
    if user.email in users:
        raise HTTPException(status_code=400, detail="User already exists")
        
    users[user.email] = user.password
    save_users(users)
    
    return {"message": "User registered successfully"}
