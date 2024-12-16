from src.repositories.client_repository import get_all_clients, get_client_by_id, create_client
from src.schemas.client_schema import ClientSchema

def get_all(db):
    return get_all_clients(db)

def get_by_id(db, id):
    return get_client_by_id(db, id)

def create(db, donnees_client: ClientSchema):
    donnees_client = donnees_client.model_dump()
    donnees_client["nomcli"] =  donnees_client["nomcli"].upper()
    donnees_client["prenomcli"] =  donnees_client["prenomcli"].capitalize()
    return create_client(db, donnees_client)