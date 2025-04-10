# Utiliser la dernière image stable de Python 3.13.2
FROM python:3.13.2

# Mettre à jour les paquets et installer bash
RUN apt-get update && apt-get install -y bash \
    && rm -rf /var/lib/apt/lists/*

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers nécessaires dans le conteneur
COPY ./SCR /app/SCR
COPY ./DATA /app/DATA
COPY ./BD /app/BD
COPY requirements.txt /app/requirements.txt

# Définir les variables d'environnement
ENV PATH_VENTES=/app/DATA/Données_brief_data_engineer_ventes.csv \
    PATH_MAGASINS=/app/DATA/Données_brief_data_engineer_magasins.csv \
    PATH_PRODUITS=/app/DATA/Données_brief_data_engineer_produits.csv

# Installer les dépendances python à partir du fichier requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Commande à exécuter au démarrage du conteneur
CMD ["bash", "-c", "python /app/SCR/create_schema.py && python /app/SCR/import_data.py"]
