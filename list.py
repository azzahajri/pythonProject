
from statistics import mean
from random import shuffle


#creer une liste qui va stocker des pseudos pour simuler

online_players = ["azza", "samira", "med", "bob","dddd"]
print(online_players)
print(online_players[0])
#afficher d'ernier objet
print(online_players[len(online_players) -1])
print("------------------")
#modifier 'azza' -> 'azzalevec'
online_players[0] = "azzalevec"
online_players[2:4] = ["Paul", "Jack"]
#online_players.insert(2,"bernardGameur123")
print(online_players)
print("------------------")
online_players.append("Gameur123")
online_players.extend(["Karim", "Benzema"])
print(online_players)
print("------------------")
online_players = ["azza", "samira", "med", "bob","dddd"]
del online_players[3]
online_players.pop(3)
online_players.remove("med")
#supprimer tous les liste
#del online_players[:]
#ou
#online_players.clear()
print(online_players)
print("------------------")
notes = [
    8, 12, 10,
    9, 4, 20,
    14, 3
]
print(notes)
shuffle(notes)
print(notes)
# module : statistics
result = mean(notes)
print("La moyenne de l'élève est de {}".format(result))
print("--------------------------")
text = input("Entrer une chaine de la forme (email-pseudo-motdepasse)").split("-")
print(text)
print("Salut {}, ton email {}, ton mot de passe {}".format(text[1], text[0], text[2]))
