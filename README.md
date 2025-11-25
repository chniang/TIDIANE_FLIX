🎬 TIDIANE_FLIX

Plateforme interactive de visualisation, d’exploration et d’analyse de films/séries.
Construite avec Streamlit, SQL, des dashboards statistiques et une interface intuitive.




📋 Table des Matières

Aperçu

Fonctionnalités

Démo / Captures

Architecture

Installation

Utilisation

Structure du Projet

Technologies

Contribution

Contact

🎯 Aperçu

TIDIANE_FLIX est une mini-plateforme analytique permettant :

de consulter des données de films/séries,

d’exécuter des requêtes SQL en direct,

d'explorer des visualisations statistiques,

et de naviguer dans une interface simple et épurée.

Projet construit dans un cadre pédagogique pour explorer SQL, Streamlit et la visualisation.

✨ Fonctionnalités

🏠 Accueil moderne avec vue générale

🧠 Exécution de requêtes SQL directement depuis Streamlit

📊 Dashboard statistique complet (genres, années, répartition, tendances…)

📸 Captures d’écran intégrées dans le README

🗄️ Base de données MySQL prête à l’emploi

🚀 Démo / Captures
📸 Screenshots (tous les fichiers se trouvent dans /screenshots/)
🏠 Accueil

🧮 Interface de requête SQL

📊 Statistiques










🏗️ Architecture
graph LR
    A[Base MySQL: tidiane_flix.sql] --> B[Streamlit - Module SQL]
    A --> C[Streamlit - Dashboard]
    B --> D[Interface Utilisateur]
    C --> D
    D --> E[Visualisation des films & statistiques]

📦 Installation
🔧 Prérequis

Python 3.x

pip

Git

MySQL (ou MariaDB)

🛠️ Étapes d'installation
# 1. Cloner le projet
git clone https://github.com/chniang/TIDIANE_FLIX.git
cd TIDIANE_FLIX

# 2. Créer un environnement virtuel
python -m venv venv
# activer Windows :
venv\Scripts\activate

# 3. Installer les dépendances
pip install -r requirements.txt

# 4. Importer la base de données
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

Pandas / NumPy

Matplotlib / Plotly

🤝 Contribution

Les contributions sont les bienvenues.
Procédure classique :

Fork

Nouvelle branche

Commits clairs

Pull Request

📧 Contact

Nom : Cheikh Niang
Email : cheikhniang159@gmail.com

GitHub : https://github.com/chniang

Projet : https://github.com/chniang/TIDIANE_FLIX

<div align="center"> Développé avec ❤️ à Dakar, Sénégal </div>
