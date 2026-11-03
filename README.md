# Python version 
Python 3.13.0

# Create virtual environment
(windows)
python -m venv venv

# Activate virtual environment
venv/Scripts/activate

# Create Database (postgresql)
eg: contactform_db

# configure .env
DATABASE_URL = postgresql+asyncpg://postgres:password@localhost:5432/contactform_db

# To run the application
uvicorn main:app --reload