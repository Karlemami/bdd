import random
import sqlite3
from faker import Faker
from datetime import datetime, timedelta
fake = Faker('fr_FR')
conn = sqlite3.connect("enquete.db")
c = conn.cursor()


def recréation_db():
    c.execute("DROP TABLE IF EXISTS employés")
    c.execute("DROP TABLE IF EXISTS vacances_2023")
    c.execute("DROP TABLE IF EXISTS badges")
    c.execute("DROP TABLE IF EXISTS mails")
    c.execute("DROP TABLE IF EXISTS congés_2023")
    c.execute("DROP TABLE IF EXISTS badges_2023")
    conn.commit()

    c.execute("""
    CREATE TABLE employés (
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    nom VARCHAR, 
    prénom VARCHAR,
    fonction VARCHAR,
    salaire INTEGER,
    date_embauche VARCHAR
    )""")
    c.execute("""
    CREATE TABLE congés_2023 (
        date_départ_demandée VARCHAR,
        date_départ_accordée VARCHAR,
        date_retour_demandée VARCHAR,
        date_retour_accordée VARCHAR,
        id_employé INTEGER,
        FOREIGN KEY (id_employé) REFERENCES employés(id)
    )""")
    c.execute("""
    CREATE TABLE badges_2023 (
        date_heure_badge VARCHAR,
        lieu_badge VARCHAR,
        type_badge VARCHAR,
        id_employé INTEGER,
        FOREIGN KEY (id_employé) REFERENCES employés(id)
    )""")
    c.execute(
    """CREATE TABLE mails (
        date TEXT,
        contenu TEXT,
        id_expéditeur INTEGER,
        id_destinataire INTEGER,
        FOREIGN KEY (id_expéditeur) REFERENCES employés(id),
        FOREIGN KEY (id_destinataire) REFERENCES employés(id)
    )""")
    conn.commit()

def génération_badges():
    data = []
    lieux = ["Bureau PDG","Open Space","Cour intérieure","Salle d'ordinateur quantique"]
    for i in range(40000):
        date = str(fake.date_between(start_date="-1y", end_date='today'))
        heure = fake.time()
        date_heure_badge = date + f"|{heure}"
        lieu_badge = random.choice(lieux)
        type_badge = random.choice(["Entrée","Sortie"])
        id_employé = random.randint(1,5001)
        data.append([date_heure_badge,lieu_badge,type_badge,id_employé])
    return data
    
def génération_congés():
    data = []
    ids_employés = list(range(5001))
    for i in range(5001):
        date_départ_demandée = fake.date_between(start_date="-1y",end_date="today")
        proba = random.randint(0,10)
        if proba in [0,1,2,3,4,5,6,7,8]:
            date_départ_accordée = date_départ_demandée
        else:
            date_départ_accordée = timedelta(days=random.randint(-10,10))
            date_départ_accordée = date_départ_demandée + date_départ_accordée
        temps_congé = random.choice((7,14))
        temps_congé = timedelta(days=temps_congé)
        date_retour_demandée = date_départ_demandée + temps_congé
        date_retour_accordée = date_départ_accordée + temps_congé
        id_employé = random.choice(ids_employés)
        ids_employés.remove(id_employé)
        data.append([date_départ_demandée,date_départ_accordée,date_retour_demandée,date_retour_accordée,id_employé])
    return data

def génération_employés():
    data = [["Philippe","Florian","PDG","1000000","13/05/2011"]]
    for i in range(5000):
        prénom = fake.first_name()
        nom = fake.last_name()
        fonction = random.choice(['Ingénieur TAL', 'Informaticien réseau', 'Expert machine learning','Développeur','Chef de projet'])
        salaire = random.randint(2000,15000) 
        date_embauche = fake.date_between(start_date='-5y', end_date='today')
        data.append([nom, prénom, fonction, salaire, date_embauche])
    return data

def génération_mails():
    data = []
    ouverture = ["Cher collègue,\n\n","Salut\n\n","Bonjour\n\n"]
    fermeture = ["Bien à toi\n\n","Bien cordialement\n\n","À +","À tout à l'heure"]
    for i in range(0,40000):
        date = str(fake.date_between(start_date="-1y", end_date='today'))
        time = fake.time()
        date += f"|{time}"
        id_expéditeur = random.randint(1,1000)
        id_destinataire = random.randint(1,1000)
        texte = random.choice(ouverture)
        texte += fake.text()
        texte += random.choice(fermeture)
        data.append([date,texte,id_expéditeur,id_destinataire])
    return data

recréation_db()

insert_query = "INSERT INTO mails (date, contenu, id_expéditeur, id_destinataire) VALUES (?,?,?,?)"
c.executemany(insert_query, génération_mails())
conn.commit()

insert_query = "INSERT INTO employés(nom, prénom, fonction, salaire, date_embauche) VALUES (?,?,?,?,?)"
c.executemany(insert_query, génération_employés())
conn.commit()

insert_query = """INSERT INTO congés_2023 (date_départ_demandée, date_départ_accordée, date_retour_demandée, 
                date_retour_accordée, id_employé) VALUES (?,?,?,?,?)"""
c.executemany(insert_query, génération_congés())
conn.commit()

insert_query = "INSERT INTO badges_2023(date_heure_badge,lieu_badge,type_badge,id_employé) VALUES (?,?,?,?)"
c.executemany(insert_query, génération_badges())
conn.commit()

conn.close()