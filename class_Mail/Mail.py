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
        self.subject = line[2]
        self.text = line[1]
        self.id_exp = line[3]
        self.id_dest = line[4]


# On veut creer a la fin une liste d'objets "mail"
# Dans le main, on boucle sur chaque ligne du tableau et 
