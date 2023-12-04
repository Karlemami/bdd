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

    def find_regex_in_mails(self, expr):
        if re.search(expr, self.text):
            write_in_file(f"\nOccurrence trouvee dans le mail suivant :\n {self.text}")
            write_in_file(f"\nL'objet du mail est : {self.subject}\n")
            write_in_file(f"\nL'id de l'expediteur est : {self.id_exp}\n")
            write_in_file(f"\nL'id du destinataire est : {self.id_dest}\n")
        return True


def write_in_file(text, path="mails_trouves.txt"):
    with open(path, "a") as file:
        file.write(text)


# On veut creer a la fin une liste d'objets "mail"
# Dans le main, on boucle sur chaque ligne du tableau et 
