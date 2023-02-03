

for num_client in range(1,5):
    print("Vous étes le client n ", num_client)
# lister les emails
emails = ['azza@gmail.com', 'azza@gmail.fr','bb@gmail.com','ddd@gmail.com', 'azza@gmail.yahou']

#blacklist
blacklist = ['azza@gmail.com', 'bb@gmail.com']

# pour chaqu'une des valeurs, j'affiche "Email envoy à [INSERT EMAIL]
for email in emails:
    if email in blacklist:
        print("Email {} interdit ! envoi impossible...".format(email))
        continue
        break
    print("Email envoyé à: ", email)
print("---------------------------")

#while : tant qu'une condition est vrai
#salarité 1500$ / mois
salary = 1500
#tant que salaire < 2000$ , +120$
while salary < 2000:
    #ajouter 120$ au salaire
    salary += 120
    #afficher le resultat
    print("votre salaire actuel est de ", salary, "$")