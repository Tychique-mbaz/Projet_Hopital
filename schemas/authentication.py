from pydantic import BaseModel
from typing import Optional
from schemas.utilisateur import CompteSchema, CompteUpdateSchema
from datetime import datetime



class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None
    passeword: Optional[str] = None
    date_derniere_connexion: Optional[datetime] = datetime.now()
    email: Optional[str] = None
    role: Optional[str] = None
    status: Optional[str] = None         
    employe_id: Optional[int] = None


class User(BaseModel):
    id: int
    username: str
    email: str
    full_name: str
    disabled: bool

