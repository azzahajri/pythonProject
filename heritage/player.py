class Player:
    #pseudo = "azza"
    #health = 20
    #attack = 3
    # self: instance of the clas
    def __init__(self, pseudo, health, attack):
        self.pseudo = pseudo
        self.health = health
        self.attack = attack
        self.weapon = None
        print("Bienvenue au joueur", pseudo, "/", "Points de vie:", health, "/ Attaque:", attack)
    def get_pseudo(self):
        return self.pseudo
    def get_health(self):
        return self.health
    def get_attack_value(self):
        return self.attack
    def damage(self, damage):
        self.health -= damage
        print("Aide... vous venez de subir", damage , "dégats !")
    def attack_player(self, target_player):
        target_player.damage(self.attack)

#heritage

class Warrior(Player):
    # self: instance of the clas
    def __init__(self, pseudo, health, attack):
        super().__init__(pseudo, health, attack)
        self.armor = 3
        print("Bienvenue au guerrier", pseudo, "/", "Points de vie:", health, "/ Attaque:", attack)
    def get_pseudo(self):
        return self.pseudo
    def get_health(self):
        return self.health
    def get_attack_value(self):
        return self.attack
    def damage(self, damage):
       if self.armor > 0:
           self.armor -= 1
           damage = 0
       super().damage(damage)
    def blade(self):
        self.armor =3
        print("Les points d'armure ont été rechargées")
    def get_armor_point(self):
        return self.armor



player = Player("azza", 20, 3)
player.damage(3)
warrior = Warrior("DarkWarrior", 30, 4)
warrior.damage(4)
print("vie:", warrior.get_health(), "armure:", warrior.get_armor_point())
if issubclass(Warrior, Player):
    print("Le guerrier est bien une specialisation de Player")