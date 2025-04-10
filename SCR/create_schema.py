import sqlite3
import pandas as pd
import os

# Créer le répertoire pour la base de données
db_path = "/app/BD/database.sqlite"
os.makedirs(os.path.dirname(db_path), exist_ok=True)

# Connexion à la base de données (création si elle n'existe pas)
conn = sqlite3.connect(db_path)
cursor = conn.cursor()
 
#créer les tables pour  vente  (si elles n'existent pas)
cursor.execute('''CREATE TABLE IF NOT EXISTS VENTES (
  "Date" DATE,
  "ID Référence produit" VARCHAR(255) PRIMARY KEY,
  "Quantité" INTEGER,
  "ID Magasin" INTEGER)
  ''')

#créer les tables pour  magasin  (si elles n'existent pas)
cursor.execute('''CREATE TABLE IF NOT EXISTS magasins (
  
  "ID Magasin" INTEGER PRIMARY KEY ,
  "Ville"  VARCHAR(255),
  "Nombre de salariés" INTEGER
 )
  ''')

#créer les tables pour  produit  (si elles n'existent pas)
cursor.execute('''CREATE TABLE IF NOT EXISTS produits (
 "Nom" VARCHAR(255),
 "ID Référence produit" VARCHAR(255) PRIMARY KEY,
 "Prix" REAL ,
 "Stock" INTEGER
 )
  ''')


conn.commit()

#pour vérifier que si le fichier à été créé
if os.path.exists(db_path):
    print("Base de données créée avec succès.")
else:
    print("Erreur: la base de données n'a pas été créée.")
conn.close()