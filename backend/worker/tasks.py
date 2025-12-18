from celery import Celery
import os

celery_app = Celery('tasks', broker=os.getenv("REDIS_URL"))

@celery_app.task
def make_my_avatar(job_id, image_url, style):
    print(f"Starting AI job {job_id}...")
    return "Your AI Headshot is Cooking! 🍳"