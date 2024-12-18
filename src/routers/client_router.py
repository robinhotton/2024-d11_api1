from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from ..database import get_db
from ..services import ClientService
from ..schemas import ClientDB, ClientPost, ClientPatch


router_client = APIRouter(prefix="/client", tags=["Client"])


@router_client.get("/", response_model=list[ClientDB], status_code=status.HTTP_200_OK)
def get_clients(db: Session = Depends(get_db)):
    """
    Récupère la liste de tous les clients.
    """
    try:
        return ClientService.get_all_clients(db)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Erreur lors de la récupération des clients: {str(e)}"
        )


@router_client.get("/{id}", response_model=ClientDB, status_code=status.HTTP_200_OK)
def get_client_by_id(id: int, db: Session = Depends(get_db)):
    """
    Récupère un client par son identifiant.
    """
    client = ClientService.get_client_by_id(db, id)
    if not client:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Client avec l'id {id} introuvable."
        )
    return client


@router_client.post("/", response_model=ClientDB, status_code=status.HTTP_201_CREATED)
def create_client(donnees_client: ClientPost, db: Session = Depends(get_db)):
    """
    Crée un nouveau client.
    """
    try:
        return ClientService.create_client(db, donnees_client)
    except ValueError as ve:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Erreur de validation des données: {str(ve)}"
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Erreur lors de la création du client: {str(e)}"
        )


@router_client.patch("/{id}", response_model=ClientDB, status_code=status.HTTP_200_OK)
def update_client(id: int, donnees_client: ClientPatch, db: Session = Depends(get_db)):
    """
    Met à jour partiellement un client par son identifiant.
    """
    client = ClientService.get_client_by_id(db, id)
    if not client:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Client avec l'id {id} introuvable."
        )
    try:
        return ClientService.patch_client_by_id(db, id, donnees_client)
    except ValueError as ve:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Erreur de validation des données: {str(ve)}"
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Erreur lors de la mise à jour du client: {str(e)}"
        )


@router_client.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_client(id: int, db: Session = Depends(get_db)):
    """
    Supprime un client par son identifiant.
    """
    client = ClientService.get_client_by_id(db, id)
    if not client:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Client avec l'id {id} introuvable."
        )
    try:
        ClientService.delete_client_by_id(db, id)
        return {"message": f"Client avec l'id {id} supprimé avec succès."}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Erreur lors de la suppression du client: {str(e)}"
        )