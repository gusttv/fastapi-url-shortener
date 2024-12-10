from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from app.models.url_model import URL
from app.schemas.url_schema import URLCreate, URLResponse
from app.utils.shortener import generate_short_url

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/shorten", response_model=URLResponse)
def create_short_url(url: URLCreate, db: Session = Depends(get_db)):
    """Cria uma URL encurtada"""
    db_url = db.query(URL).filter(URL.original_url == url.original_url).first()
    if db_url:
        return db_url

    short_url = generate_short_url()
    while db.query(URL).filter(URL.short_url == short_url).first():
        short_url = generate_short_url()

    new_url = URL(original_url=str(url.original_url), short_url=str(short_url))
    db.add(new_url)
    db.commit()
    db.refresh(new_url)

    return new_url

@router.get("/{short_url}", response_model=URLResponse)
def redirect_to_url(short_url: str, db: Session = Depends(get_db)):
    db_url = db.query(URL).filter(URL.short_url == short_url).first()
    if not db_url:
        raise HTTPException(status_code=404, detail="URL not found")
    return db_url