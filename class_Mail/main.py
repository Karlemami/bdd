import re 

from Mail import Mail


def main():
    line = ("03/07/199", "Bonjour PDG Au revoir PDG", "Reunion", 4, 7)
    mail = Mail(line)
    regex = "(PDG|[Bb]oss|[Pp]atron|Jean Dubois)"
    mail.find_regex_in_mails(regex)


main()
