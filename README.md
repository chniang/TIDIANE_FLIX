# 🎬 TIDIANE FLIX – Système de Gestion de Billetterie

TIDIANE FLIX est une application simple permettant d'exécuter des requêtes SQL, visualiser des statistiques, et interagir avec une base de données MySQL via une interface Streamlit.

---

## 🧠 Diagramme simplifié du fonctionnement

```mermaid
graph LR
    A[Base de données MySQL] --> B[Interface SQL - Streamlit]
    B --> C[Visualisation des statistiques]
    C --> D[Tableau de bord et résultats]
📦 Installation
🔧 Prérequis
Python 3.x

Git

MySQL (ou tout SGBD compatible)

🚀 Étapes d'installation
bash
Copier le code
# 1. Cloner le dépôt
git clone https://github.com/chniang/TIDIANE_FLIX.git
cd TIDIANE_FLIX

# 2. Créer un environnement virtuel
python -m venv venv

# Activer l'environnement (Windows)
venv\Scripts\activate

# 3. Installer les dépendances
pip install -r requirements.txt

# 4. Initialiser la base de données
mysql -u root -p < tidiane_flix.sql

# 5. Lancer l'application Streamlit
streamlit run streamlit_app.py
🧩 Structure du projet
arduino
Copier le code
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
├── Model_Conceptuel_et_logique.pdf
├── tidiane_flix.sql
├── streamlit_app.py
└── requirements.txt
📸 Captures d'écran
🏠 Accueil

💻 Interface SQL

📊 Statistiques





🛠️ Technologies utilisées
Python

Streamlit

MySQL / SQL

Pandas / NumPy

Matplotlib / Plotly

🤝 Contribution
Les contributions sont les bienvenues :

Fork

Créer une branche

Commit clair

Pull Request

Merci d'appliquer les bonnes pratiques (PEP8, docstrings, tests si nécessaire).

📧 Contact
Nom : Cheikh Niang
Email : cheikhniang159@gmail.com
GitHub : https://github.com/chniang
Projet : https://github.com/chniang/TIDIANE_FLIX
