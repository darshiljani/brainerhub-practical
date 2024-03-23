# Excel Input API

The Excel Input API is a RESTful API designed to allow users to upload Excel files containing company and employee data, which is then processed and inserted into the database.

## Features

- Upload Excel files containing company and employee data.
- Process the uploaded Excel file and insert the data into the database.
- Error handling for various scenarios such as missing files, invalid file formats, and database errors.

## Requirements

- Python 3.x
- Django
- Django REST Framework
- pandas

## Setup

1. Clone the repository  
   `git clone https://github.com/darshiljani/brainerhub-practical.git`
2. Setup virtual enviornment
   - Create the environment  
     `virtualenv venv` (If virtualenv is installed)  
     `python -m venv venv` (If virtualenv is not installed)
   - Activate the environment  
     `./venv/Scripts/activate` (If using Windows)  
     `source venv/bin/activate` (If using Linux)
3. Install dependencies  
   `pip install -r requirements/local.txt`
4. Run migrations  
   `python manage.py migrate`
5. Start the development server  
   `python manage.py runserver`
6. Access the API  
   `http://localhost:8000/api/excel-input/`.

## Usage

The file `test.py` has been added as a way of testing the API using the `requests` library. The steps to run the test are :

1. Activate the virtual environment (Refer step 2 of installation)
2. `python test.py`
