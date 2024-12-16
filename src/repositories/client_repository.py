from src.models import Client

def get_all_clients(db):
    return list(db.query(Client).all())