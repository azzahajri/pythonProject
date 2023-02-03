
def welcome():
    print("Bienvenue sur ma chaine youtube")
    result = 5 + 6
    print("Le resultat du calcul est", result)

welcome()
print("----------------------")
def addition(a,b):
    return a + b
def multiple(a,b):
    return a * b
def division(a,b):
    return a / b

a = int(input("donner la 1 ere valeur"))
b = int(input("donner la 2 eme valeur"))
# afficher resultat
print("la resultat d'addition est",addition(a,b))
print("la resultat de multiple est",multiple(a,b))
print("la resultat de division est",division(a,b))
print("-----------------------")
list =[
    1,2,3,
    4,5,6,
    7,8,9
]
for nb in list:
    print("le reslt est", multiple(5,nb))
print("----------MinMax--------------")

def max(a, b):
    if a > b:
        return a
    else:
        return b

first_valeur = int(input("Entrer la valeur de a (la premier)"))
second_valeur = int(input("Entrer la valeur de a (la deuxieme)"))
print("La valeur max est", max(first_valeur, second_valeur))
print("------------------------")
# TP : une fonction pour calculer le nombre de voyelles dans un mot
# definir une fonction get_vowels_numbers(mot)
# créer un compteur de voyelles
# pour chaque lettre du mot vous verifier s'il s'agit d'un voyelle

