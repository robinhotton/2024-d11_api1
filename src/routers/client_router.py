from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from src.database import get_db
from src.services.client_service import get_all, get_by_id, create
from src.schemas.client_schema import ClientSchema, ClientDB


router_client = APIRouter(prefix="/client", tags=["Client"])


@router_client.get("/")
def get_clients(db: Session = Depends(get_db)):
    try:
        return get_all(db)
    except HTTPException as e:
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, str(e))


@router_client.get("/{id}")
def get_client_by_id(id: int, db: Session = Depends(get_db)):
    client = get_by_id(db, id)
    if client:
        return client
    else:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Id not found")


@router_client.post("/", response_model=ClientDB)
def create_client(donnees_client: ClientSchema, db: Session = Depends(get_db)):
    return create(db, donnees_client)


@router_client.put("/")
def update_client():
    pass


@router_client.delete("/")
def delete_client():
    pass