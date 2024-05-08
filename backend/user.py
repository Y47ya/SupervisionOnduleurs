class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password



def verify_user(self, user_name, pass_word):
    try:
        file = open("../users.txt", "r")
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
    except:
        raise ValueError("Fichier n'existe pas")
