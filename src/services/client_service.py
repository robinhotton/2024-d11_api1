from src.repositories.client_repository import get_all_clients, get_client_by_id


def get_all(db):
    return get_all_clients(db)

def get_by_id(db, id):
    return get_client_by_id(db, id)