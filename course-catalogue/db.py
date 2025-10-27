# course-catalogue/db.py

import os
import psycopg2

def get_db_connection():
    # Establish a new database connection using DATABASE_URL
    db_url = os.getenv("DATABASE_URL", "postgresql://course:password@course-db:5432/courses")
    conn = psycopg2.connect(db_url)
    return conn
