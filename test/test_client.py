from fastapi.testclient import TestClient
from src.main import app


client = TestClient(app)

# changer de base de données : sqlite
# pour notre cas pas besoin de changer de bdd


def test_get_all_clients():
    response = client.get("/client/")
    assert response.status_code == 200 # success
    assert isinstance(response.json(), list)
    
    
def test_get_client_by_id():
    pass


def test_create_client():
    pass