from fastapi import FastAPI
from db import engine, Base
from routers import auth, products, favorites, lists, alerts
from fastapi.middleware.cors import CORSMiddleware

# ✅ Inicialización
app = FastAPI(title="PRICEZAPP Backend (Auth Ready)")

# ✅ Crear tablas si no existen
Base.metadata.create_all(bind=engine)

# ✅ Lista explícita de dominios permitidos
origins = [
    "https://oppita.github.io",                   # Frontend (GitHub Pages)
    "https://oppita.github.io/PricezappFrontend", # Subruta (si la usas así)
    "https://pricezappbackendv2.onrender.com",    # Backend (Render)
    "http://localhost:8000",                      # Local dev
]

# ✅ Middleware de CORS corregido
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["*"],
)

# ✅ Incluir routers de tu app
app.include_router(auth.router)
app.include_router(products.router)
app.include_router(favorites.router)
app.include_router(lists.router)
app.include_router(alerts.router)

# ✅ Ruta raíz
@app.get("/")
def root():
    return {"message": "PRICEZAPP backend (auth) running ✅"}
