from fastapi import APIRouter, Depends, HTTPException, Header
from db import SessionLocal
from schemas import AlertCreate
from models import Alert

router = APIRouter(prefix='/alerts', tags=['alerts'])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post('/', response_model=dict)
def create_alert(payload: AlertCreate, authorization: str = Header(None)):
    if not authorization:
        raise HTTPException(status_code=401, detail='Missing authorization header')
    db = next(get_db())
    a = Alert(user_id=1, product_id=payload.product_id, target_price=payload.target_price)
    db.add(a); db.commit(); db.refresh(a)
    return {'id': a.id, 'product_id': a.product_id, 'target_price': a.target_price}
