from fastapi import FastAPI
from app.api.endpoints import router
from app.db.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Simple url shortener api")
app.include_router(router=router)



