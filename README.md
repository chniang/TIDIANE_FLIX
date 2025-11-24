# 🎬 TIDIANE FLIX  
Système de gestion de billetterie avec MySQL + Streamlit

TIDIANE FLIX est une mini-application permettant d’exécuter des requêtes SQL, d’explorer une base MySQL et de visualiser rapidement des statistiques via une interface Streamlit simple et intuitive.

---

## 🔗 Démo / Ressources

- 🎥 **Vidéo Démo (YouTube)** : *à ajouter si tu veux, lien ici*  
- 💻 **Dépôt GitHub** : https://github.com/chniang/TIDIANE_FLIX  
- 🖥️ **Version locale** :  
  ```bash
  streamlit run streamlit_app.py
🧠 Architecture du projet
mermaid
Copier le code
graph LR
    A[Base MySQL - tidiane_flix.sql] --> B[Backend SQL]
    B --> C[Streamlit - Interface]
    C --> D[Visualisations & Tableaux de bord]
📦 Installation
1️⃣ Prérequis
Python 3.x

Git

MySQL installé localement

pip

2️⃣ Installation rapide
bash
Copier le code
# 1. Cloner le projet
git clone https://github.com/chniang/TIDIANE_FLIX.git
cd TIDIANE_FLIX

# 2. Créer un environnement virtuel
python -m venv venv

# Activer l'environnement (Windows)
venv\Scripts\activate

# 3. Installer les dépendances
pip install -r requirements.txt

# 4. Importer la base de données
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
├── Model_Conceptuel et logique.pdf
├── tidiane_flix.sql
├── streamlit_app.py
└── requirements.txt
📸 Captures d’écran
🏠 Accueil

💻 Exécution des requêtes SQL

📊 Statistiques





🛠️ Technologies utilisées
Python 3

Streamlit

MySQL

Pandas / NumPy

Matplotlib / Plotly

🤝 Contribution
Tu peux contribuer via :

Fork du dépôt

Création d’une nouvelle branche

Commit clair

Pull Request

👤 Auteur
Cheikh Niang
📧 Email : cheikhniang159@gmail.com
🌐 GitHub : https://github.com/chniang
📁 Repo du projet : https://github.com/chniang/TIDIANE_FLIX