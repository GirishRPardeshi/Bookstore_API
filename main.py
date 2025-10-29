from fastapi import FastAPI
from routers import books, authors, reviews
from database import engine, Base
from models import *

app = FastAPI(title="Bookstore API")

# Create all tables
Base.metadata.create_all(bind=engine)

# Include routers
app.include_router(books.router)
app.include_router(authors.router)
app.include_router(reviews.router)

@app.get("/")
def root():
    return {"message": "Welcome to the Bookstore API (with Database)"}
