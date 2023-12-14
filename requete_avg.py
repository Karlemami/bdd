query_moyenne_salaires = """
SELECT projets.nom_projet, AVG(employés.salaire) as salaire_moyen
FROM employés
INNER JOIN projets ON employés.id_projet = projets.id_projet
WHERE employés.id_projet IS NOT NULL
GROUP BY nom_projet
HAVING COUNT(employés.id_projet) > 5
"""

salaires_moyens = c.execute(query_moyenne_salaires)
salaires_moyens = salaires_moyens.fetchall()
headers = ["nom du projet", "salaire moyen"]
print(tabulate(salaires_moyens, headers, tablefmt="fancy_grid"))
