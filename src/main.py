# importer fastapi
from fastapi import FastAPI
from .database import engine
from .models import Base
from .routers import router

# definir les routes
app = FastAPI()
app.include_router(router)

# importer engine(database.py) et Base(models.py)
Base.metadata.create_all(engine)


@app.get("/")
def home():
    return {"message": "Bienvenue sur l'API de gestion de clients et de commandes de Digicheese!"}