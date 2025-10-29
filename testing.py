import requests

BASE = "http://127.0.0.1:8000"

# Create author
requests.post(f"{BASE}/authors/", json={"id": 1, "name": "J.K. Rowling"})

# Create book
requests.post(f"{BASE}/books/", json={
    "id": 1,
    "title": "Harry Potter",
    "author_id": 1,
    "price": 499.99
})

# Create review
requests.post(f"{BASE}/reviews/", json={
    "id": 1,
    "book_id": 1,
    "rating": 5,
    "comment": "Magical story!"
})

# Fetch all books
res = requests.get(f"{BASE}/books/")
print(res.json())


 