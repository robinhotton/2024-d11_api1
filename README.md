# FastAPI & SQLAlchemy

## Description

Ce projet est un exemple d'application utilisant **FastAPI** et **SQLAlchemy**. Il a été développé dans le cadre de la session 2024-D11 de Diginamic, une formation en **cybersécurité** appliquée, utilisant des technologies comme **Bash** et **Python**.

## Prérequis

Avant de commencer, assurez-vous d'avoir les éléments suivants installés sur votre machine :

- **Python 3.8+**
- **Git & Github**

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

Cela démarrera le serveur FastAPI via uvicorn, accessible à l'adresse suivante : [http://127.0.0.1:8000](http://127.0.0.1:8000).

## Utilisation

Une fois le serveur démarré, vous pouvez accéder à la documentation interactive générée automatiquement par Swagger à l'adresse suivante : [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).

Cette interface vous permettra de tester les différentes API de manière simple et intuitive.

## Auteur

**Robin Hotton**  
Formation **Diginamic - Session 2024-D11**
