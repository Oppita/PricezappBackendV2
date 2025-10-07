from fastapi import FastAPI
from db import engine, Base
from routers import auth, products, favorites, lists, alerts
from fastapi.middleware.cors import CORSMiddleware

# Inicializar FastAPI
app = FastAPI(title="PRICEZAPP Backend (Auth Ready)")

# Crear las tablas de la base de datos
Base.metadata.create_all(bind=engine)

# ✅ Configuración de CORS corregida
# Nota: No se puede usar "*" con allow_credentials=True
# Por eso, definimos explícitamente los dominios permitidos
origins = [
    "https://oppita.github.io",                     # 🌐 Frontend (GitHub Pages)
    "https://pricezappbackendv2.onrender.com",      # Backend desplegado (Render)
    "http://localhost:8000",                        # Local (para pruebas)
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,          # Dominios autorizados
    allow_credentials=True,         # Permite tokens/cookies
    allow_methods=["*"],            # Permite todos los métodos (GET, POST, PUT, DELETE)
    allow_headers=["*"],            # Permite todos los headers
)

# ✅ Incluir routers (rutas de la API)
app.include_router(auth.router)
app.include_router(products.router)
app.include_router(favorites.router)
app.include_router(lists.router)
app.include_router(alerts.router)

# ✅ Ruta raíz para verificación rápida del estado del backend
@app.get("/")
def root():
    return {"message": "PRICEZAPP backend (auth) running ✅"}

# Puedes probar que todo funciona accediendo a:
# https://pricezappbackendv2.onrender.com/
# o ver la documentación interactiva en:
# https://pricezappbackendv2.onrender.com/docs
