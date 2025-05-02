-- Création de la base de données
CREATE DATABASE TIDIANE_FLIX;

-- Sélection de la base de données
USE TIDIANE_FLIX;

-- Table Film
CREATE TABLE Film (
    id_film INT PRIMARY KEY,
    titre VARCHAR(100) NOT NULL,
    genre VARCHAR(50),
    date_sortie DATE,
    duree_minutes INT CHECK (duree_minutes > 0),
    realisateur VARCHAR(100)
);

-- Table Salle
CREATE TABLE Salle (
    id_salle INT PRIMARY KEY,
    nom_salle VARCHAR(50) NOT NULL,
    capacite INT CHECK (capacite > 0)
);

-- Table Client
CREATE TABLE Client (
    id_client INT PRIMARY KEY,
    nom VARCHAR(50) NOT NULL,
    prenom VARCHAR(50) NOT NULL,
    email VARCHAR(100),
    telephone VARCHAR(15)
);

-- Table Projection
CREATE TABLE Projection (
    id_projection INT PRIMARY KEY,
    date_projection DATE NOT NULL,
    heure TIME NOT NULL,
    id_film INT NOT NULL,
    id_salle INT NOT NULL,
    FOREIGN KEY (id_film) REFERENCES Film(id_film),
    FOREIGN KEY (id_salle) REFERENCES Salle(id_salle)
);

-- Table Ticket
CREATE TABLE Ticket (
    id_ticket INT PRIMARY KEY,
    prix DECIMAL(6,2) CHECK (prix > 0),
    date_achat DATE NOT NULL,
    id_client INT NOT NULL,
    id_projection INT NOT NULL,
    FOREIGN KEY (id_client) REFERENCES Client(id_client),
    FOREIGN KEY (id_projection) REFERENCES Projection(id_projection)
);

-- Table Avis
CREATE TABLE Avis (
    id_avis INT PRIMARY KEY,
    note INT CHECK (note >= 1 AND note <= 5),
    commentaire TEXT,
    date_avis DATE NOT NULL,
    id_client INT NOT NULL,
    id_film INT NOT NULL,
    FOREIGN KEY (id_client) REFERENCES Client(id_client),
    FOREIGN KEY (id_film) REFERENCES Film(id_film)
);
