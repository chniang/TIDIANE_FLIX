
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