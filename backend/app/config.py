import os
from dotenv import load_dotenv

# This tells the computer to go look in the .env file
load_dotenv()

class Settings:
    REPLICATE_API_TOKEN = os.getenv("REPLICATE_API_TOKEN")
    STRIPE_SECRET_KEY = os.getenv("STRIPE_SECRET_KEY")
    AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
    S3_UPLOAD_BUCKET = os.getenv("S3_UPLOAD_BUCKET")

settings = Settings()