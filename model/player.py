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
