from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from db import engine, Base
import os

app = FastAPI(title='PRICEZAPP Backend')

# Create tables if they don't exist
Base.metadata.create_all(bind=engine)

# CORS - adjust origins in production
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://oppita.github.io",
        "http://localhost:8000",
        "http://localhost:3000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# import routers after app creation
from routers import auth, products, favorites, lists, alerts  # noqa: E402

app.include_router(auth.router)
app.include_router(products.router)
app.include_router(favorites.router)
app.include_router(lists.router)
app.include_router(alerts.router)


@app.get('/')
def root():
    return { 'message': 'PRICEZAPP backend (auth) running' }


@app.get('/health')
def health():
    return { 'status': 'healthy' }

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=int(os.environ.get('PORT', 10000)))

