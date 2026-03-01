from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .auth import router as auth_router
from .upload import router as upload_router
from .admin_routes import router as admin_router
from .explorer_routes import router as explorer_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router, prefix="/auth")
app.include_router(upload_router, prefix="/api")
app.include_router(admin_router, prefix="/api")
app.include_router(explorer_router, prefix="/api")

@app.get("/")
def read_root():
    return {"Hello": "World"}
