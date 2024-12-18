import pytest


# Constantes pour l'endpoint
CLIENT_ENDPOINT = "/api/v1/client"


@pytest.fixture
def client_data():
    """Données de test pour créer un client."""
    return {
        "nom": "Doe",
        "prenom": "John",
        "genre": "M",
        "adresse": "123 rue de la Paix",
        "complement_adresse": "Batiment b",
        "tel": "01.23.45.67.89",
        "email": "John.Doe@gmail.com",
        "newsletter": 1,
    }


@pytest.fixture
def formatted_client_data():
    """Données attendues après la création d'un client."""
    return {
        "id": 1,
        "nom": "DOE",
        "prenom": "John",
        "genre": "M",
        "adresse": "123 rue de la paix",
        "complement_adresse": "Batiment B",
        "tel": "0123456789",
        "email": "john.doe@gmail.com",
        "newsletter": 1,
    }


def assert_client_data(response_data, expected_data):
    """Fonction utilitaire pour comparer les données d'un client."""
    assert response_data["id"] == expected_data["id"]
    assert response_data["nom"] == expected_data["nom"]
    assert response_data["prenom"] == expected_data["prenom"]
    assert response_data["genre"] == expected_data["genre"]
    assert response_data["adresse"] == expected_data["adresse"]
    assert response_data["complement_adresse"] == expected_data["complement_adresse"]
    assert response_data["tel"] == expected_data["tel"]
    assert response_data["email"] == expected_data["email"]
    assert response_data["newsletter"] == expected_data["newsletter"]


def test_get_all_clients(client):
    """Tester l'obtention de tous les clients (doit renvoyer une liste vide au début)."""
    response = client.get(CLIENT_ENDPOINT)
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) == 0


def test_create_client(client, client_data, formatted_client_data):
    """Tester la création d'un client."""
    response = client.post(CLIENT_ENDPOINT, json=client_data)
    assert response.status_code == 201

    data = response.json()
    assert_client_data(data, formatted_client_data)


def test_get_client_by_id(client, client_data, formatted_client_data):
    """Tester la récupération d'un client par son ID."""
    # Créer un client d'abord
    response = client.post(CLIENT_ENDPOINT, json=client_data)
    client_id = response.json()["id"]

    # Récupérer le client par ID
    response = client.get(f"{CLIENT_ENDPOINT}/{client_id}")
    assert response.status_code == 200

    data = response.json()
    assert_client_data(data, formatted_client_data)


def test_patch_client_by_id(client, client_data):
    """Tester la mise à jour partielle des informations d'un client."""
    # Créer un client d'abord
    response = client.post(CLIENT_ENDPOINT, json=client_data)
    client_id = response.json()["id"]

    # Nouvelle donnée à mettre à jour
    new_data = {
        "nom": "Smith",
        "prenom": "Jane",
        "genre": "F",
        "adresse": "456 rue de la Paix",
        "complement_adresse": "Batiment C",
        "tel": "0712211213",
        "email": "Jane.Smith@yopmail.fr",
        "newsletter": 0
    }

    response = client.patch(f"{CLIENT_ENDPOINT}/{client_id}", json=new_data)
    assert response.status_code == 200

    updated_data = response.json()
    assert updated_data["id"] == client_id
    assert updated_data["nom"] == "SMITH"
    assert updated_data["prenom"] == "Jane"
    assert updated_data["genre"] == "F"
    assert updated_data["adresse"] == "456 rue de la paix"
    assert updated_data["complement_adresse"] == "Batiment C"
    assert updated_data["tel"] == "0712211213"
    assert updated_data["email"] == "jane.smith@yopmail.fr"
    assert updated_data["newsletter"] == 0


def test_delete_client_by_id(client, client_data):
    """Tester la suppression d'un client par son ID."""
    # Créer un client d'abord
    response = client.post(CLIENT_ENDPOINT, json=client_data)
    client_id = response.json()["id"]

    # Supprimer le client
    response = client.delete(f"{CLIENT_ENDPOINT}/{client_id}")
    assert response.status_code == 204  # Pas de contenu

    # Vérifier que le client n'existe plus
    response = client.get(f"{CLIENT_ENDPOINT}/{client_id}")
    assert response.status_code == 404
    assert response.json() == {"detail": f"Client avec l'id {client_id} introuvable."}

    # Vérifier que la liste des clients est vide
    response = client.get(CLIENT_ENDPOINT)
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) == 0
