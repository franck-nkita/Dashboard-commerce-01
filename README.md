# 📊 Dashboard E-commerce Conteneurisé

Projet de tableau de bord complet permettant d’analyser une base de données e-commerce contenant des millions d’enregistrements (clients, produits, commandes, stocks, paiements, livraisons, etc.).

Ce projet est construit avec Python, Streamlit et MySQL, et entièrement conteneurisé avec Docker.

---

## 🚀 Objectif du projet

Mettre en pratique des compétences réelles en :

- Développement backend (Python)
- Gestion de base de données relationnelle
- Analyse de données
- Visualisation de données
- Architecture logicielle
- Conteneurisation (Docker)

---

## 🧱 Technologies utilisées

- Python
- Streamlit
- Pandas
- MySQL
- Docker
- Docker Compose

---

## 📊 Fonctionnalités

- 📈 Tableau de bord interactif
- 👥 Analyse des clients
- 📦 Suivi des commandes
- 💰 Calcul du chiffre d’affaires
- 🛍️ Top produits vendus
- 📉 Alertes de stock faible
- 📍 Analyse géographique des clients
- 📊 Graphiques dynamiques

---

## 📂 Structure du projet
dashboard/ │ ├── app.py ├── db.py ├── dependances.txt ├── Dockerfile ├── docker-compose.yml ├── .env │ ├── init/ │   ├── schema.sql │   └── data.sql │ └── pages/

---

## ⚙️ Installation et exécution

### 1. Cloner le projet

```bash
git clone <repo_url>
cd dashboard
```

### Lancer avec Docker
Lancer avec Docker

```bash
docker compose up --build
```

### Accès à l’application
```bash
http://localhost:8501
```
### Configuration des variables d’environnement
```bash
mysql_host=db
mysql_user=root
mysql_passwd=root
mysql_db=shop
```

### Architecture Docker

Le projet contient deux services :
    db → MySQL (base de données)
    dashboard → Application Streamlit
Communication interne via réseau Docker.

## Points forts du projet
Architecture professionnelle type production
Séparation backend / base de données
Automatisation complète avec Docker Compose
Données persistées via volumes
Initialisation automatique des tables SQL

## Améliorations possibles

Authentification utilisateur
API REST (FastAPI)
Cache (Redis)
Déploiement cloud
Temps réel (WebSockets)
CI/CD pipeline

## Auteur

Projet réalisé dans un objectif d’apprentissage et de mise en pratique des technologies modernes de data et DevOps.
L'homme a la base est nkita kankonde franck.
