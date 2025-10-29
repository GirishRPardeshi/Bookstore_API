# 📚 Bookstore API  

A RESTful API built with **FastAPI**, providing CRUD operations for managing books, authors, and reviews. Designed for scalability, modularity, and easy database integration using **SQLAlchemy ORM**.

---

## 🚀 Features
- Add, view, update, and delete **Books**, **Authors**, and **Reviews**  
- Proper **database relationships** (One-to-Many) between Authors → Books → Reviews  
- Clean **project structure** using `routers/` and `models/` folders  
- **Pydantic models** for request validation and response formatting  
- Database managed via **SQLAlchemy ORM**  
- **Environment-based configuration** with `.env` file  
- **Automatic schema creation** on startup  
- API tested manually with tools like **Postman** and **Thunder Client**

---

## 🧩 Project Structure
bookstore_api/
│
├── main.py
├── database.py
├── .env
├── .gitignore
│
├── models/
│ ├── book_model.py
│ ├── author_model.py
│ └── review_model.py
│
├── routers/
│ ├── book_router.py
│ ├── author_router.py
│ └── review_router.py
│
└── requirements.txt


---

## ⚙️ Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/GirishRPardeshi/Bookstore_API.git
   cd Bookstore_API


2. **Create a virtual environment**
```bash
python -m venv venv
venv\Scripts\activate


3. **Install dependencies**
```bash
pip install -r requirements.txt


4. **Run the API**
```bash
uvicorn main:app --reload

**🌐 API Endpoints**
Method	Endpoint	Description
GET	/books/	Get all books
POST	/books/	Add new book
GET	/books/{id}	Get a book by ID
PUT	/books/{id}	Update a book
DELETE	/books/{id}	Delete a book
GET	/authors/	List authors
POST	/authors/	Add author
GET	/reviews/	View all reviews

**🛠️ Tools Used**

FastAPI — high-performance API framework

Uvicorn — ASGI web server

SQLAlchemy — ORM for database management

Pydantic — data validation

Postman / Thunder Client — API testing

**📖 Future Enhancements**

JWT Authentication for users

Pagination and filtering for books

Async database operations

Docker containerization

**👨‍💻 Author**

Girish R. Pardeshi
FastAPI Developer & MCA Student
