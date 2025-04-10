import sqlite3
import pandas as pd
import os

# Connexion à la base de données (existante ou création)
db_path = "/app/BD/database.sqlite"
conn = sqlite3.connect(db_path)
cursor = conn.cursor()
 
# Supprimer la table "ventes" si elle existe déjà
conn.execute('DROP TABLE IF EXISTS ventes')
conn.execute('DROP TABLE IF EXISTS magasins')
conn.execute('DROP TABLE IF EXISTS produits')

# Vérification des chemins des fichiers CSV via les variables d'environnement
path_ventes = os.environ.get("PATH_VENTES")
path_magasins = os.environ.get("PATH_MAGASINS")
path_produits = os.environ.get("PATH_PRODUITS")

# Affichage des chemins pour débogage
print(f"Chemin des ventes: {path_ventes}")
print(f"Chemin des magasins: {path_magasins}")
print(f"Chemin des produits: {path_produits}")

# Chargement des données de ventes depuis le fichier CSV
try:
    ventes_df = pd.read_csv(path_ventes, delimiter=",")
    print(ventes_df.head())  # Afficher les premières lignes du DataFrame
    ventes_df.to_sql("ventes", conn, if_exists="replace", index=False)
except Exception as e:
    print(f"Erreur lors de l'importation des ventes : {e}")

# Chargement des données de magasins depuis le fichier CSV
try:
    magasins_df = pd.read_csv(path_magasins, delimiter=",")
    print(magasins_df.head())
    magasins_df.to_sql("magasins", conn, if_exists="replace", index=False)
except Exception as e:
    print(f"Erreur lors de l'importation des magasins : {e}")

# Chargement des données de produits depuis le fichier CSV
try:
    produits_df = pd.read_csv(path_produits, delimiter=",")
    print(produits_df.head())
    produits_df.to_sql("produits", conn, if_exists="replace", index=False)
except Exception as e:
    print(f"Erreur lors de l'importation des produits : {e}")

# Vérification de l'insertion des données dans les tables
try:
    cursor.execute("SELECT COUNT(*) FROM ventes")
    print("Nombre de lignes dans ventes :", cursor.fetchall()[0][0])
except Exception as e:
    print(f"Erreur lors de la vérification de la table 'ventes' : {e}")

try:
    cursor.execute("SELECT COUNT(*) FROM magasins")
    print("Nombre de lignes dans magasins :", cursor.fetchall()[0][0])
except Exception as e:
    print(f"Erreur lors de la vérification de la table 'magasins' : {e}")

try:
    cursor.execute("SELECT COUNT(*) FROM produits")
    print("Nombre de lignes dans produits :", cursor.fetchall()[0][0])
except Exception as e:
    print(f"Erreur lors de la vérification de la table 'produits' : {e}")

# Commit et fermeture de la connexion
conn.commit()
conn.close()
