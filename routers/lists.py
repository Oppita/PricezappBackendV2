from fastapi import APIRouter, Depends, HTTPException, Header
from db import SessionLocal
from schemas import ShoppingListCreate
from models import ShoppingList

router = APIRouter(prefix='/lists', tags=['lists'])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post('/', response_model=dict)
def create_list(payload: ShoppingListCreate, authorization: str = Header(None)):
    if not authorization:
        raise HTTPException(status_code=401, detail='Missing authorization header')
    db = next(get_db())
    nl = ShoppingList(user_id=1, name=payload.name, items=payload.items)
    db.add(nl); db.commit(); db.refresh(nl)
    return {'id': nl.id, 'name': nl.name, 'items': nl.items}

