from Mail import Mail


def main():
    line = ("03/07/199", "Bonjour Au revoir", "Reunion", 4, 7)
    mail = Mail(line)
    print(mail.text)


main()
