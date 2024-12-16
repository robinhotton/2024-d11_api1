from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from src.database import get_db
from src.services.client_service import get_all, get_by_id


router_client = APIRouter(prefix="/client", tags=["Client"])


@router_client.get("/")
def get_clients(db: Session = Depends(get_db)):
    try:
        return get_all(db)
    except:
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR)


@router_client.get("/{id}")
def get_client_by_id(id: int, db: Session = Depends(get_db)):
    return get_by_id(db, id)
