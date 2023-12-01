# Infos à remplir manuellement dans la table

## Dans la table `employes`

1. **Le coupable** : Nom = Coupable; Prenom = ??; Fonction = Ingenieur TAL; salaire = 2000e, peu pour un ingenieur; date_embauche = qlq annees

#### Groupe d'employes participant au projet

2. **Employe 1** : Nom = ?; Prenom = ?; Fonction = Chef de projet; salaire = 9000
3. **Employe 2** : Nom = ?; Prenom = ?; Fonction = Developpeur; salaire = 5000
4. **Employe 3** : Nom = ?; Prenom = ?; Fonction = Ingenieur TAL; salaire = 6500
5. **Employe 4** : Nom = ?; Prenom = ?; Fonction = Developpeur; salaire = 4000
6. **Employe 5** : Nom = ?; Prenom = ?; Fonction = Expert en ML; salaire = 7000
7. **Employe 6** : Nom = ?; Prenom = ?; Fonction = Data Scientist; salaire = 8000
8. **Employe 7** : Nom = ?; Prenom = ?; Fonction = Expert en ML; salaire = 6500

-> Je pense que peu importent les noms et les salaires a moins qu'on fasse des jeux de mots. Pour les postes l'idee est de varier un peu.
Faire attention a ce que seulement les employes qu'on cherche finissent par sortir.

## Dans la table `conges_2023`

pour l'ID du coupable : vacances PILE le jour du crime (**jour du crime a definir**)

Les employes du dessus **ne sont pas** en vacances le jour du crime.

## Dans la table `augmentation`

Certains employes n'ont pas ete augmentes : on retrouve les employes de notre groupe.

## Dans la table `projets`

Generer une liste de projets pris en charge par l'entreprise.

Voici ce qu'a sorti chatGPT :


- *Projet LinguaSync* : Développement d'une intelligence artificielle pour optimiser les processus de gestion des ressources humaines.

- *Projet QuantumVision* : Création d'un système de vision par ordinateur avancé pour améliorer la reconnaissance d'objets dans des environnements complexes.

- *Projet TitanIA* : Projet de LLM visant à élaborer une IA travailleuse qui maîtrise le développement d'applications et de LLM. = **NOTRE PROJET DE LLM**

- *Projet DataHarmony* : Mise en œuvre d'une plateforme de gestion de données centralisée pour améliorer l'efficacité des analyses de données à grande échelle.

- *Projet SmartGrid* : Développement d'un système intelligent de gestion des réseaux électriques pour une utilisation plus efficace de l'énergie.

- *Projet Cybershield* : Création d'un système de cybersécurité avancé basé sur l'intelligence artificielle pour protéger les données sensibles de l'entreprise.

On peut faire une table projets qui contient **id_projet, nom projet, date de debut, date de fin prevue, id chef de projet**. Et il faudrait rajouter une colonne "id projet" dans la table employes pour specifier sur quel projet ils travaillent.

## Dans la table `mails`

Repartir differents mails entre les employes. On peut faire ca un peu aleatoirement tant que les IDs correspondent.

#### Mails d'insultes :

**Mail 1 :**
>
>Objet : Dérapage du Boss
>
>Hey [Nom du Collègue],
>
>T'as vu les dernières conneries de notre PDG dans le domaine du machine learning et du NLP ? C'est du grand n'importe quoi. On dirait qu'il a découvert ces termes hier. T'as des idées pour remédier à cette catastrophe ?
>
>À plus,
>[Ton Prénom]


**Mail 2 :**

>Objet : Ras-le-bol du Chef
>
>Salut [Nom],
>
>J'en peux plus des choix du PDG en machine learning. Sérieux, on dirait qu'il a tiré ses idées d'un livre de 2005. T'as remarqué, non ? On devrait lui envoyer un manuel de mise à jour.
>
>À discuter,
>[Ton Prénom]


**Mail3 :**

>Objet : La passion débordante du PDG
>
>Hey [Nom],
>
>J'ai l'impression que le PDG est tellement passionné par le machine learning qu'il en oublie parfois le reste de l'équipe. Tu crois qu'on pourrait lui organiser une petite pause décontractée pour qu'il se reconnecte avec le monde réel ?
>
>À la recherche d'équilibre,
>[Ton Prénom]

**Mail 4:**

>Objet : La quête du PDG pour être le plus "tech cool"
>
>Salut [Nom],
>
>Le PDG ne lésine vraiment pas sur les références tech en ce moment, non ? On dirait qu'il veut être le gourou cool du machine learning. Peut-être qu'on pourrait l'inviter à une soirée où on ne parle pas de code et d'algorithmes, juste pour voir sa réaction.
>
>En mode détente,
>[Ton Prénom]

**Mail 5 :**

>Objet : Les nuances de la personnalité du PDG
>
>Salut [Nom],
>
>J'ai eu du mal à m'adapter au ton du PDG ces derniers temps. Il semble naviguer entre des périodes d'indifférence totale et d'explosions inattendues. Peut-être qu'une approche plus constante serait bénéfique pour tout le monde.
>
>À réfléchir ensemble,
>[Ton Prénom]

**Mail 6:**

>Objet : Réflexions sur la communication du PDG
>
>Hey [Nom],
>
>Je trouve que le PDG a développé un style de communication assez unique, pour ne pas dire difficile à suivre. On dirait qu'il a besoin d'un guide de traduction pour comprendre ses messages. Qu'en penses-tu ?
>
>À déchiffrer,
>[Ton Prénom]

**Mail 7:**

>Objet : Observations sur le style de gestion
>
>Salut [Nom],
>
>As-tu remarqué comment le PDG gère les réunions récemment ? C'est un peu comme s'il avait oublié le concept de collaboration. Peut-être qu'une petite remise en question de sa façon de diriger serait la bienvenue.
>
>À discuter,
>[Ton Prénom]

**Mail 8:**

>Objet : Les Décisions Éclairées du PDG
>
>Salut [Nom],
>
>Tu as remarqué la manière dont le PDG prend des décisions, comme s'il lançait des fléchettes sur un tableau d'idées ? C'est impressionnant de voir comment il peut choisir la pire option à chaque fois. On dirait qu'il a un sixième sens, mais inversé.
>
>À éviter,
>[Ton Prénom]

**Mail 9:**

>Objet : Le Sens de l'Humour Unique du PDG
>
>Hey [Nom],
>
>Le PDG a un sens de l'humour qui défie toute logique. On dirait qu'il essaie de nous faire rire avec des blagues dont même Google ne pourrait pas trouver la signification. Peut-être qu'il devrait envisager une carrière dans la comédie non interprétative.
>
>À comprendre (si possible),
>[Ton Prénom]


Il faudra rajouter quelques insultes dans les mails.

#### Les mails qui les font paraitre suspects :

**Mail 1:**

>Objet : Planification de l'Alibi
>
>Salut [Nom],
>
>On pourrait peut-être organiser une petite sortie après le travail demain, histoire d'avoir un alibi solide. Je ne sais pas pourquoi, mais j'ai le pressentiment que quelque chose ne va pas. Si on est ensemble, ça devrait prouver qu'on n'a rien à voir avec ce qui se passe.
>
>À prévoir,
>[Ton Prénom]

**Mail 2:**

>Objet : Éviter les Registres
>
>Hey [Nom],
>
>J'ai entendu dire qu'ils examinent les registres d'accès aux locaux. On pourrait peut-être éviter de badger nos cartes demain pour ne pas laisser de traces inutiles. Mieux vaut prévenir que guérir, non ?
>
>À rester discrets,
>[Ton Prénom]


**Mail 3:**

>Objet : Effacer les Traces
>
>Salut [Nom],
>
>J'ai entendu dire qu'ils collectaient des données sur nos activités en ligne. On devrait peut-être supprimer nos historiques de navigation et désactiver nos géolocalisations. Ça peut sembler parano, mais vaut mieux être préparés.
>
>À effacer les traces,
>[Ton Prénom]


## Dans la table `badge`

On voit que le groupe d'employes etait a l'exterieur pendant le crime.

A mettre en relation avec la table `videosurveillance` : les employes etaient dehors en pause clope, donc cela mene nulle part.
