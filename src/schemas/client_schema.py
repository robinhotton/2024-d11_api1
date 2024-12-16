from pydantic import BaseModel
from typing import Optional


class ClientSchema(BaseModel):
    prenomcli:Optional[str] = None
    nomcli:str
    
    
class ClientDB(ClientSchema):
    codcli: int