from fastapi import APIRouter, Depends, HTTPException, Header
from db import SessionLocal
from models import Favorite
from schemas import FavoriteCreate

router = APIRouter(prefix='/favorites', tags=['favorites'])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post('/', response_model=dict)
def add_favorite(payload: FavoriteCreate, authorization: str = Header(None)):
    if not authorization:
        raise HTTPException(status_code=401, detail='Missing authorization header')
    db = next(get_db())
    fav = Favorite(user_id=1, product_id=payload.product_id)
    db.add(fav); db.commit(); db.refresh(fav)
    return {'id': fav.id, 'product_id': fav.product_id}
