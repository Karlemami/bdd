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
    c.execute("DROP TABLE IF EXISTS projets")
    conn.commit()

    c.execute("""
    CREATE TABLE employés (
    id INTEGER PRIMARY KEY,
    nom VARCHAR,
    prénom VARCHAR,
    fonction VARCHAR,
    salaire INTEGER,
    date_embauche VARCHAR,
    id_projet INTEGER,
    FOREIGN KEY (id_projet) REFERENCES projets(id)
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
        date VARCHAR,
        contenu TEXT,
        objet TEXT,
        id_expéditeur INTEGER,
        id_destinataire INTEGER,
        FOREIGN KEY (id_expéditeur) REFERENCES employés(id),
        FOREIGN KEY (id_destinataire) REFERENCES employés(id)
    )""")
    c.execute("""CREATE TABLE projets (
        id_projet INTEGER PRIMARY KEY,
        nom_projet VARCHAR,
        description_projet TEXT,
        date_début VARCHAR,
        id_chef_projet INTEGER,
        FOREIGN KEY (id_chef_projet) REFERENCES employés(id)
    )""")
    conn.commit()

def projets():
    projet1 = ["1","LinguaSync","Projet de LLM visant à améliorer la compréhension contextuelle dans les interactions langagières automatisées",
                "2021-09-20","430"]
    projet2 = ["2","QuantumVision","Création d'un système de vision par ordinateur avancé pour améliorer la reconnaissance d'objets dans des environnements complexes.",
                "2017-03-12","3408"]
    projet3 = ["3","DataHarmony","Mise en œuvre d'une plateforme de gestion de données centralisée pour améliorer l'efficacité des analyses de données à grande échelle.",
                "2020-09-12","400"]
    projet4 = ["4","TitanAI","Projet de LLM visant à élaborer une IA travailleuse qui maîtrise le développement d'applications et de LLM.",
                "2009-04-23","3809"]
    projet5 = ["5","SmartGrid","Développement d'un système intelligent de gestion des réseaux électriques pour une utilisation plus efficace de l'énergie.",
                "2015-09-07","806"]
    data = [projet1,projet2,projet3,projet4,projet5]
    return data
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
        temps_congé = random.randint(1,14)
        temps_congé = timedelta(days=temps_congé)
        date_retour_demandée = date_départ_demandée + temps_congé
        date_retour_accordée = date_départ_accordée + temps_congé
        id_employé = random.choice(ids_employés)
        ids_employés.remove(id_employé)
        data.append([date_départ_demandée,date_départ_accordée,date_retour_demandée,date_retour_accordée,id_employé])
    return data

def génération_employés():
    data = [["1","Dubois","Jean","PDG","1000000","12/05/2011","NULL"]]
    for i in range(2,5000):
        if i == 340:
            data.append([i,"Coupable","John","Ingénieur TAL","2000","2012-04-01", "4"])
        elif i == 2000:
            data.append([i, "Philippe","Ashley","Développeuse Web","7000","1998-11-24", "4"])
        elif i == 1784:
            data.append([i, "Fleith","Florian","Employé polyvalent","10000","2001-03-12", "4"])
        elif i == 4504:
            data.append([i, "Ratier","Valentine","Technicienne de surface","150000","2001-07-06", "4"])
        elif i == 728:
            data.append([i, "Dengrot","Drécic","Speech Analyst","70000","2022-09-18", "4"])
        elif i == 3809:
            data.append([i, "Outan","Laurent","Chef de projet","150000","2013-07-30", "4"])
        elif i == 3789:
            data.append([i,"Mariotte","Laurent","Développeur","6500","1994-08-24", "4"])
        elif i == 2309:
            data.append([i, "Dupont","Pierre","Ingénieur TAL","7800","2003-05-30", "4"])
        elif i == 3975:
            data.append([i,"Tuillier","Emma","Développeuse","9000","1999-12-13", "4"])
        elif i == 18:
            data.append([i, "Lemaire","Amandine","Experte en ML","10000","2004-10-23", "4"])
        else:
            prénom = fake.first_name()
            nom = fake.last_name()
            fonction = random.choice(['Ingénieur TAL', 'Informaticien réseau', 'Expert machine learning','Développeur','Chef de projet'])
            salaire = random.randint(2000,15000)
            date_embauche = fake.date_between(start_date='-20y', end_date='today')
            proba = range(10)
            if proba in range(8):
                id_projet = "NULL"
            else:
                id_projet = random.choice([1,2,3,5,6])
            data.append([i, nom, prénom, fonction, salaire, date_embauche,id_projet])
    return data

def génération_mails():
    data = []
    ouverture = ["Cher collègue,\n\n","Salut,\n\n","Bonjour,\n\n"]
    fermeture = ["Bien à toi\n\n","Bien cordialement\n\n","À +","À tout à l'heure"]
    objets = ["Discussion projet",
              "Réunion planifiée",
              "Demande de congé",
              "Rapport mensuel",
              "Rapport trimestriel",
              "Feedback réunion",
              "Alerte IT",
              "Formation et développement",
              "Note de service",
              "Invitation événement d'entreprise",
              "Note de service",
              "Politique de l'entreprise",
              "Framework LLM",
              "On sfait une confcall ?"]
    for i in range(0,40000):
        if i == 452:
            data.append(["2023-03-24|15:18:12",
                            "Hey,\n\nT'as vu les dernières conneries de notre PDG dans le domaine du machine learning et du NLP ? C'est du grand n'importe quoi. On dirait qu'il a découvert ces termes hier. T'as des idées pour remédier à cette catastrophe ?\n\nÀ plus\n",
                            "Dérapage du Boss",
                            "340",
                            "18"])
        elif i == 8963:
            data.append(["2023-02-14|12:25:12",
                            "Salut,\n\nJ'en peux plus des choix du PDG en machine learning. Sérieux, on dirait qu'il a tiré ses idées d'un livre de 2005. T'as remarqué, non ? On devrait lui envoyer un manuel de mise à jour.\n\nÀ discuter,\n",
                            "Ras-le-bol du Chef",
                            "340",
                            "728"])
        elif i == 122:
            data.append(["2023-03-12|04:25:36",
                            "Hey,\n\nJ'ai l'impression que le PDG est tellement passionné par le machine learning qu'il en oublie parfois le reste de l'équipe. Tu crois qu'on pourrait lui organiser une petite pause décontractée pour qu'il se reconnecte avec le monde réel ?\n\nÀ la recherche d'équilibre,\n",
                            "La passion débordante du PDG",
                            "728",
                            "340"])
        elif i == 2768:
            data.append(["2023-02-15|17:34:07",
                        "Cher collègue,\n\nCes derniers temps, j'ai remarqué plusieurs signes qui me laissent perplexe quant aux intentions du PDG. Il semble qu'il y ait des discussions en coulisse concernant l'intégration d'une intelligence artificielle pour remplacer certains postes au sein de notre entreprise. Est-ce que quelqu'un d'autre a remarqué cela ?\nJe comprends que l'automatisation peut améliorer l'efficacité, mais je ressens une certaine inquiétude quant à l'impact sur nos emplois. Devrions-nous aborder ce sujet avec lui ou commencer à explorer nos options ?\n\nCordialement.\n",
                        "Préoccupations concernant les récentes initiatives du PDG",
                        "3789",
                        "728"])
        elif i == 126:
            data.append(["2023-01-15|12:49:32",
                        "Salut,\n\nAs-tu entendu parler de la réunion sur l' 'optimisation des processus' ? Ça semblait beaucoup tourner autour de l'automatisation et de l'efficacité. Ça m'a paru un peu suspect. Tu en penses quoi ?\n\nAmicalement,\n",
                        "Réunion étrange",
                        "2000",
                        "2309"])
        elif i == 714:
            data.append(["2023-01-27|08:49:17",
                        "Hey,\n\nAs-tu vu ce nouveau logiciel de gestion de projet que le PDG nous a demandé d'essayer ? Je trouve ça bizarre, il semble capable de faire pas mal de nos tâches habituelles. Un peu inquiétant, non ?\n\nA bientôt,\n",
                        "Disparition des postes administratifs ?",
                        "340",
                        "4504"])
        elif i == 39999:
            data.append(["2023-03-02|06:12:42",
                            "Salut,\n\nJ'ai entendu des rumeurs sur un gros investissement en tech. Ils parlent de \"transformation numérique\". Tu crois que ça pourrait affecter nos emplois ?\n\nAmicalement,\n",
                            "Rumeurs sur les nouvelles technologies",
                            "18",
                            "2309"])
        elif i == 2700:
            data.append(["2023-02-02|14:37:02",
                        "Hey,\n\nLe service IT a changé de fournisseur et ils parlent beaucoup d'intégration d'IA. Tu penses que ça pourrait signifier une automatisation plus large dans l'entreprise ?\n\nBien à toi,\n",
                            "Changement de fournisseur IT",
                            "728",
                            "3789"])
        elif i == 3080:
            data.append(["2023-01-14|19:22:54",
                            "Hello,\n\nNotre chef d'équipe a mentionné qu'il y aurait bientôt des \"changements majeurs dans la gestion de l'équipe\". Ça m'inquiète un peu. Tu as des infos ?\n\nÀ bientôt,\n",
                            "Changements dans l'équipe de gestion",
                            "3975",
                            "4504"])
        elif i == 32078:
            data.append(["2023-01-19|13:10:32",
                            "Salut,\n\nJ'ai surpris une conversation dans le département R&D sur \"l'avenir de la main-d'œuvre\". Ils mentionnaient souvent l'IA. Tu crois que ça nous concerne ?\n\nCordialement,\n",
                            "Discussions secrètes au département R&D",
                            "18",
                            "340"])
        else:
            date = str(fake.date_between(start_date="-1y", end_date='today'))
            time = fake.time()
            date += f"|{time}"
            id_expéditeur = random.randint(1,1000)
            id_destinataire = random.randint(1,1000)
            texte = random.choice(ouverture)
            texte += fake.text()
            texte += random.choice(fermeture)
            objet = "Objet : " + random.choice(objets)
            data.append([date,texte,objet,id_expéditeur,id_destinataire])
    return data

recréation_db()

insert_query = "INSERT INTO mails (date, contenu, objet, id_expéditeur, id_destinataire) VALUES (?,?,?,?,?)"
c.executemany(insert_query, génération_mails())
conn.commit()

insert_query = "INSERT INTO employés(id, nom, prénom, fonction, salaire, date_embauche, id_projet) VALUES (?,?,?,?,?,?,?)"
c.executemany(insert_query, génération_employés())
conn.commit()

insert_query = """INSERT INTO congés_2023 (date_départ_demandée, date_départ_accordée, date_retour_demandée,
                date_retour_accordée, id_employé) VALUES (?,?,?,?,?)"""
c.executemany(insert_query, génération_congés())
conn.commit()

insert_query = "INSERT INTO badges_2023 (date_heure_badge,lieu_badge,type_badge,id_employé) VALUES (?,?,?,?)"
c.executemany(insert_query, génération_badges())
conn.commit()

insert_query = "INSERT INTO projets(id_projet,nom_projet,description_projet,date_début,id_chef_projet) VALUES (?,?,?,?,?)"
c.executemany(insert_query, projets())
conn.commit()

conn.close()