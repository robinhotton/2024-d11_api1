from src.models import Client
from sqlalchemy.orm import Session

def get_all_clients(db: Session):
    return list(db.query(Client).all())

def get_client_by_id(db: Session, id: int):
    return db.query(Client).get(id)