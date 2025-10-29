from pydantic import BaseModel
from typing import List, Optional

# ---------------- Author ----------------
class BookBase(BaseModel):
    title: str
    author_id: int

class BookCreate(BookBase):
    pass

class ReviewBase(BaseModel):
    content: str
    book_id: int

class ReviewCreate(ReviewBase):
    pass

# --- Nested Responses ---
class ReviewResponse(ReviewBase):
    id: int
    class Config:
        from_attributes = True

class BookResponse(BookBase):
    id: int
    reviews: List[ReviewResponse] = []
    class Config:
        from_attributes = True

class AuthorBase(BaseModel):
    name: str

class AuthorCreate(AuthorBase):
    pass

class AuthorResponse(AuthorBase):
    id: int
    books: List[BookResponse] = []
    class Config:
        from_attributes = True
