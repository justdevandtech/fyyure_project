import os
SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

# Connect to the database


# TODO IMPLEMENT DATABASE URL
DB_HOST = os.getenv('DB_HOST','127.0.0.1:5432')
DB_USER = os.getenv('DB_USER','postgres')
DB_PASSWORD = os.getenv('DB_PASSWORD','postgres')
DB_NAME = os.getenv('DB_NAME','practical_db')
SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@localhost:5432/practical_db'
