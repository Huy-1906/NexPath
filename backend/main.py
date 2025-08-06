from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from api import models, toolpaths, simulations, users
from models import database

app = FastAPI(title="NexPath API", description="API for NexPath LFAM Platform")

# Setup CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create database tables
database.Base.metadata.create_all(bind=database.engine)

# Include routers
app.include_router(models.router, prefix="/api/models", tags=["models"])
app.include_router(toolpaths.router, prefix="/api/toolpaths", tags=["toolpaths"])
app.include_router(simulations.router, prefix="/api/simulations", tags=["simulations"])
app.include_router(users.router, prefix="/api/users", tags=["users"])

@app.get("/")
async def root():
    return {"message": "Welcome to NexPath API"}

# Dependency to get the database session
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)