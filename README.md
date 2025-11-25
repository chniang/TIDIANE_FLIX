🎬 TIDIANE_FLIX – Plateforme d’analyse et de visualisation de films & séries

Une application Streamlit basée sur MySQL, permettant d’exécuter des requêtes SQL en direct et d’explorer des statistiques interactives sur les films & séries.






📌 Table des Matières

Aperçu

Fonctionnalités

Screenshots

Architecture

Installation

Structure du Projet

Technologies

Contribution

Contact

🎯 Aperçu

TIDIANE_FLIX est une application web conçue pour :

🔍 Analyser, visualiser et explorer une base de données de films & séries

📝 Utiliser une interface SQL intégrée pour exécuter des requêtes

📊 Générer des dashboards statistiques visuels

🎨 Présenter des graphiques interactifs et propres

Une solution idéale pour apprendre SQL, manipuler des données et créer un projet professionnel dans ton portfolio.

✨ Fonctionnalités

🎥 Accueil interactif

🧮 Interface SQL temps réel

📊 Dashboard analytique avec graphiques (genres, années, popularité, etc.)

🗂️ Gestion complète via la base tidiane_flix.sql

📸 Nombreuses captures d’écran intégrées

📸 Screenshots

(Les liens pointent directement vers les images du dossier screenshots/ du repo. Tout fonctionne sur GitHub.)

🏠 Accueil

🧮 Interface de requête SQL

📊 Statistiques










🏗️ Architecture
graph LR
    A[Base MySQL] --> B[Interface SQL]
    B --> C[Application Streamlit]
    C --> D[Dashboards & Visualisations]

⚙️ Installation
🔧 Prérequis

Python 3.x

MySQL

pip

Git

📥 Étapes d'installation
# 1. Cloner le projet
git clone https://github.com/chniang/TIDIANE_FLIX.git
cd TIDIANE_FLIX

# 2. Créer un environnement virtuel
python -m venv venv
venv\Scripts\activate   # Windows

# 3. Installer les dépendances
pip install -r requirements.txt

# 4. Initialiser la base de données
mysql -u root -p < tidiane_flix.sql

# 5. Lancer l’application
streamlit run streamlit_app.py

🧩 Structure du Projet
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

Pandas, NumPy

Matplotlib, Plotly

🤝 Contribution

Contributeurs bienvenus !

Faites un fork

Créez une branche

Faites un commit clair

Ouvrez une Pull Request

📧 Contact

👤 Cheikh Niang
📩 Email : cheikhniang159@gmail.com

💼 GitHub : https://github.com/chniang

🔗 Projet : https://github.com/chniang/TIDIANE_FLIX

<div align="center"> <strong>Développé avec ❤️ à Dakar, Sénégal</strong> </div>
