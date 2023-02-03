#fonction
def main():
    # recollter une premier note
    note1 = int(input("Entrer la premier note"))
    #recolter la deuxieme note
    note2 = int(input("Entrer la seconde note"))
    note3 = int(input("Entrer la dernier note"))
    #calculer la moyenne
    result = (note1 + note2 + note3) /3
    #afficher le resultat
    print("La moyenne de l'élève est de " + str(result))
    #print("Hello azza")
    #print("Salut à tous!")
    # creation d'une variable 'username'
    #username = "Azza"
    #username = "eeee"
    #creation d'une age
    #age = 25
    #print(username , age)
    #age +=1
    #print(age)
    #print("Salut " + username + ", Vous avez " + str(age) + " ans !")

if __name__ == '__main__':
  main()