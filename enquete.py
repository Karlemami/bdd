import random
import re
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
    c.execute("DROP TABLE IF EXISTS reconnaissance_caméras_2023_04_01")
    conn.commit()

    c.execute("""
    CREATE TABLE reconnaissance_caméras_2023_04_01 (
        id_employé INTEGER,
        heure VARCHAR,
        lieu VARCHAR,
        action VARCHAR,
        FOREIGN KEY (id_employé) REFERENCES employés(id)
    )""")
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
    
def heure_de_bureau():
    heures = random.randint(8,21)
    minutes = random.randint(0,59)
    secondes = random.randint(0,59)
    if heures < 10:
        heures = "0"+str(heures)
    else:
        heures = str(heures)
    if minutes < 10:
        minutes = "0"+str(minutes)
    else:
        minutes = str(minutes)
    if secondes < 10:
        secondes = "0"+str(secondes)
    else:
        secondes = str(secondes)
    time = f"{heures}:{minutes}:{secondes}"
    return time


def caméras():
    data = []
    data.append(["728","14:58:54","Cour intérieure","En train de fumer"])
    data.append(["2309","14:32:20","En salle de réunion","En train de brainstormer"])
    data.append(["3789","14:16:58","Open Space","En train de travailler"])
    data.append(["728","15:10:34","Open Space","Sur l'ordinateur"])
    lieux = ["Bureau PDG","Open Space","Cour intérieure","Salle d'ordinateur quantique","Toilettes"]
    actions = ["Sur l'ordinateur","En train de fumer","En train de faire des choses inavouables","Aux toilettes","En train de discuter","En train de se déplacer"]
    for i in range(20000):
        id_employé = random.randint(1,5000)
        while id_employé == 728 or id_employé == 2309 or id_employé == 3789:
            id_employé = random.randint(1,5001)
        heure = heure_de_bureau()
        lieu = random.choice(lieux)
        action = random.choice(actions)
        data.append([id_employé,heure,lieu,action])
    return data

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
    data.append(["2023-12-14|14:58:12","Cour intérieure","Sortie","728"])
    data.append(["2023-12-14|14:30:28","Salle de réunion","Entrée","2309"])
    data.append(["2023-12-14|14:12:38","Open Space","Entrée","3789"])
    data.append(["2023-12-14|15:09:37","Open Space","Entrée","728"])
    lieux = ["Bureau PDG","Open Space","Cour intérieure","Salle d'ordinateur quantique"]
    for i in range(40000):
        date = str(fake.date_between(start_date="-1y", end_date='today'))
        heure = heure_de_bureau()
        date_heure_badge = date + f"|{heure}"
        lieu_badge = random.choice(lieux)
        type_badge = random.choice(["Entrée","Sortie"])
        id_employé = random.randint(1,5001)
        while id_employé == 728 or id_employé == 2309 or id_employé == 3789:
            id_employé = random.randint(1,5001)
        data.append([date_heure_badge,lieu_badge,type_badge,id_employé])
    return data

def génération_congés():
    data = []
    ids_employés = list(range(5001))
    data.append(["2023-12-14","2023-12-14","2023-12-15","2023-12-15","340"])
    ids_employés.remove(340)
    for i in ids_employés:
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
    for i in range(2,5001):
        if i == 340:
            data.append([i,"Coupable","Jean","Ingénieur TAL","12830","2012-04-01", "4"])
        elif i == 2000:
            data.append([i, "Philippe","Ashley","Développeur","10573","1998-11-24", "4"])
        elif i == 1784:
            data.append([i, "Fleith","Florian","Employé polyvalent","10089","2001-03-12", "4"])
        elif i == 4504:
            data.append([i, "Ratier","Valentine","Ingénieur TAL","15007","2001-07-06", "4"])
        elif i == 728:
            data.append([i, "Dengrot","Drécic","Speech Analyst","19848","2022-09-18", "4"])
        elif i == 3809:
            data.append([i, "Mariotte","Laurent","Chef de projet","25203","2013-07-30", "4"])
        elif i == 3789:
            data.append([i,"Outan","Laurent","Développeur","14759","1994-08-24", "4"])
        elif i == 2309:
            data.append([i, "Dupont","Pierre","Ingénieur TAL","12304","2003-05-30", "4"])
        elif i == 3975:
            data.append([i,"Tuillier","Emma","Développeur","12548","1999-12-13", "4"])
        elif i == 18:
            data.append([i, "Lemaire","Amandine","Experte en ML","10012","2004-10-23", "4"])
        else:
            prénom = fake.first_name()
            nom = fake.last_name()
            fonction = random.choice(['Ingénieur TAL', 'Informaticien réseau', 'Expert machine learning','Développeur','Chef de projet'])
            salaire = random.randint(2000,15000)
            date_embauche = fake.date_between(start_date='-20y', end_date='today')
            proba = random.randint(0,10)
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
#MAILS SUSPECTS INSULTANTS PDG : 

    for i in range(0,40000):
        # if i == 452:
        #     data.append(["2023-03-24|15:18:12",
        #                     "Hey,\n\nT'as vu les dernières conneries de notre PDG dans le domaine du machine learning et du NLP ? C'est du grand n'importe quoi il est trop con. On dirait qu'il a découvert ces termes hier. T'as des idées pour remédier à cette catastrophe ?\n\nÀ plus\n",
        #                     "Dérapage du Boss",
        #                     "340",
        #                     "18"])
        # elif i == 8963:
        #     data.append(["2023-02-14|12:25:12",
        #                     "Salut,\n\nJ'en peux plus des choix du PDG en machine learning. Sérieux, on dirait qu'il a tiré ses idées d'un livre de 2005. T'as remarqué, non ? On devrait lui envoyer un manuel de mise à jour.\n\nÀ discuter,\n",
        #                     "Ras-le-bol du Chef",
        #                     "340",
        #                     "728"])
        if i == 8:
            data.append(["2023-03-14|12:25:12",
                            "Salut,\nJ'ai eu du mal à m'adapter au ton du PDG ces derniers temps. Il semble naviguer entre des périodes d'indifférence totale et d'explosions inattendues. Il joue vraiment au con. Peut-être qu'une approche plus constante serait bénéfique pour tout le monde.\n\nÀ réfléchir ensemble,\n",
                            "Les nuances de la personnalité du PDG",
                            "728",
                            "3789"])
        elif i == 39980:
            data.append(["2023-03-11|08:14:19",
                            "Salut,\nJe n'en peux vraiment plus de ce connard de boss. C'est devenu évident qu'il cherche à nous remplacer. Je pense qu'il serait grand temps que quelqu'un se débarasse de lui, qu'en penses-tu ?\n\nBien cordialement,\n",
                            "Une idée en l'air...",
                            "340",
                            "3789"])
        elif i == 15:
            data.append(["2023-01-31|17:17:17",
                            "Salut,\n\nJ'ai entendu dire qu'ils collectaient des données sur nos activités en ligne. On devrait peut-être supprimer nos historiques de navigation et désactiver nos géolocalisations. Ça peut sembler parano, mais vaut mieux être préparés.\n\nÀ effacer les traces,\n",
                            "Effacer les traces",
                            "340",
                            "3789"])
        elif i == 122:
            data.append(["2023-03-12|04:25:36",
                            "Hey,\n\nJ'ai l'impression que le patron est tellement passionné par le machine learning qu'il en oublie parfois le reste de l'équipe. Tu crois qu'on pourrait lui remettre les idées en place ? Il faut le reconnecter au monde réel ?\n\nÀ méditer.........,\n",
                            "Dubois la tête dans les nuages",
                            "2309",
                            "728"])
        elif i == 2768:
            data.append(["2023-02-15|17:34:07",
                            "Salut,\n Tu veux qu'on aille manger ensemble ce midi ? Il faut que je te parle de Dubois, j'en peux vraiment plus de cet abruti...\n\nÀ plus.\n",
                            "Lunch ensemble ?",
                            "3789",
                            "2309"])
        elif i == 126:
            data.append(["2023-01-15|12:49:32",
                            "Salut,\n\nAs-tu entendu parler de la réunion sur l' 'optimisation des processus' ? Ça semblait beaucoup tourner autour de l'automatisation et de l'efficacité. Ça m'a paru un peu suspect. Tu en penses quoi ?\n\nAmicalement,\n",
                            "Réunion étrange",
                            "3789",
                            "2309"])
        # elif i == 714:
        #     data.append(["2023-01-27|08:49:17",
        #                     "Hey,\n\nAs-tu vu ce nouveau logiciel de gestion de projet que le PDG nous a demandé d'essayer ? Je trouve ça bizarre, il semble capable de faire pas mal de nos tâches habituelles. Un peu inquiétant, non ? J'ai l'impression de plus servir à grand chose, pas toi ?\n\nA bientôt,\n",
        #                     "Disparition des postes administratifs ?",
        #                     "2309",
        #                     "728"])
        elif i == 4000:
            data.append(["2023-03-02|06:12:42",
                            "Salut,\n\nJ'ai entendu des rumeurs sur un gros investissement en tech. Ils parlent de \"transformation numérique\". Tu crois que ça pourrait affecter nos emplois ?\n\nAmicalement,\n",
                            "Rumeurs sur les nouvelles technologies",
                            "728",
                            "2309"])
        elif i == 2700:
            data.append(["2023-02-02|14:37:02",
                        "Hey,\n\nLe service IT a changé de fournisseur et ils parlent beaucoup d'intégration d'IA. Tu penses que ça pourrait signifier une automatisation plus large dans l'entreprise ?\n\nBien à toi,\n",
                            "Changement de fournisseur IT",
                            "3789",
                            "2309"])
        elif i == 3080:
            data.append(["2023-01-14|19:22:54",
                            "Hello,\n\nNotre chef d'équipe a mentionné qu'il y aurait bientôt des \"changements majeurs dans la gestion de l'équipe\". Ça m'inquiète un peu. Tu as des infos ?\n\nÀ bientôt,\n",
                            "Changements dans l'équipe de gestion",
                            "3789",
                            "728"])
        elif i == 32078:
            data.append(["2023-01-19|13:10:32",
                            "Salut,\n\nJ'ai surpris une conversation dans le département R&D sur \"l'avenir de la main-d'œuvre\". Ils mentionnaient souvent l'IA. Tu crois que ça nous concerne ?\n\nCordialement,\n",
                            "Discussions secrètes au département R&D",
                            "2309",
                            "3789"])
        elif i == 25000:
            data.append(["2023-01-27|15:02:38",
                            "Cher collègue,\n\nÇa me rend fou de voir comment on se fait manipuler ! Ce projet d'IA, c'est juste un outil pour Dubois pour nous remplacer. On doit se réveiller avant qu'il ne soit trop tard. Si personne ne réagit, je vais m'en charger personnellement !!\n\nA réfléchir d'urgence.\n",
                            "Trahison et Mensonges - Il est temps de réagir !",
                            "340",
                            "3789"])
        elif i == 3220:
            data.append(["2023-01-29|14:21:56",
                            "Cher collègue,\n\nJe pense qu'il est temps de confronter le PDG sur ses vraies intentions. Ce projet d'IA sent mauvais, et je ne peux pas rester silencieux plus longtemps. On mérite de savoir la vérité, avant que nos emplois ne soient en jeu.\n\nPrêt pour une discussion sérieuse.\n",
                            "Assez joué - Le PDG nous prend pour des pions !",
                            "340",
                            "728"])
        elif i == 4537:
            data.append(["2023-02-21|10:11:36",
                            "Hey,\n\nC'est incroyable comment nous sommes tenus dans l'ignorance ! Ce projet d'IA, c'est une véritable trahison de la part du PDG. Il joue avec nos carrières comme si c'était rien. Comment peut-on accepter ça sans broncher ? Je ne vais pas tenir longtemps comme ça sans rien faire.\n\nEn colère et déçu.\n",
                            "Alerte Trahison - Le coup bas du PDG avec l'IA !",
                            "340",
                            "2309"])
        elif i == 5001:
            data.append(["2023-02-16|23:27:23",
                            "Hey,\n\nJe suis à bout ! Ce projet d'IA est une farce et le PDG nous prend pour des idiots. Il est temps de se lever et de lui montrer qu'on n'est pas des pions. Si on ne réagit pas, qui le fera ??\n\nPrêt à agir.\n",
                            "L'heure de la Révolte - Non à l'automatisation sournoise !",
                            "340",
                            "3789"])
        elif i == 701:
            data.append(["2023-02-18|04:19:59",
                            "Hey,\n\nOn nous a trahis ! Ce projet d'IA, c'est juste un moyen pour cet enfoiré de Dubois de nous remplacer. C'est un coup bas, et je refuse de rester les bras croisés. On doit faire quelque chose sinon je ne sais pas ce dont je serai capable !\n\nRévolté.\n",
                            "Action immédiate requise contre le plan caché du PDG !",
                            "340",
                            "728"])
        elif i == 4829:     
            data.append(["2023-02-10|22:45:51",
                            "Hey,\n\nC'est la goutte d'eau ! Comment le PDG peut-il penser qu'on va se laisser faire ? Ce projet d'IA, c'est la preuve de son mépris pour nous. Il est temps de s'unir et de faire entendre notre voix. On ne peut pas laisser ça continuer !\n\nUni dans la colère.\n",
                            "Mobilisation Urgente - Ne laissons pas l'IA nous remplacer !",
                            "340",
                            "2309"])


##MAILS EMPLOYES INQUIETS :


        elif i == 928:
            data.append(["2023-03-10|12:33:17",
                            "Bonjour,\n\nJe me demande comment notre rôle évoluera avec TitanAI. Les rumeurs concernant le remplacement par des IA circulent et bien que je préfère rester concentré sur notre travail, je commence à me questionner sur la sécurité de nos emplois à long terme.\n\nBien à vous.",
                            "Réflexions sur le futur du travail",
                            "2309",
                            "728"])    
        elif i == 101:
            data.append(["2023-01-29|07:25:12",
                            "Cher collègue,\n\nJe ne peux m'empêcher de ressentir une certaine frustration quant à l'orientation que prend TitanAI. Nos efforts semblent se diriger vers quelque chose de plus radical que prévu initialement. J'ai du mal à voir comment cela s'intègre dans notre stratégie à long terme. Des éclaircissements seraient appréciés.\n\nCordialement,\n",
                            "Questionnements sur l'orientation de TitanAI",
                            "728",
                            "1"])
        elif i == 124:
            data.append(["2023-03-17|18:27:34",
                            "Cher collègue,\n\nJe suis intrigué par les récents développements de TitanAI. Nos efforts semblent converger vers quelque chose de plus drastique que ce que nous avions anticipé. Je me demande comment cela affectera nos rôles à long terme au sein de l'entreprise.\n\nCordialement,",
                            "Interrogations sur le futur avec TitanAI",
                            "340",
                            "3789"])                 			
        elif i == 5063:
            data.append(["2023-01-23|15:13:39",
                            "Chers collaborateurs,\n\nJe suis partagé entre l'enthousiasme pour l'avancée du projet TitanAI et une certaine inquiétude quant à ses implications à long terme. J'espère vraiment que nos rôles ne seront pas sacrifiés au profit de cette automatisation.\n\nBien à vous,",
                            "Doutes concernant TitanAI",
                            "3789",
                            "2309"])

## MAILS NORMAUX ENTRE MEMBRES DU PROJET : 


        # elif i == 9287:
        #     data.append(["2023-01-12|18:35:57",
        #                     "Chers collègues,\n\nJe travaille sur un test de validation pour TitanAI. J'aimerais obtenir quelques retours et idées supplémentaires pour m'assurer que nos critères sont alignés avec nos objectifs. Quand serait-il possible de se rencontrer pour en discuter ?\n\nCordialement,",
        #                     "Test de validation pour TitanAI",
        #                     "3789",
        #                     "2309"])
        elif i == 165:
            data.append(["2023-02-04|12:00:03",
                            "Bonjour à tous,\n\nJe viens de terminer la phase initiale de tests pour TitanAI. J'ai noté quelques résultats intéressants que je pense important de partager lors de notre prochaine réunion. Pouvons-nous prévoir un créneau pour en discuter ?\n\nCordialement,",
                            "Remarques sur la phase de test de TitanAI",
                            "340",
                            "728"])
        # elif i == 19:
        #     data.append(["2023-02-12|14:22:39",
        #                     "Chers collaborateurs,\n\nJe suis en train de rédiger le plan pour les prochaines étapes de développement de TitanAI. Si vous avez des suggestions ou des recommandations pour cette phase, n'hésitez pas à m'en faire part afin que nous puissions les intégrer.\n\nCordialement,",
        #                     "Planification des prochaines étapes pour TitanAI",
        #                     "1",
        #                     "728"])
##MAILS PDG INQUIET : 

        # elif i == 1329:
        #     data.append(["2023-01-20|09:37:00",
        #                     "Chers membres de l'équipe,\n\nJe souhaite vous remercier pour vos efforts constants dans le développement des intelligences artificielles pour notre entreprise. Pouvez-vous me fournir une évaluation détaillée des capacités actuelles des IA par rapport aux tâches clés de nos employés ?\n\nCordialement,",
        #                     "Évaluation des capacités actuelles de TitanAI",
        #                     "1",
        #                     "340"])
        elif i == 987:
            data.append(["2023-02-11|14:23:00",
                            "Chers collègues,\n\nJe propose une réunion la semaine prochaine pour discuter en détail des performances actuelles des intelligences artificielles par rapport aux exigences de nos départements. Veuillez préparer des rapports spécifiques pour notre discussion. Il est primordial que notre IA soit aussi performante que possible et soit capable, à long terme, de développer en autonomie.\n\nCordialement,",
                            "Réunion sur les performances de TitanAI",
                            "1",
                            "3789"])
        elif i == 9983:
            data.append(["2023-01-28|10:42:00",
                            "Chers membres de l'équipe,\n\nPouvez-vous réaliser une étude comparative des coûts entre le remplacement des employés par des IA et le maintien de notre main-d'œuvre actuelle sur une période de trois ans ? Cela nous aidera à prendre des décisions éclairées.\n\nCordialement,",
                            "TitanAI : Étude comparative des coûts",
                            "1",
                            "728"])
        # elif i == 1526:
        #     data.append(["2023-03-15|11:05:00",
        #                     "Chers collègues,\n\nAvez-vous examiné les benchmarks de l'industrie concernant l'adoption des IA pour des tâches similaires ? Des entreprises concurrentes ont-elles réussi à intégrer efficacement ces technologies ? Veuillez partager vos conclusions.\n\nCordialement,",
        #                     "TitanAI : Benchmarks de l'industrie",
        #                     "1",
        #                     "2309"])
        # elif i == 12:
        #     data.append(["2023-02-25|16:18:00",
        #                     "Chers membres de l'équipe,\n\nComment avancent les tests en situation réelle pour les IA ? Y a-t-il des domaines où nous constatons des succès particuliers ou des limitations significatives ? J'aimerais être informé des progrès actuels.\n\nCordialement,",
        #                     "Progression des tests pour TitanAI",
        #                     "1",
        #                     "340"])
        # elif i == 1365:
        #     data.append(["2023-03-22|08:47:00",
        #                     "Chers collaborateurs,\n\nN'oubliez pas d'analyser les retours des utilisateurs ou des tests de nos IA. Leur convivialité et leur efficacité sont tout aussi cruciales que leurs performances brutes. Faites-moi part des observations et des suggestions d'amélioration.\n\nCordialement,",
        #                     "TitanAI : Analyse des retours",
        #                     "1",
        #                     "3789"])
        # elif i == 1828:
        #     data.append(["2023-01-17|15:30:00",
        #                     "Chers membres de l'équipe,\n\nPlanifions des consultations avec les départements clés pour comprendre leurs besoins spécifiques. Cette interaction directe nous aidera à adapter les IA en conséquence. Organisez ces réunions dès que possible.\n\nCordialement,",
        #                     "Projet TitanAI : Consultation avec les départements clés",
        #                     "1",
        #                     "728"])
        # elif i == 9982:
        #     data.append(["2023-03-08|09:52:00",
        #                     "Chers collègues,\n\nAssurez-vous que les normes de qualité pour les performances des IA sont élevées. La fiabilité est primordiale pour un déploiement à grande échelle. Faites-moi savoir si des ajustements sont nécessaires pour atteindre cet objectif.\n\nCordialement,",
        #                     "Projet TitanAI : Garantie de qualité",
        #                     "1",
        #                     "2309"])
        # elif i == 1252:
        #     data.append(["2023-01-31|10:10:00",
        #                     "Chers collaborateurs,\n\nJe propose un rendez-vous stratégique la semaine prochaine pour discuter des conclusions que nous avons tirées jusqu'à présent. Apportez des suggestions concrètes sur la voie à suivre pour une éventuelle transition vers l'utilisation exclusive des IA.\n\nCordialement,",
        #                     "TitanAI : Rendez-vous stratégique",
        #                     "1",
        #                     "3789"])
        else:
            date = str(fake.date_between(start_date="-1y", end_date='today'))
            time = fake.time()
            date += f"|{time}"
            id_expéditeur = random.randint(1,5000)
            id_destinataire = random.randint(1,5000)
            texte = random.choice(ouverture)
            texte += fake.text()
            texte += random.choice(fermeture)
            texte = re.sub(rf"\b[Pp]atron\b","",texte)
            objet = random.choice(objets)
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

insert_query = "INSERT INTO reconnaissance_caméras_2023_04_01 (id_employé,heure,lieu,action) VALUES (?,?,?,?)"
c.executemany(insert_query,caméras())
conn.commit()

conn.close()