from ..repositories import ClientRepository

class ClientService:

    @staticmethod
    def get_all_clients(db):
        return ClientRepository.get_all_clients(db)
    
    @staticmethod
    def get_client_by_id(db, id):
        return ClientRepository.get_client_by_id(db, id)
    