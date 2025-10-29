from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models.author_model import Author
from schemas import AuthorCreate, AuthorResponse

router = APIRouter(
    prefix="/authors",
    tags=["Authors"]
)

# Create Author
@router.post("/", response_model=AuthorResponse)
def create_author(author: AuthorCreate, db: Session = Depends(get_db)):
    new_author = Author(name=author.name)
    db.add(new_author)
    db.commit()
    db.refresh(new_author)
    return new_author

# Get All Authors
@router.get("/", response_model=list[AuthorResponse])
def get_authors(db: Session = Depends(get_db)):
    authors = db.query(Author).all()
    return authors

# Get Author by ID
@router.get("/{author_id}", response_model=AuthorResponse)
def get_author(author_id: int, db: Session = Depends(get_db)):
    author = db.query(Author).filter(Author.id == author_id).first()
    if not author:
        raise HTTPException(status_code=404, detail="Author not found")
    return author

# Update Author
@router.put("/{author_id}", response_model=AuthorResponse)
def update_author(author_id: int, updated_author: AuthorCreate, db: Session = Depends(get_db)):
    author = db.query(Author).filter(Author.id == author_id).first()
    if not author:
        raise HTTPException(status_code=404, detail="Author not found")
    author.name = updated_author.name
    db.commit()
    db.refresh(author)
    return author

# Delete Author
@router.delete("/{author_id}")
def delete_author(author_id: int, db: Session = Depends(get_db)):
    author = db.query(Author).filter(Author.id == author_id).first()
    if not author:
        raise HTTPException(status_code=404, detail="Author not found")
    db.delete(author)
    db.commit()
    return {"message": "Author deleted successfully"}
