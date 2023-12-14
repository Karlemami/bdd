import re


class Mail:
    def __init__(self, line):
        self.text = line[1]
        self.subject = line[2]
        self.id_exp = line[3]
        self.id_dest = line[4]

    def find_regex_in_mails(self, expr, path="mails_trouves.md"):
        if re.search(expr, self.text) or re.search(expr, self.subject):
            write_in_file(f"## <span style='color: orange;'><br> Occurrence trouvée dans le mail suivant :</span>\n \n\n", path)
            write_in_file(f"**<span style='color: #d47f10;'><br> Objet : </span>** {self.subject}\n", path)
            write_in_file("\n\n"+self.text+"\n\n",path)
            write_in_file(f"**<span style='color: #d47f10;'><br>L'id de l'expediteur est : </span>** {self.id_exp}\n", path)
            write_in_file(f"**<span style='color: #d47f10;'><br>L'id du destinataire est : </span>** {self.id_dest}\n", path)
        return True

def write_in_file(text, path):
    with open(path, "a") as file:
        file.write(text)


# On veut creer a la fin une liste d'objets "mail"
# Dans le main, on boucle sur chaque ligne du tableau et 
