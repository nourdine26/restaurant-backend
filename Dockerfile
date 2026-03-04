# Forcer Python 3.12
FROM python:3.12-slim

# Variables d'environnement pour éviter les problèmes
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Créer le répertoire de travail
WORKDIR /app

# Copier les fichiers de configuration
COPY config/requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copier tout le projet
COPY . /app/

# Définir le répertoire de travail sur config
WORKDIR /app/config

# Collecter les fichiers statiques
RUN python manage.py collectstatic --noinput

# Commande de démarrage (avec le bon port Render)
CMD gunicorn config.wsgi:application --bind 0.0.0.0:$PORT