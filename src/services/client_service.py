from sqlalchemy.orm import Session
from ..repositories import ClientRepository
from ..schemas import ClientPatch, ClientPost


class ClientService:
    
    @staticmethod
    def _clean_string(value: str, transform: callable = None) -> str:
        """
        Nettoie une chaîne en appliquant une transformation donnée.
        Retourne None si la valeur est vide ou None.
        """
        if not value:
            return None
        value = value.strip()
        return transform(value) if transform else value


    @staticmethod
    def _format_data(data: dict) -> dict:
        """
        Nettoie et transforme les données d'entrée pour le format attendu.
        """
        # Nettoyage et transformation des chaînes
        data["nom"] = ClientService._clean_string(data.get("nom"), str.upper)
        data["prenom"] = ClientService._clean_string(data.get("prenom"), str.capitalize)
        data["genre"] = ClientService._clean_string(data.get("genre"), str.capitalize)
        data["adresse"] = ClientService._clean_string(data.get("adresse"), str.capitalize)
        data["complement_adresse"] = ClientService._clean_string(data.get("complement_adresse"), str.title)
        data["email"] = ClientService._clean_string(data.get("email"), str.lower)
        
        # Formatage du numéro de téléphone
        tel = ClientService._clean_string(data.get("tel"))
        if tel:
            tel = tel.replace(" ", "").replace("-", "").replace(".", "")
            if not tel.startswith("0") or len(tel) != 10 or not tel.isdigit():
                raise ValueError("Le numéro de téléphone doit commencer par 0 et être composé de 10 chiffres")
        data["tel"] = tel

        # Suppression des clés pour les valeurs vides
        result = {k: v for k, v in data.items() if v}
        
        # ajout de la clé newsletter (car supprimée si False avec la ligne précédente)
        result["newsletter"] = 1 if result.get("newsletter") else 0
        return result


    @staticmethod
    def get_all_clients(db: Session):
        return ClientRepository.get_all_clients(db)


    @staticmethod
    def get_client_by_id(db: Session, id):
        return ClientRepository.get_client_by_id(db, id)


    @staticmethod
    def create_client(db: Session, donnees_client: ClientPost):
        donnees_client = donnees_client.model_dump()
        data_formated = ClientService._format_data(donnees_client)
        return ClientRepository.create_client(db, data_formated)
    
    
    @staticmethod
    def patch_client_by_id(db: Session, id: int, donnees_client: ClientPatch):
        donnees_client = donnees_client.model_dump()
        data_formated = ClientService._format_data(donnees_client)
        return ClientRepository.patch_client_by_id(db, id, data_formated)
    
    
    @staticmethod
    def delete_client_by_id(db: Session, id: int):
        return ClientRepository.delete_client_by_id(db, id)
