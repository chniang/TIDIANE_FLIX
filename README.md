# 🎬 TidianeFlix

**TidianeFlix** est un projet de modélisation et de gestion d'un système de billetterie pour un service de projection de films.  
Il permet de gérer les films, les clients, les projections, les salles, les billets ainsi que les avis des clients.

---

## 📌 Objectifs du projet

- Modéliser les données à l'aide d'un diagramme entité-association (EA).
- Créer la base de données relationnelle correspondante (modèle logique).
- Implémenter les tables avec des contraintes d'intégrité.
- Insérer des données fictives pertinentes.
- Formuler des requêtes SQL pour extraire des informations utiles.

---

## 🗂️ Entités principales

- **Film** : `id_film`, `titre`, `genre`, `date_sortie`, `durée`, `réalisateur`  
- **Salle** : `id_salle`, `nom_salle`, `capacité`  
- **Projection** : `id_projection`, `date`, `heure`, `id_film`, `id_salle`  
- **Client** : `id_client`, `nom`, `prénom`, `email`, `téléphone`  
- **Billet** : `id_ticket`, `prix`, `date_achat`, `id_client`, `id_projection`  
- **Avis** : `id_avis`, `note`, `commentaire`, `date_avis`, `id_client`, `id_film`

---

## 🛠️ Étapes de réalisation

1. **Modélisation conceptuelle** :  
   Diagramme entité-association (EA) avec cardinalités.

2. **Modélisation logique** :  
   Traduction du modèle EA en schéma relationnel (modèle logique).

3. **Création de la base SQL** :  
   Tables avec :
   - Clés primaires
   - Clés étrangères
   - Contraintes `NOT NULL`, `CHECK`, etc.

4. **Remplissage de données fictives** :
   - 15 films
   - 3 salles
   - 20 projections (réparties sur plusieurs jours)
   - 20 clients
   - 30 billets (certains clients achètent plusieurs tickets)
   - 10 avis

5. **Requêtes SQL** :

   ### Requêtes de base :
   - Liste de tous les films avec durée et genre
   - Projections d’un film donné
   - Liste des clients triés par nom
   - Nombre de films projetés cette semaine

   ### Requêtes avec jointures :
   - Détail des tickets achetés (film, date, client, prix)
   - Projections avec titre du film et nom de la salle
   - Avis (notes et commentaires) par film
   - Clients ayant assisté à plus de 3 projections

   ### Requêtes avancées :
   - Film le plus projeté du mois
   - Moyenne des notes par film
   - Salles les plus utilisées
   - Clients ayant donné un avis sans avoir acheté de ticket
   - Revenus générés par jour et semaine
   - Vue `films_populaires(titre, nb_tickets, note_moyenne)`
   - Fonction `revenu_par_film(id_film)` : total des gains d’un film

---

## 💡 Technologies utilisées

- **MySQL** : création de la base, requêtes, fonctions
- **Draw.io** : création du diagramme EA
- **Données fictives** : ajout via requêtes `INSERT INTO`

---

## 📷 Aperçu

- Modèle conceptuel EA (diagramme)
- Modèle logique relationnel
- Script SQL complet avec données

---

## 👤 Auteur

**Cheikh Niang**  
📧 Contact : cheikhniang159@gmail.com

---

## ✅ Licence

Ce projet est libre d'utilisation à des fins **pédagogiques**.  
Toute contribution ou amélioration est la bienvenue !
