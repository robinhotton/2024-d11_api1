from sqlalchemy.orm import Session
from ..models import Client
from typing import List


class ClientRepository:

    @staticmethod
    def get_all_clients(db: Session) -> List[Client]:
        return list(db.query(Client).all())


    @staticmethod
    def get_client_by_id(db: Session, id: int) -> Client:
        return db.query(Client).get(id)


    @staticmethod
    def create_client(db: Session, donnees_client: dict) -> Client:
        client = Client(**donnees_client)
        db.add(client)
        db.commit()
        db.refresh(client)
        return client
    
    
    @staticmethod
    def patch_client_by_id(db: Session, id: int, donnees_client: dict) -> Client:
        client = db.query(Client).get(id)
        for key, value in donnees_client.items():
            setattr(client, key, value)
        db.commit()
        db.refresh(client)
        return client
    
    
    @staticmethod
    def delete_client_by_id(db: Session, id: int) -> Client:
        client = db.query(Client).get(id)
        db.delete(client)
        db.commit()
        return client
