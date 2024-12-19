# FastAPI & SQLAlchemy

## Description

Ce projet est un exemple d'api utilisant **FastAPI** et **SQLAlchemy**. Il a été développé dans le cadre de la session 2024-D11 de Diginamic, une formation en **cybersécurité** appliquée, utilisant des technologies comme **Bash** et **Python**.

Le sujet est appliqué sur le projet **Digicheese** qui est une application de gestion de la fidélisation d'une fromagerie. L'API permet de gérer les clients, les produits et les commandes.

## Sommaire

- [Prérequis](#prérequis)
- [Dépendances](#dépendances)
- [Architecture](#architecture)
- [Installation](#installation)
  - [1. Cloner le projet](#1-cloner-le-projet)
  - [2. Créer un environnement virtuel](#2-créer-un-environnement-virtuel)
  - [3. Installer les dépendances](#3-installer-les-dépendances)
  - [4. Configuration](#4-configuration)
  - [5. Lancer le serveur](#5-lancer-le-serveur)
- [Utilisation](#utilisation)
- [Lancement des tests](#lancement-des-tests)
- [Différentes versions du projet](#différentes-versions-du-projet)
- [Auteur](#auteur)

## Prérequis

Avant de commencer, assurez-vous d'avoir les éléments suivants installés sur votre machine :

- **Python 3.8+**
- **Git & Github**

## Dépendances

Les dépendances du projet sont les suivantes :

- **FastAPI** : Framework web moderne pour construire des APIs avec Python 3.6+.
- **uvicorn** : Serveur pour démarrer l'application FastAPI.
- **Pydantic** : Bibliothèque pour la validation des données et la sérialisation des données.
- **SQLAlchemy** : Outil SQL flexible et puissant pour Python.
- **pymysql** : Pilote MySQL pour Python.
- **python-dotenv** : Module permettant de charger des variables d'environnement à partir d'un fichier `.env`.
- **pytest & httpx** : Framework de test pour Python.

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
├── test/
│   ├── __init__.py        # Fichier d'initialisation des tests
│   └── test_client.py     # Tests des routes API du client
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
2. Modifiez la **connection string** dans le fichier `database.py` pour vous connecter à votre base de données.

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

### Endpoint

- **/clients** : Gestion des clients (CRUD)
  - **GET** : Récupérer tous les clients
  - **GET** : Récupérer un client par son ID
  - **POST** : Créer un nouveau client
  - **PUT** : Mettre à jour un client
  - **DELETE** : Supprimer un client

Les autres endpoints (objets, commandes) arriveront prochainement.

## Lancement des tests

Pour lancer les tests, exécutez la commande suivante :

```bash
pytest
```

Cela lancera tous les tests unitaires et les tests d'intégration du projet contenu dans le dossier **test/**.

## Différentes versions du projet

Il y a plusieurs branches dans ce dépôt, chacune représentant une version différente du projet :

- **main** : version de base du projet (sans classes et imports relatifs)
- **classe** : ancienne version du projet utilisant des classes pour la logique métier
- **class__import__** : ancienne version du projet utilisant des classes et des imports relatifs
- **final** : version la plus avancée du projet utilisant classes et imports relatifs. Il y a aussi une gestion poussée des services et des tests d'intégration.

## Auteur

**Robin Hotton**  
Formation **Diginamic - Session 2024-D11**
