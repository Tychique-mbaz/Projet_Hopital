from datetime import datetime, timedelta
from typing import Optional

from fastapi import Depends, APIRouter, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from sqlalchemy.orm import Session

from database.tables.utilisateur import Compte
from database.base import get_db
from schemas.authentication import TokenData, Token


SECRET_KEY = "MIICWwIBAAKBgQCLoYAZcoA5ihLn789AMBkyDwl8s9eO0S5MhpNnAXumU1hBcbYBPGZJGQ48Ab"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

authentication_router = APIRouter()


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


async def get_compte(db: Session, username: str) -> Compte :
    return db.query(Compte).filter(Compte.username  == username).first()


async def authenticate_user(db: Session, username: str, password: str) -> Compte :
    compte = await get_compte(db, username)
    if not compte :
        return False
    if compte.passeword == password :
        return compte
    return False


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta :
        expire = datetime.utcnow() + expires_delta
    else :
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


async def get_current_user(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)) -> Compte :
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try :
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        compte: Compte = payload.get("compte")
        if compte is None:
            raise credentials_exception
        token_data = TokenData(
            username=compte['username'], 
            passeword=compte['passeword'],
            email=compte['email'],
            role=compte['role'],
            status=compte['status'],
            employe_id=compte['employe_id']
        )
        
    except JWTError :
        raise credentials_exception
    user = await get_compte(db, username=token_data.username)
    if user is None:
        raise credentials_exception
    return user


async def get_current_active_user(current_compte: Compte = Depends(get_current_user)) -> Compte :
    if current_compte.disabled :
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_compte


@authentication_router.post("/token", response_model=Token)
async def login_for_access_token(db: Session = Depends(get_db), form_data: OAuth2PasswordRequestForm = Depends()):
    compte = await authenticate_user(db, form_data.username, form_data.password)
    if not compte :
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    data_compte = {
        'username': compte.username, 
        'passeword': compte.passeword,
        'email': compte.email,
        'role': compte.role,
        'status': compte.status,
        'employe_id': compte.employe_id
    }
    access_token = create_access_token(
        data={"compte": data_compte }, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@authentication_router.get("/users/me", response_model=TokenData)
async def read_users_me(current_user: Compte = Depends(get_current_active_user)):
    return current_user