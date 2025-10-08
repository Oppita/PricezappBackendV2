import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = os.getenv('postgresql://postgres:Virumafia123%2A@db.mkqrkjjalxvyibpqjrtt.supabase.co:5432/postgres', '')

# supabase sometimes provides URL starting with 'postgres://'
if DATABASE_URL.startswith('postgres://'):
    DATABASE_URL = DATABASE_URL.replace('postgres://', 'postgresql://', 1)

# Fallback to sqlite for local/testing if not provided
if not DATABASE_URL:
    DATABASE_URL = 'sqlite:///./pricezapp.db'

engine = create_engine(DATABASE_URL, connect_args={'check_same_thread': False} if DATABASE_URL.startswith('sqlite') else {})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
