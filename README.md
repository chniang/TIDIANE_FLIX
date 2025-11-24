# 🎬 TidianeFlix — Projet SQL + Dashboard Streamlit

Ce dépôt contient un projet complet simulant la gestion d’un cinéma :  
➡️ une base de données SQL  
➡️ un dashboard Streamlit pour visualiser et interagir avec les données.

---

## 📁 Structure du projet (réelle)

Model_Conceptuel et logique.pdf # Modèle conceptuel + logique (MCD/MLD)
streamlit_app.py # Application Streamlit
tidiane_flix.sql # Script SQL (tables + données fictives)

yaml
Copier le code

---

## 🎯 Objectif du projet

Le but de **TidianeFlix** est de créer :

- une base de données propre pour gérer :
  - films  
  - salles  
  - séances / projections  
  - clients  
  - tickets  
  - avis
- une interface Streamlit permettant :
  - d’afficher les données,
  - d’ajouter de nouveaux tickets,
  - de consulter des statistiques simples,
  - d’exécuter des requêtes SELECT pour vérifier des données.

---

## 🗄️ Installation de la base de données

### 1️⃣ Import via phpMyAdmin (XAMPP)
1. Ouvre phpMyAdmin : http://localhost/phpmyadmin  
2. Crée une base `tidiane_flix`  
3. Va dans **Importer**, choisis `tidiane_flix.sql` → Exécuter

### 2️⃣ Import via terminal
```bash
mysql -u root -p
CREATE DATABASE tidiane_flix;
USE tidiane_flix;
EXIT;

# Import
mysql -u root tidiane_flix < tidiane_flix.sql
▶️ Lancer le dashboard Streamlit
Dans le dossier du projet :

bash
Copier le code
streamlit run streamlit_app.py
🧩 Structure du projet
arduino
Copier le code
http://localhost:8501
⚙️ Connexion à la base (par défaut)
makefile
Copier le code
host: 127.0.0.1
user: root
password: (vide)
database: tidiane_flix
📊 Fonctionnalités de l’application Streamlit
Affichage des films

Liste des projections

Liste des clients

Vente de tickets (insertion SQL)

Visualisation des tickets

Requêtes SQL en lecture (SELECT)

Statistiques simples

📄 Documents inclus
✔️ Model_Conceptuel et logique.pdf
Le schéma technique du projet :

Modèle Conceptuel

Modèle Logique

✔️ tidiane_flix.sql
Contient :

création de toutes les tables,

jeux de données fictives,

clés primaires / étrangères.

✔️ streamlit_app.py
L’interface permettant de :

visualiser les données,

insérer des tickets,

analyser les ventes.

💡 Améliorations possibles
Ajouter des visualisations Plotly dans les statistiques

Ajouter un système d’authentification (admin)

Ajouter des captures d’écran du dashboard

Structurer le projet en dossiers (/sql, /docs, /assets)

Ajouter un requirements.txt

👤 Auteur
Cheikh Niang
Email : cheikhniang159@gmail.com
