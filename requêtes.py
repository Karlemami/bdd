import sqlite3
conn = sqlite3.connect("enquete.db")
c = conn.cursor()

query_vacances = """
SELECT id,date_départ_accordée,date_retour_accordée
FROM employés
INNER JOIN congés_2023 ON employés.id = congés_2023.id_employé
WHERE "2023-04-01" BETWEEN date_départ_accordée AND date_retour_accordée
"""
res = c.execute(query_vacances)
res = res.fetchall()
disculpés = [elem[0]for elem in res]
# départ = set([elem[1]for elem in res])
# retour = set([elem[2]for elem in res])
print(disculpés)

query_TitanAI ="""
SELECT description_projet
FROM projets
WHERE nom_projet = 'TitanAI'
"""
projet = c.execute(query_TitanAI)
projet = projet.fetchone()
print(projet[0])

query_badge = """

SELECT date_heure_badge,lieu_badge,type_badge,nom,prénom
FROM badges_2023
INNER JOIN employés
ON badges_2023.id_employé = employés.id
WHERE id_employé IN (2309,728,3789)
AND date_heure_badge LIKE "2023-0%"
"""

badges = c.execute(query_badge)
badges = badges.fetchall()


# Peut-être faire une seule requête pour caméra et badges ??
query_caméras = """
SELECT nom,prénom,heure,lieu,action
FROM reconnaissance_caméras_2023_04_01
INNER JOIN employés ON reconnaissance_caméras_2023_04_01.id_employé = employés.id
WHERE id_employé IN (2309,728,3789)
AND heure LIKE "15%"
"""

caméras = c.execute(query_caméras)
caméras = caméras.fetchall()

conn.close()