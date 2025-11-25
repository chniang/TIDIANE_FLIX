🎬 TIDIANE_FLIX

Plateforme d’analyse de films/séries avec interface Streamlit, requêtes SQL et visualisations statistiques.




📋 Table des Matières

Aperçu

Fonctionnalités

Démo (Screenshots)

Architecture

Installation

Utilisation

Structure du projet

Technologies

Contribution

Contact

🎯 Aperçu

TIDIANE_FLIX est une application développée en Streamlit, permettant :

La visualisation de films/séries

L'exécution de requêtes SQL

L'analyse via un dashboard statistique complet

✨ Fonctionnalités

🎥 Accueil : présentation du projet

🧮 Interface SQL : exécuter vos propres requêtes

📊 Dashboard : statistiques et visualisations

📸 Captures d’écran intégrées

🚀 Démo (Screenshots)
📸 Captures d’écran

(Cliquables si tu les ouvres dans GitHub)

🏠 Accueil

🧮 Interface de requête SQL

📊 Statistiques










🏗️ Architecture
graph LR
    A[Base MySQL] --> B[Interface SQL]
    B --> C[Application Streamlit]
    C --> D[Dashboard & Visualisations]

📦 Installation
Prérequis

Python 3.x

pip

Git

MySQL

Étapes
# 1. Cloner le projet
git clone https://github.com/chniang/TIDIANE_FLIX.git
cd TIDIANE_FLIX

# 2. Environnement virtuel
python -m venv venv
venv\Scripts\activate  # Windows

# 3. Installer les dépendances
pip install -r requirements.txt

# 4. Initialiser la base de données
mysql -u root -p < tidiane_flix.sql

# 5. Lancer l'application
streamlit run streamlit_app.py

🧩 Structure du projet
TIDIANE_FLIX/
├── .streamlit/
│   └── config.toml
├── screenshots/
│   ├── accueil.png
│   ├── interface_de_requette_SQL.png
│   ├── statistique_1.png
│   ├── statistique_2.png
│   ├── statistique_3.png
│   ├── statistique_4.png
│   └── statistique_5.png
├── Model_Conceptuel et logique.pdf
├── tidiane_flix.sql
├── streamlit_app.py
├── requirements.txt
└── README.md

🛠️ Technologies

Python

Streamlit

MySQL / SQL

Pandas / NumPy

Matplotlib / Plotly

🤝 Contribution

Contributions bienvenues :

Fork

Nouvelle branche

Commit propre

Pull request

📧 Contact

Nom : Cheikh Niang
Email : cheikhniang159@gmail.com

GitHub : https://github.com/chniang

Projet : https://github.com/chniang/TIDIANE_FLIX

<div align="center">✨ Développé avec passion à Dakar 🇸🇳 ✨</div>
