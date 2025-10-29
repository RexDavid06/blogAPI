# BlogAPI

A simple and secure RESTful **Blog API** built with **Django REST Framework (DRF)** and **JWT authentication**.  
It allows users to register, log in, and manage blog posts (create, read, update, delete) through protected API endpoints.

---

## ⚙️ Tech Stack

- **Python**
- **Django**
- **Django REST Framework**
- **JWT (JSON Web Token)** for authentication

---

##  Setup Instructions

###  Clone the Repository

git clone https://github.com/RexDavid06/blogAPI.git
cd blogAPI
# Create a Virtual Environment
python -m venv venv
venv\Scripts\activate   # for Windows
source venv/bin/activate   # for Mac/Linux
# Install Dependencies
pip install -r requirements.txt
# Apply Migrations
python manage.py migrate
# Run the Development Server
python manage.py runserver
# Environment Variables
Create a .env file in your project root and set the following:
SECRET_KEY=your_secret_key
DEBUG=True
(Add other environment variables if needed, e.g. database configs)

🧠 Features
User Registration & Login

JWT Authentication

CRUD operations for Blog Posts:

Create

Read (list & detail)

Update

Delete

📡 API Endpoints
🔐 Authentication
Method	Endpoint	Description
POST	api/v1/auth/register/	Register a new user
POST	api/v1/auth/login/	Log in and get JWT tokens
GET	/profile/	Retrieve user profile (Requires authentication)

📝 Blog Posts
Method	Endpoint	Description
POST	api/v1/post/create/	Create a new post
GET	api/v1/post/list/	List all posts
GET	api/v1/post/<slug:slug>/	Retrieve a single post
PUT	api/v1/post/<slug:slug>/update/	Update an existing post
DELETE	api/v1/post/<slug:slug>/delete/	Delete a post

⚠️ All post routes (except list and register) require authentication via Bearer token.

👤 Author
Buchi Rex-David
GitHub

🪪 License
This project is open-source and available under the MIT License.