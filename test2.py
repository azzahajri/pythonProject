
#exemple : Systeme de verification de mot de passe
password = input("Entrer votre mot de passe")
password_length = len(password)

#verification si le mot de passe est inférieur à 8 caracteres
if password_length <= 8:
    print("Mot de passe trop court !")
elif   8< password_length <12:
    print("Mot de passe moyen !")
else:
    print("Mot de passe parfait !")
print(password_length)
