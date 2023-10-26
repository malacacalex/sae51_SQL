-- Base de données SAE51
CREATE DATABASE saesql;
USE saesql;

-- Table "Ordinateurs"
CREATE TABLE Ordinateurs (
    ID INT PRIMARY KEY,
    Marque VARCHAR(255),
    Modele VARCHAR(255),
    Annee_achat DATE,
    RAM INT,
    Systeme_exploitation VARCHAR(255),
    Autres_informations_materiel TEXT
);

-- Table "Logiciels"
CREATE TABLE Logiciels (
    ID INT PRIMARY KEY,
    Nom_du_logiciel VARCHAR(255),
    Version VARCHAR(255),
    Licence VARCHAR(255),
    Ordinateur_ID INT,
    FOREIGN KEY (Ordinateur_ID) REFERENCES Ordinateurs(ID)
);

-- Table "Utilisateurs"
CREATE TABLE Utilisateurs (
    ID INT PRIMARY KEY,
    Nom VARCHAR(255),
    Prenom VARCHAR(255),
    Autres_informations_utilisateur TEXT
);

-- Table "Affectations"
CREATE TABLE Affectations (
    ID INT PRIMARY KEY,
    Ordinateur_ID INT,
    Utilisateur_ID INT,
    Date_affectation DATE,
    FOREIGN KEY (Ordinateur_ID) REFERENCES Ordinateurs(ID),
    FOREIGN KEY (Utilisateur_ID) REFERENCES Utilisateurs(ID)
);

-- Table "Maintenance"
CREATE TABLE Maintenance (
    ID INT PRIMARY KEY,
    Ordinateur_ID INT,
    Technicien VARCHAR(255),
    Date_intervention DATE,
    Actions_effectuees TEXT,
    FOREIGN KEY (Ordinateur_ID) REFERENCES Ordinateurs(ID)
);

