pip install sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


# Créez le moteur SQLAlchemy
engine = create_engine(db_url)

# Définissez le modèle de données (par exemple, pour la table "Ordinateurs")
from mymodels import Ordinateur  # Remplacez "mymodels" par le nom de votre module de modèles



import random
import string
import datetime

# Fonction pour générer un nom aléatoire
def generate_random_name():
    first_name = ''.join(random.choice(string.ascii_uppercase) for _ in range(3))
    last_name = ''.join(random.choice(string.ascii_uppercase) for _ in range(5))
    return f"{first_name} {last_name}"

# Générer des données aléatoires pour la table "Ordinateurs"
for _ in range(100):
    marque = random.choice(['HP', 'Dell', 'Lenovo', 'Acer', 'Asus'])
    modele = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(8))
    annee_achat = random.randint(2010, 2023)
    ram = random.randint(4, 32)
    systeme_exploitation = random.choice(['Windows 10', 'Windows 11', 'Linux', 'macOS'])
    autres_informations = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(20))

    # Insérez ces données dans la table "Ordinateurs" de votre base de données

# Générer des données aléatoires pour la table "Logiciels"
for _ in range(100):
    nom_logiciel = ''.join(random.choice(string.ascii_letters) for _ in range(10))
    version = ''.join(random.choice(string.digits) for _ in range(3)) + '.' + ''.join(random.choice(string.digits) for _ in range(2))
    licence = random.choice(['Gratuit', 'Payant', 'Open Source'])
    
    # Assurez-vous que l'ID de l'ordinateur auquel ce logiciel est installé existe dans la table "Ordinateurs"
    ordinateur_id = random.randint(1, 100)  # Vous devrez ajuster cela en fonction de votre base de données

    # Insérez ces données dans la table "Logiciels" de votre base de données

# Générer des données aléatoires pour la table "Utilisateurs"
for _ in range(50):
    nom_utilisateur = generate_random_name()
    
    # Insérez ces données dans la table "Utilisateurs" de votre base de données

# Générer des données aléatoires pour la table "Affectations"
for _ in range(50):
    utilisateur_id = random.randint(1, 50)  # Vous devrez ajuster cela en fonction de votre base de données
    ordinateur_id = random.randint(1, 100)  # Vous devrez ajuster cela en fonction de votre base de données
    date_affectation = datetime.date(random.randint(2010, 2022), random.randint(1, 12), random.randint(1, 28))
    
    # Insérez ces données dans la table "Affectations" de votre base de données

# Générer des données aléatoires pour la table "Maintenance"
for _ in range(30):
    technicien = random.choice(['Adrien Conin', 'Axel Malac', 'Ben Gala'])
    ordinateur_id = random.randint(1, 100)  # Vous devrez ajuster cela en fonction de votre base de données
    date_intervention = datetime.date(random.randint(2010, 2022), random.randint(1, 12), random.randint(1, 28))
    actions_effectuees = ''.join(random.choice(string.ascii_letters) for _ in range(20))
    
    # Insérez ces données dans la table "Maintenance" de votre base de données

