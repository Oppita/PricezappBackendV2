from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="PriceZapp API", version="2.0")

# CORS para GitHub Pages
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # En producción especifica tu dominio GitHub Pages
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Importar routers DESPUÉS de crear app
from routers import auth, products, favorites, lists, alerts

app.include_router(auth.router)
app.include_router(products.router)
app.include_router(favorites.router)
app.include_router(lists.router)
app.include_router(alerts.router)

@app.get("/")
def root():
    return {"message": "✅ PriceZapp API Running", "status": "healthy"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}
