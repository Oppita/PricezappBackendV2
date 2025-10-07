from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from db import engine, Base
from routers import auth, products, favorites, lists, alerts

# 🚀 Inicializar FastAPI
app = FastAPI(
    title="PRICEZAPP Backend (Auth Ready)",
    description="Backend oficial de Pricezapp con autenticación, productos, favoritos, listas y alertas.",
    version="2.0.0"
)

# 🔧 Crear tablas automáticamente
Base.metadata.create_all(bind=engine)

# 🌐 Configuración de CORS (muy importante para GitHub Pages)
# ⚠️ Si el frontend cambia de dominio, agrégalo aquí también.
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://oppita.github.io",  # Dominio del frontend (GitHub Pages)
        "https://oppita.github.io/PricezappFrontend",
        "https://oppita.github.io/PricezappFrontend/", 
        "https://pricezappfrontend.onrender.com",
        "http://localhost",
        "http://localhost:8000"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 🧩 Incluir los routers principales
app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(products.router, prefix="/products", tags=["Products"])
app.include_router(favorites.router, prefix="/favorites", tags=["Favorites"])
app.include_router(lists.router, prefix="/lists", tags=["Lists"])
app.include_router(alerts.router, prefix="/alerts", tags=["Alerts"])

# 🏠 Endpoint raíz (prueba de vida)
@app.get("/")
def root():
    return {"message": "✅ PRICEZAPP backend (auth) running", "version": "2.0.0"}

