from sqlalchemy import Column, Integer, String, Date, ForeignKey, Index, Numeric, Float
from sqlalchemy.ext.declarative import declarative_base

# déclaration d'une base qui permet après de créer un modele et de mapper avec sql alchemy
Base = declarative_base()

# classe permettant de définir les modèles de la base de données pour créer ou accéder aux tables
# hérite de la base définie dans database.py

class Client(Base):
	__tablename__ = "t_client"

	codcli = Column(Integer,primary_key=True)
	genrecli = Column(String(8), default=None)
	nomcli = Column(String(40), default=None, index=True)
	prenomcli = Column(String(30), default=None)
	adresse1cli = Column(String(50), default=None)
	adresse2cli = Column(String(50), default=None)
	adresse3cli = Column(String(50), default=None)
	# villecli_id = Column(Integer,ForeignKey('t_communes.id'))
	telcli = Column(String(10), default=None)
	emailcli = Column(String(255), default=None)
	portcli = Column(String(10), default=None)
	newsletter = Column(Integer, default=0)


class Commande(Base):
	__tablename__ = "t_entcde"

	codcde = Column(Integer,primary_key=True)
	datcde = Column(Date)
	codcli = Column(Integer,ForeignKey('t_client.codcli'))
	timbrecli = Column(Float)
	timbrecde = Column(Float)
	# nbcolis = Column(Integer, default=1)
	cheqcli = Column(Float)
	# idcondit = Column(Integer, default=0)
	cdeComt = Column(String(255), default=None)
	# barchive = Column(Integer, default=0)
	# bstock = Column(Integer, default=0)

	__table_args__ = (Index('commmande_index', "cdeComt", "codcli"),)


class Objet(Base):
	__tablename__ = "t_objet"

	codobj = Column(Integer,primary_key=True)
	libobj = Column(String(50), default=None)
	tailleobj = Column(String(50), default=None)
	puobj = Column(Numeric, default=0.0000)
	poidsobj = Column(Numeric, default=0.0000)
	indispobj = Column(Integer, default=0)
	# o_imp = Column(Integer, default=0)
	# o_aff = Column(Integer, default=0)
	# o_cartp = Column(Integer, default=0)
	points = Column(Integer, default=0)
	# o_ordre_aff = Column(Integer, default=0)
	# condit = relationship("ObjetCond",back_populates='objets')


class Detail(Base):
	__tablename__ = "t_dtlcode"

	id = Column(Integer,primary_key=True)
	codcde = Column(Integer,ForeignKey('t_entcde.codcde'), index=True)
	objet_id = Column(Integer, ForeignKey('t_objet.codobj'))
	qte = Column(Integer, default=1)
	# colis = Column(Integer, default=1)
	commentaire = Column(String(100), default=None)
 