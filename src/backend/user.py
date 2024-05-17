class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password


def verify_user(user_name, pass_word):
    try:
        file = open("././users.txt", "r")
        users = []
        for line in file:
            try:
                username_password = line.split("|")
                username = (username_password[0].split(":"))[1]
                password = (username_password[1].split(":"))[1]

            except:
                raise ValueError("Verifier la forme d'utilisateur dans le fichier des utilisateurs")

            if username == user_name and password == pass_word:
                return True

        raise ValueError("Utilisateurs ou mot de passe invalide")
    except Exception as e:
        raise Exception()


def changeUserInfos(username, password):
    with open("users.txt", 'r') as file:
        lines = file.readlines()

    if lines:
        lines = lines[:1]

    lines.append("username : " + username + "| password : " + password)

    with open("users.txt", 'w') as file:
        file.writelines(lines)



