from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from db import SessionLocal
from models import User
from schemas import UserCreate, UserOut, Token, UserLogin
from passlib.context import CryptContext
from jose import jwt, JWTError
from datetime import datetime, timedelta
from fastapi.security import OAuth2PasswordBearer

router = APIRouter(prefix='/auth', tags=['auth'])

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')
SECRET_KEY = __import__('os').environ.get('SECRET_KEY', 'change_this_in_prod')
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24 * 7

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='auth/login')

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def verify_password(plain, hashed):
    try:
        return pwd_context.verify(plain, hashed)
    except Exception:
        return False

def get_password_hash(password):
    # truncate long passwords for bcrypt safety
    pw = password
    if isinstance(pw, str) and len(pw.encode('utf-8')) > 72:
        pw = pw.encode('utf-8')[:72].decode('utf-8', errors='ignore')
    return pwd_context.hash(pw)

def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({'exp': expire})
    encoded = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded

@router.post('/register', response_model=UserOut)
def register(payload: UserCreate, db: Session = Depends(get_db)):
    existing = db.query(User).filter(User.email == payload.email).first()
    if existing:
        raise HTTPException(status_code=400, detail='Email already registered')
    hashed = get_password_hash(payload.password)
    user = User(name=payload.name, email=payload.email, hashed_password=hashed)
    db.add(user); db.commit(); db.refresh(user)
    return user

@router.post('/login', response_model=Token)
def login(payload: UserLogin, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == payload.email).first()
    if not user:
        raise HTTPException(status_code=401, detail='Incorrect email or password')
    if not verify_password(payload.password, user.hashed_password):
        raise HTTPException(status_code=401, detail='Incorrect email or password')
    expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    token = create_access_token({'sub': user.email, 'user_id': user.id}, expires_delta=expires)
    return {'access_token': token, 'token_type': 'bearer'}

@router.get('/me', response_model=UserOut)
def me(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(status_code=401, detail='Could not validate credentials')
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get('sub')
        if email is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user = db.query(User).filter(User.email == email).first()
    if not user:
        raise HTTPException(status_code=404, detail='User not found')
    return user

