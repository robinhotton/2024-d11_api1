# FastAPI & SQLAlchemy

## Description

Ceci est un projet de exemple pour FastAPI et SQLAlchemy pour la session 2024-D11 de Diginamic qui est une formation Cyber sécurité appliqué avec bash et python.

## Installation

### Prérequis

- Python 3.8+
- git bash

### cloner le projet

```bash
git clone https://github.com/robinhotton/2024-d11_api1.git
cd 2024-d11_api1
```

### Créer un environnement virtuel

- Windows:

    ```bash
    python -m venv .venv
    .venv\Scripts\activate
    ```

- Linux/Mac:

    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    ```

### Installer les dépendances

```bash
pip install -r requirements.txt
```

### Configuration

1. Créer la base de données avec mon SGDB préféré
2. Changer la **connection string** dans le fichier database.py

### Lancer le serveur

```bash
uvicorn src.main:app --reload
```

## Utilisation

Ouvrir un navigateur et aller à l'adresse de swagger : [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

## Auteur

Robin Hotton
