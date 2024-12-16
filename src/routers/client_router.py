from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from ..database import get_db
from ..services import ClientService


router_client = APIRouter(prefix="/client", tags=["Client"])


@router_client.get("/")
def get_clients(db: Session = Depends(get_db)):
    return ClientService.get_all_clients(db)


@router_client.get("/{id}")
def get_client_by_id(id: int, db: Session = Depends(get_db)):
    try:
        return ClientService.get_client_by_id(db, id)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    