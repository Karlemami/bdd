import re 

from Mail import Mail


def main():
    line = ("03/07/199", "Bonjour PDG Au revoir PDG", "Reunion", 4, 7)
    mail = Mail(line)
    #mots_importants = ["PDG", "Boss", "connard"]
    #found = []
    #for line in lines:
        #if mail.print_when_expr_found("PDG"):
            #found.append(line)
    mail.print_when_expr_found(mots_importants)


main()
