import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'mysecretkey')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'mysql+pymysql://root:123321@localhost/social_sips?charset=utf8mb4')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'myjwtsecretkey')
    JWT_ACCESS_TOKEN_EXPIRES  = os.getenv('JWT_ACCESS_TOKEN_EXPIRES', 28800)
    JWT_TOKEN_LOCATION = ['headers']