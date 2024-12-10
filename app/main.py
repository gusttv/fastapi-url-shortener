from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from app.database import Base, engine, SessionLocal
from app.model import URL
from app.schema import URLCreate, URLResponse
import string
import random

Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency for database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Utility function to generate short URL
def generate_short_url():
    chars = string.ascii_letters + string.digits
    return ''.join(random.choices(chars, k=6))

# Endpoint to create short URL
@app.post("/shorten", response_model=URLResponse)
def create_short_url(url: URLCreate, db: Session = Depends(get_db)):
    """Cria uma URL encurtada"""
    db_url = db.query(URL).filter(URL.original_url == str(url.original_url)).first()
    if db_url:
        return db_url

    short_url = generate_short_url()
    while db.query(URL).filter(URL.short_url == short_url).first():
        short_url = generate_short_url()

    # Certifique-se de que ambos os valores são strings
    new_url = URL(original_url=str(url.original_url), short_url=str(short_url))
    db.add(new_url)
    db.commit()
    db.refresh(new_url)

    return new_url


# Endpoint to redirect to the original URL
@app.get("/{short_url}", response_model=URLResponse)
def redirect_to_url(short_url: str, db: Session = Depends(get_db)):
    db_url = db.query(URL).filter(URL.short_url == short_url).first()
    if not db_url:
        raise HTTPException(status_code=404, detail="URL not found")
    return db_url