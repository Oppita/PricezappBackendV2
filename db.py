from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os

# URL de Supabase - REEMPLAZA CON TU URL
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:password@localhost:5432/pricezapp")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
