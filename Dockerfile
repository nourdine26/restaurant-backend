# Utiliser Python 3.12 officiel
FROM python:3.12-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers de configuration
COPY config/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copier tout le projet
COPY . .

# Définir le répertoire de travail sur config
WORKDIR /app/config

# Commande de démarrage
CMD gunicorn config.wsgi:application --bind 0.0.0.0:$PORT