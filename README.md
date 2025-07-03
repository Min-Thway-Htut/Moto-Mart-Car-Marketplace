# End-to-End-Computer-Science-Project

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
- Autocomplete Search Functionality
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
- Docker - DevOps

## Installation

### Please follow these instructions to run the application on Windows

```bash
# Clone the repository
git clone https://github.com/Min-Thway-Htut/End-to-End-Computer-Science-Project.git

# Navigate to the directory
cd End-to-End-Computer-Science-Project

# Create a virtual environment
python3 -m venv venv

# Initialize the virtual environment
./venv/Scripts/activate

# Navigate to the directory
cd carmarket

# Create a .env file and add environment variables.
# The contents of .env file can be view in .env.example file.

# Install necessary packages
pip install -r requirements.txt

# Start the project
python3 manage.py runserver

```

### Please follow these instructions to run the application on Linux

```bash
# Clone the repository
git clone https://github.com/Min-Thway-Htut/End-to-End-Computer-Science-Project.git

# Navigate to the directory
cd End-to-End-Computer-Science-Project

# Create a virtual environment
python3 -m venv venv

# Initialize a virtual environment
source venv/bin/activate

# Navigate to the directory
cd carmarket

# Create a .env file and add environment variables.
# The contents of .env file can be view in .env.example file.

# Install necessary packages
pip install -r requirements.txt

# For development
python3 manage.py runserver

# For production
gunicorn carmarket.wsgi:application --bind 0.0.0.0:8080

```

### Please follow these instructions to run the application using Docker

```bash

# Clone the repository
git clone https://github.com/Min-Thway-Htut/End-to-End-Computer-Science-Project.git

# Navigate to the directory
cd End-to-End-Computer-Science-Project

# Create a virtual environment
python3 -m venv venv

# Initialize a virtual environment
source venv/bin/activate

# Navigate to the directory
cd carmarket

# Create a .env file and add environment variables.
# The contents of .env file can be view in .env.example file.

# Install necessary packages
pip install -r requirements.txt

# Build the image and start the containers
sudo docker-compose up --build -d

# Start the containers (without rebuilding the image)
sudo docker-compose up -d

```

The application will be running at http://localhost:8000/ .
