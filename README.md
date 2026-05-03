# 🎬 Films API

API REST construite avec FastAPI pour gérer un catalogue de films.

## Lancer le projet

```bash
# 1. Cloner le repo
git clone https://github.com/ton-username/films-api.git
cd films-api

# 2. Créer un environnement virtuel
python -m venv venv
source venv/bin/activate        # Linux/Mac
venv\Scripts\activate           # Windows

# 3. Installer les dépendances
pip install -r requirements.txt

# 4. Lancer le serveur
uvicorn main:app --reload
```

L'API est disponible sur http://localhost:8000
Documentation Swagger : http://localhost:8000/docs

## Endpoints

| Méthode | Route | Description |
|--------|-------|-------------|
| GET | /films | Liste avec filtres |
| GET | /films/{id} | Détail d'un film |
| POST | /films | Créer un film |
| PUT | /films/{id} | Remplacer un film |
| PATCH | /films/{id} | Mise à jour partielle |
| DELETE | /films/{id} | Supprimer un film |