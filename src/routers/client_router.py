from fastapi import APIRouter

router_client = APIRouter(prefix="/client", tags=["Client"])

@router_client.get("/")
def get_clients():
    return {"message": "Client"}

@router_client.post("/")
def get_clients():
    return {"message": "Client"}
