from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from db import engine, Base
from routers import auth, products, favorites, lists, alerts

# ========================================
# ✅ Configuración CORS (antes de cualquier router)
# ========================================
app = FastAPI(title="PRICEZAPP Backend (Auth Ready)")

origins = [
    "https://oppita.github.io",
    "https://oppita.github.io/PricezappFrontend",
    "https://pricezappbackendv2.onrender.com",
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ========================================
# ✅ Inicialización DB
# ========================================
Base.metadata.create_all(bind=engine)

# ========================================
# ✅ Incluir routers
# ========================================
app.include_router(auth.router)
app.include_router(products.router)
app.include_router(favorites.router)
app.include_router(lists.router)
app.include_router(alerts.router)

@app.get("/")
def root():
    return {"message": "PRICEZAPP backend (auth) running ✅"}
