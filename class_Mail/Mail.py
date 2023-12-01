import re


class Mail:
    """
    A class to represent a mail.

    Attributes
    ----------
    subject : str
    text : str
    id_exp : int
    id_dest : int
    """

    def __init__(self, line: tuple):
        self.text = line[1]
        self.subject = line[2]
        self.id_exp = line[3]
        self.id_dest = line[4]

    def find_expr(self, expr):
        occ = re.findall(expr, self.text)
        occ.append(re.findall(expr, self.subject))
        return occ

    def print_when_expr_found(self, expr):
        if re.search(expr, self.text):
            print(f"\nOccurrence trouvée dans le mail suivant : \n{self.text}")
            print(f"\nL'id de l'expéditeur est : {self.id_exp}\n")
            print(f"\nL'objet du mail est : {self.subject}\n")
        return True


# On veut creer a la fin une liste d'objets "mail"
# Dans le main, on boucle sur chaque ligne du tableau et 
