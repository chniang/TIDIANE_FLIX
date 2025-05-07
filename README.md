# 🎬 Projet SQL – TidianeFlix : Gestion de Billetterie pour un Cinéma

## 📌 Description du projet

**TidianeFlix** est une base de données conçue pour gérer un système de billetterie dans un service de projection de films. Elle permet de stocker et organiser des informations sur :

- les **films** projetés,
- les **clients**,
- les **paiements** effectués,
- les **billets** achetés,
- et les **projections** programmées.

L’objectif est de faciliter la gestion des ventes de billets et le suivi des projections dans un cinéma ou un service de streaming local.

---

## 🗂️ Structure de la base de données

La base de données est constituée de plusieurs **tables** :

1. **films** : Contient les informations sur chaque film (titre, genre, durée, année, etc.).
2. **clients** : Enregistre les informations des clients (nom, email, téléphone...).
3. **projections** : Liste les projections (date, heure, salle...).
4. **billets** : Contient les billets vendus pour chaque projection.
5. **paiements** : Enregistre les paiements des clients (montant, moyen de paiement...).

---

## ⚙️ Étapes du projet

Le projet se décompose en plusieurs étapes réalisées avec des requêtes SQL :

1. **Création des tables** : Définir la structure de chaque table avec les bons types de données et les relations entre elles.
2. **Insertion de données fictives** : Ajouter des données simulées pour tester la base (exemples de films, de clients, de paiements...).
3. **Requêtes SQL** :
   - Requêtes simples : sélection de films, de clients, etc.
   - Jointures : lier les tables pour obtenir des informations croisées (ex : clients + films achetés).
   - Requêtes avancées : filtrer, trier, regrouper les résultats (ex : total payé par chaque client).
4. **Création de vues** : Enregistrer certaines requêtes sous forme de vues pour les réutiliser facilement.
5. **Fonctions personnalisées** : Créer des fonctions SQL pour automatiser certains calculs (ex : calcul du total des paiements d’un client).

---

## 📈 Objectif final

Le but est de simuler un vrai système de gestion pour un cinéma (ou service de streaming), permettant de :

- gérer les projections,
- suivre les ventes de billets,
- suivre les paiements,
- et faire des statistiques utiles (recettes par film, client fidèle, etc.).

---

## 🏗️ 1. Création de la base de données et des tables

```sql
-- Création de la base de données

CREATE DATABASE TIDIANE_FLIX;
USE TIDIANE_FLIX;

-- Table Film
CREATE TABLE Film (
    id_film INT AUTO_INCREMENT PRIMARY KEY,
    titre VARCHAR(100) NOT NULL,
    genre VARCHAR(50),
    date_sortie DATE,
    duree INT CHECK (duree > 0),
    realisateur VARCHAR(100)
);

-- Table Salle
CREATE TABLE Salle (
    id_salle INT AUTO_INCREMENT PRIMARY KEY,
    nom_salle VARCHAR(50),
    capacite INT CHECK (capacite > 0)
);

-- Table Projection
CREATE TABLE Projection (
    id_projection INT AUTO_INCREMENT PRIMARY KEY,
    date_projection DATE,
    heure TIME,
    id_film INT,
    id_salle INT,
    FOREIGN KEY (id_film) REFERENCES Film(id_film),
    FOREIGN KEY (id_salle) REFERENCES Salle(id_salle)
);

-- Table Client
CREATE TABLE Client (
    id_client INT AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(50),
    prenom VARCHAR(50),
    email VARCHAR(100),
    telephone VARCHAR(20)
);

-- Table Ticket
CREATE TABLE Ticket (
    id_ticket INT AUTO_INCREMENT PRIMARY KEY,
    prix DECIMAL(6,2),
    date_achat DATE,
    id_client INT,
    id_projection INT,
    FOREIGN KEY (id_client) REFERENCES Client(id_client),
    FOREIGN KEY (id_projection) REFERENCES Projection(id_projection)
);

-- Table Avis
CREATE TABLE Avis (
    id_avis INT AUTO_INCREMENT PRIMARY KEY,
    note INT CHECK (note BETWEEN 1 AND 5),
    commentaire TEXT,
    date_avis DATE,
    id_client INT,
    id_film INT,
    FOREIGN KEY (id_client) REFERENCES Client(id_client),
    FOREIGN KEY (id_film) REFERENCES Film(id_film)
);


🧪 2. Insertion de données fictives
🎞️ Films (15)
sql


INSERT INTO Film (titre, genre, date_sortie, duree, realisateur) VALUES
('Inception', 'Science Fiction', '2010-07-16', 148, 'Christopher Nolan'),
('Titanic', 'Romance', '1997-12-19', 195, 'James Cameron'),
('Avatar', 'Science Fiction', '2009-12-18', 162, 'James Cameron'),
('Black Panther: Wakanda Forever', 'Action', '2022-11-11', 161, 'Ryan Coogler'),
('Parasite', 'Thriller', '2019-05-30', 132, 'Bong Joon-ho'),
('The Godfather', 'Crime', '1972-03-24', 175, 'Francis Ford Coppola'),
('The Dark Knight', 'Action', '2008-07-18', 152, 'Christopher Nolan'),
('Pulp Fiction', 'Crime', '1994-10-14', 154, 'Quentin Tarantino'),
('Interstellar', 'Science Fiction', '2014-11-07', 169, 'Christopher Nolan'),
('Joker', 'Drame', '2019-10-04', 122, 'Todd Phillips'),
('Shutter Island', 'Thriller', '2010-02-19', 138, 'Martin Scorsese'),
('Forrest Gump', 'Drame', '1994-07-06', 142, 'Robert Zemeckis'),
('Gladiator', 'Action', '2000-05-05', 155, 'Ridley Scott'),
('The Matrix', 'Science Fiction', '1999-03-31', 136, 'The Wachowskis'),
('The Lion King', 'Animation', '1994-06-24', 88, 'Roger Allers');


🏟️ Salles (3)
sql

INSERT INTO Salle (nom_salle, capacite) VALUES
('Salle 1', 100),
('Salle 2', 80),
('Salle 3', 50);


📽️ Projections (20)
sql

INSERT INTO Projection (date_projection, heure, id_film, id_salle) VALUES
('2025-05-01', '18:00:00', 1, 1),
('2025-05-01', '20:30:00', 2, 2),
('2025-05-02', '17:00:00', 3, 3),
-- 17 lignes supplémentaires à compléter selon les besoins...
('2025-05-03', '19:30:00', 4, 1),
('2025-05-04', '21:00:00', 5, 2),
('2025-05-05', '18:00:00', 6, 1),
('2025-05-06', '20:00:00', 7, 3),
('2025-05-07', '19:00:00', 8, 2),
('2025-05-08', '21:00:00', 9, 1),
('2025-05-09', '18:30:00', 10, 3),
('2025-05-10', '17:00:00', 11, 2),
('2025-05-11', '19:00:00', 12, 1),
('2025-05-12', '20:00:00', 13, 3),
('2025-05-13', '21:00:00', 14, 2),
('2025-05-14', '18:00:00', 15, 1),
('2025-05-15', '17:00:00', 1, 3),
('2025-05-16', '20:00:00', 2, 2),
('2025-05-17', '21:00:00', 3, 1);


👤 Clients (20)
sql

INSERT INTO Client (nom, prenom, email, telephone) VALUES
('Niang', 'Cheikh', 'cheikh1@mail.com', '777777001'),
-- 19 autres clients à compléter
('Fall', 'Fatou', 'fatou@mail.com', '777777002'),
('Ba', 'Alioune', 'alioune@mail.com', '777777003'),
-- ...
('Gueye', 'Awa', 'awa@mail.com', '777777020');


🎟️ Tickets (30)
sql

INSERT INTO Ticket (prix, date_achat, id_client, id_projection) VALUES
(3000, '2025-05-01', 1, 1),
-- 29 autres tickets (certains clients ayant plusieurs)
(3000, '2025-05-01', 1, 2),
(3500, '2025-05-02', 2, 3),
-- ...
(4000, '2025-05-10', 20, 10);


✍️ Avis (10)
sql

INSERT INTO Avis (note, commentaire, date_avis, id_client, id_film) VALUES
(5, 'Excellent film !', '2025-05-01', 1, 1),
-- 9 autres avis
(4, 'Très bon.', '2025-05-02', 2, 2),
(3, 'Pas mal.', '2025-05-03', 3, 3),
-- ...
(5, 'Chef-d’œuvre.', '2025-05-10', 10, 10);


🔍 3. Requêtes SQL
📄 Requêtes de base
sql

-- Lister les films
SELECT titre, duree, genre FROM Film;

-- Projections du film 'Wakanda Forever'
SELECT * FROM Projection WHERE id_film = (SELECT id_film FROM Film WHERE titre = 'Black Panther: Wakanda Forever');

-- Clients triés par nom
SELECT * FROM Client ORDER BY nom;

-- Nombre de films projetés dans la semaine
SELECT COUNT(DISTINCT id_film) FROM Projection WHERE WEEK(date_projection) = WEEK(CURDATE());


🔗 Requêtes avec jointures
sql

-- Détail des tickets achetés

SELECT Ticket.id_ticket, Film.titre, Projection.date_projection, Client.nom, Ticket.prix
FROM Ticket
JOIN Projection ON Ticket.id_projection = Projection.id_projection
JOIN Film ON Projection.id_film = Film.id_film
JOIN Client ON Ticket.id_client = Client.id_client;

-- Liste des projections avec film et salle

SELECT Projection.id_projection, Film.titre, Salle.nom_salle
FROM Projection
JOIN Film ON Projection.id_film = Film.id_film
JOIN Salle ON Projection.id_salle = Salle.id_salle;

-- Notes et commentaires par film

SELECT Film.titre, Avis.note, Avis.commentaire
FROM Avis
JOIN Film ON Avis.id_film = Film.id_film;

-- Clients ayant assisté à plus de 3 projections

SELECT Client.nom, Client.prenom, COUNT(*) AS nb_projections
FROM Ticket
JOIN Client ON Ticket.id_client = Client.id_client
GROUP BY Ticket.id_client
HAVING nb_projections > 3;


🧠 Requêtes avancées
sql

-- Film le plus projeté ce mois-ci

SELECT Film.titre, COUNT(*) AS nb_projections
FROM Projection
JOIN Film ON Projection.id_film = Film.id_film
WHERE MONTH(date_projection) = MONTH(CURDATE())
GROUP BY Film.id_film
ORDER BY nb_projections DESC
LIMIT 1;

-- Moyenne des notes par film

SELECT Film.titre, AVG(Avis.note) AS moyenne
FROM Avis
JOIN Film ON Avis.id_film = Film.id_film
GROUP BY Film.id_film;

-- Salles les plus utilisées

SELECT Salle.nom_salle, COUNT(*) AS nb
FROM Projection
JOIN Salle ON Projection.id_salle = Salle.id_salle
GROUP BY Salle.id_salle
ORDER BY nb DESC;

-- Clients ayant donné un avis mais pas acheté de ticket

SELECT DISTINCT Client.nom, Client.prenom
FROM Avis
LEFT JOIN Ticket ON Avis.id_client = Ticket.id_client
JOIN Client ON Avis.id_client = Client.id_client
WHERE Ticket.id_ticket IS NULL;

-- Revenus par jour

SELECT date_achat, SUM(prix) AS total
FROM Ticket
GROUP BY date_achat;

-- Création de vue : films populaires

CREATE VIEW films_populaires AS
SELECT Film.titre, COUNT(Ticket.id_ticket) AS nb_tickets, AVG(Avis.note) AS moyenne
FROM Film
LEFT JOIN Projection ON Film.id_film = Projection.id_film
LEFT JOIN Ticket ON Projection.id_projection = Ticket.id_projection
LEFT JOIN Avis ON Film.id_film = Avis.id_film
GROUP BY Film.id_film;

-- Fonction : revenu par film

DELIMITER //
CREATE FUNCTION revenu_par_film(film_id INT)
RETURNS DECIMAL(10,2)
DETERMINISTIC
BEGIN
  DECLARE total DECIMAL(10,2);
  SELECT SUM(Ticket.prix)
  INTO total
  FROM Ticket
  JOIN Projection ON Ticket.id_projection = Projection.id_projection
  WHERE Projection.id_film = film_id;
  RETURN IFNULL(total, 0);
END //
DELIMITER ;

👤 Auteur
Cheikh Niang
📧 cheikhniang159@gmail.com
