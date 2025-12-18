from sqlalchemy import create_column, String, Integer, DateTime, JSON
from sqlalchemy.orm import declarative_base
from datetime import datetime

Base = declarative_base()

class Job(Base):
    __tablename__ = "jobs"
    id = Integer(primary_key=True)
    user_id = String()
    status = String(default="pending") # pending, processing, completed
    style = String()
    output_urls = JSON() # This stores the final AI links
    created_at = DateTime(default=datetime.utcnow)