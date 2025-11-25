🎬 TIDIANE_FLIX

Plateforme de visualisation et d’analyse de films & séries, avec interface Streamlit, exploration SQL et dashboard statistique.




📋 Table des Matières

Aperçu

Fonctionnalités

Démo

Architecture

Installation

Utilisation

Structure du Projet

Technologies

Contribution

Contact

🎯 Aperçu

TIDIANE_FLIX est une mini-plateforme Streamlit permettant :

la consultation d’un catalogue de films/séries,

l’exécution de requêtes SQL via une interface simplifiée,

la visualisation de statistiques interactives (genres, années, popularité…),

la démonstration d’un pipeline Data complet (SQL → Python → Dashboard).

✨ Fonctionnalités

🎥 Page d’accueil avec présentation du projet

🧮 Interface SQL pour interroger la base tidiane_flix.sql

📊 Dashboard statistique avec plusieurs graphiques (genre, années, notes…)

📸 Captures d'écran intégrées pour démonstration visuelle

🗂️ Base SQL complète fournie dans le projet

🚀 Démo
📸 Captures d’écran
<details><summary>Cliquer pour voir</summary>
🏠 Accueil

🧮 Interface SQL

📊 Dashboards & Statistiques










</details>
🏗️ Architecture
graph LR
    A[Base SQL: tidiane_flix.sql] --> B[Python / Pandas]
    B --> C[Streamlit Interface]
    C --> D[Dashboard & Visualisations]

📦 Installation
✅ Prérequis

Python 3.x

pip

Git

MySQL

🔧 Installation
# 1. Cloner le projet
git clone https://github.com/chniang/TIDIANE_FLIX.git
cd TIDIANE_FLIX

# 2. Créer un environnement virtuel
python -m venv venv
venv\Scripts\activate  # Windows

# 3. Installer les dépendances
pip install -r requirements.txt

# 4. Importer la base
mysql -u root -p < tidiane_flix.sql

# 5. Lancer l'application
streamlit run streamlit_app.py

▶️ Utilisation

Ouvrir l'application dans votre navigateur

Explorer les pages :

Accueil

Requêtes SQL

Statistiques

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

Python 3.x

Streamlit

MySQL

Pandas / NumPy

Matplotlib / Plotly

🤝 Contribution

Les contributions sont les bienvenues !

Fork

Nouvelle branche

Commit clair

Pull request

📧 Contact

Nom : Cheikh Niang
Email : cheikhniang159@gmail.com

GitHub : https://github.com/chniang

Projet : https://github.com/chniang/TIDIANE_FLIX

<div align="center">Développé avec ❤️ à Dakar, Sénégal</div>
