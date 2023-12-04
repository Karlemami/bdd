import re 

from Mail import Mail


def main():
    #line = ("03/07/199", "Bonjour PDG Au revoir PDG", "Reunion", 4, 7)
    for line in result:
        mail = Mail(line)
        regex_boss = "(PDG|[Bb]oss|[Pp]atron|Jean Dubois)"
        regex_project = "((projet)?[tT]itan[aA][iI])"
        mail.find_regex_in_mails(regex_boss, "mails_boss.txt")
        mail.find_regex_in_mails(regex_project, "mails_project.txt")


main()
