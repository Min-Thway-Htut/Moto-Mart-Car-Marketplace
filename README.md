mu77# End-to-End-Computer-Science-Project

## MotoMart Car Marketplace

## Project Overview
MotoMart is a car marketplace on which you can sell your cars just by uploading its images and related information. Similarly, you can view the items uploaded by other users in case you are interested in buying car.

### Included Features
- User Authentication (Login/Logout)
- Car Information Submission
- Car Marketplace
- Search by Name
- Search by Ascending Order
- Search by Descending Order
- Pagination
- Profile Section
- F&Qs Section
- Contact Section (users can send messages to the support team directly via email)
- Responsive Design
- Dark/Light Mode

## Tech Stack

- Frontend - Django HTML Template, CSS, Bootstrap Framework, and JavaScript
- Backend - Python Django Framework
- Database - SQLite

## Installation

```bash
# Clone the repository
git clone https://github.com/Min-Thway-Htut/End-to-End-Computer-Science-Project.git

# Initialize the virtual environment
source env/bin/activate (on Linux)
.\env\Scripts\Activate.ps1 (on Windows)

# Navigate to the directory
cd carmarket

# Install necessary packages
pip install -r requirements.txt

# Start the project

# For development
python3 manage.py runserver

# For production
gunicorn carmarket.wsgi:application


