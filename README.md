# FastAPI & SQLAlchemy

## Description

Ce projet est un exemple d'application utilisant **FastAPI** et **SQLAlchemy**. Il a été développé dans le cadre de la session 2024-D11 de Diginamic, une formation en **cybersécurité** appliquée, utilisant des technologies comme **Bash** et **Python**.

## Prérequis

Avant de commencer, assurez-vous d'avoir les éléments suivants installés sur votre machine :

- **Python 3.8+**
- **Git & Github**

## Architecture

Le projet est structuré de la manière suivante :

```bash
2024-d11_api1/
│
├── src/
│   ├── main.py            # Point d'entrée principal de l'application
│   ├── database.py        # Configuration et gestion de la base de données
│   ├── models.py          # Définition des modèles de données (tables)
│   ├── Repositories/      # Contient les classes pour accéder aux données (logique d'accès à la BDD)
│   ├── services/          # Contient la logique métier de l'application
│   ├── schemas/           # Définitions des schémas de validation des données (Pydantic)
│   └── routers/           # Contient les routes API (endpoints)
│
├── .gitignore             # Fichier de configuration Git pour ignorer certains fichiers/dossiers
├── README.md              # Documentation du projet
├── requirements.txt       # Liste des dépendances du projet
├── .venv/                 # Environnement virtuel Python
└── .env                   # Fichier de configuration des variables d'environnement
```

## Installation

### 1. Cloner le projet

Clonez le projet depuis GitHub :

```bash
git clone https://github.com/robinhotton/2024-d11_api1.git
cd 2024-d11_api1
```

### 2. Créer un environnement virtuel

#### Sous Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

#### Sous Linux/MacOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Installer les dépendances

Installez les bibliothèques nécessaires en exécutant la commande suivante :

```bash
pip install -r requirements.txt
```

### 4. Configuration

1. Créez une base de données avec votre Système de Gestion de Base de Données (SGDB) préféré.
2. Modifiez les **variables d'environnement** dans le fichier `.env` pour vous connecter à votre base de données.

### 5. Lancer le serveur

Pour démarrer le serveur de développement, exécutez la commande suivante :

```bash
uvicorn src.main:app --reload
```

alternativement, vous pouvez exécuter le script `run.py` pour démarrer le serveur :

```bash
python run.py
```

Cela démarrera le serveur FastAPI via uvicorn, accessible à l'adresse suivante : [http://127.0.0.1:8000](http://127.0.0.1:8000).

## Utilisation

Une fois le serveur démarré, vous pouvez accéder à la documentation interactive générée automatiquement par Swagger à l'adresse suivante : [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).

Cette interface vous permettra de tester les différentes API de manière simple et intuitive.

## Lancement des tests

Pour lancer les tests, exécutez simplement la commande suivante dans votre terminal :

```bash
pytest
```

### Informations complémentaires

- **Emplacement des tests** : Tous les tests sont situés dans le dossier `tests/`.
- **Serveur** : Il n'est pas nécessaire de démarrer le serveur pour exécuter les tests. Les tests sont exécutés directement via des requêtes HTTP simulées.
- **Base de données de test** : Les tests utilisent une base de données SQLite qui est stockée dans le fichier `test.db`. Cela permet de tester sans interférer avec la base de données de développement ou de production.
- **Isolation des tests** : Chaque test utilise une nouvelle instance de la base de données afin d'assurer l'isolement des tests et de garantir des résultats cohérents.

## Auteur

**Robin Hotton**  
Formation **Diginamic - Session 2024-D11**
