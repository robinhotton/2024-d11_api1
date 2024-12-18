from sqlalchemy import Column, Integer, String, Date, ForeignKey, Index, Numeric, Float
from sqlalchemy.ext.declarative import declarative_base

# déclaration d'une base qui permet après de créer un modele et de mapper avec sql alchemy
Base = declarative_base()

# classe permettant de définir les modèles de la base de données pour créer ou accéder aux tables
# hérite de la base définie dans database.py

class Client(Base):
	__tablename__ = "t_client"

	id = Column(Integer, primary_key=True)
	nom = Column(String(40), index=True)
	prenom = Column(String(30))
	genre = Column(String(8), default=None)
	adresse = Column(String(50))
	complement_adresse = Column(String(50), default=None)
	tel = Column(String(10), default=None)
	email = Column(String(255), default=None)
	newsletter = Column(Integer, default=0)


class Commande(Base):
	__tablename__ = "t_entcde"

	codcde = Column(Integer,primary_key=True)
	datcde = Column(Date)
	codcli = Column(Integer,ForeignKey('t_client.id'))
	timbrecli = Column(Float)
	timbrecde = Column(Float)
	cheqcli = Column(Float)
	cdeComt = Column(String(255), default=None)

	__table_args__ = (Index('commmande_index', "cdeComt", "codcli"),)


class Objet(Base):
	__tablename__ = "t_objet"

	codobj = Column(Integer,primary_key=True)
	libobj = Column(String(50), default=None)
	tailleobj = Column(String(50), default=None)
	puobj = Column(Numeric, default=0.0000)
	poidsobj = Column(Numeric, default=0.0000)
	indispobj = Column(Integer, default=0)
	points = Column(Integer, default=0)


class Detail(Base):
	__tablename__ = "t_dtlcode"

	id = Column(Integer,primary_key=True)
	codcde = Column(Integer,ForeignKey('t_entcde.codcde'), index=True)
	objet_id = Column(Integer, ForeignKey('t_objet.codobj'))
	qte = Column(Integer, default=1)
	commentaire = Column(String(100), default=None)
 