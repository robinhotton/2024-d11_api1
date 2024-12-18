from pydantic import BaseModel, EmailStr
from typing import Optional


class ClientBase(BaseModel):
    nom: str
    prenom: str
    genre: Optional[str] = None
    adresse: str
    complement_adresse: Optional[str] = None
    tel: Optional[str] = None
    email: Optional[EmailStr] = None
    newsletter: Optional[int] = 0
    

class ClientPatch(ClientBase):
    nom: Optional[str] = None
    prenom: Optional[str] = None
    adresse: Optional[str] = None


class ClientPost(ClientBase):
    pass

    
class ClientDB(ClientBase):
    id: int
    
    class Config:
        from_attributes = True
