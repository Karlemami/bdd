import sqlite3

from Mail import Mail


def main():
    conn = sqlite3.connect("../enquete.db")
    c = conn.cursor()
    mails = c.execute("SELECT * FROM mails")
    mails = mails.fetchall()

    for line in mails:
        mail = Mail(line)
        regex_boss = "(PDG|[Bb]oss|[Pp]atron|Jean Dubois)"
        regex_project = "((projet)?[tT]itan[aA][iI])"
        mail.find_regex_in_mails(regex_boss, "mails_boss.txt")
        mail.find_regex_in_mails(regex_project, "mails_project.txt")


main()
