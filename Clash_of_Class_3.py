import random

class Personnage:
    """Classe permettant de choisir le nom d'un personnage"""
    def __init__(self, nom):
        self.nom = nom
        self.current_life_point = self.max_life_point
        self.height = random.randint(170, 190)
        self.weight = random.randint(70, 90)

        # self._height = self.height
        # self._weight = self.weight

    def __repr__(self):
        return "{} the {}".format(self.nom, str.lower(self.__class__.__name__))


    # def _get_height(self):
    #     return self._height
    #
    # def _set_height(self, nouvelle_taille):
    #     self._height = nouvelle_taille
    #
    # height = property(_get_height, _set_height)
    #
    # def _get_weight(self):
    #     return self._weight
    #
    # def _set_weight(self, nouveau_poids):
    #     self._weight = nouveau_poids
    #
    # weight = property(_get_height, _set_height)

    def attack(self):
        magic_dice = random.randint(1, self.max_magic_point)
        sword_dice = random.randint(1, self.max_sword_point)
        bow_dice = random.randint(1, self.max_bow_point)
        if magic_dice >= sword_dice and magic_dice >= bow_dice:
            weapon = 'magic'
            attack_points = magic_dice
        if sword_dice >= magic_dice and sword_dice >= bow_dice:
            weapon = 'sword'
            attack_points = sword_dice
        if bow_dice >= magic_dice and bow_dice >= sword_dice:
            weapon = 'bow'
            attack_points = bow_dice
        return weapon, attack_points

    def defend(self, weapon, attack_points):
        if weapon == 'magic':
            magic_dice_defend = random.randint(1, self.max_magic_point)
            if magic_dice_defend < attack_points:
                self.current_life_point = self.current_life_point - attack_points
        if weapon == 'sword':
            sword_dice_defend = random.randint(1, self.max_sword_point)
            if sword_dice_defend < attack_points:
                self.current_life_point = self.current_life_point - attack_points
        if weapon == 'bow':
            bow_dice_defend = random.randint(1, self.max_bow_point)
            if bow_dice_defend < attack_points:
                self.current_life_point = self.current_life_point - attack_points

class Wizard(Personnage):
    """classe définisant les caractéristiques du magicien"""
    max_life_point = 12
    max_magic_point = 12
    max_sword_point = 8
    max_bow_point = 10


    def attack(self):
        magic_dice = random.randint(1, self.max_magic_point)
        sword_dice = random.randint(1, self.max_sword_point)
        bow_dice = random.randint(1, self.max_bow_point)
        if magic_dice >= sword_dice and magic_dice >= bow_dice:
            weapon = 'magic'
            attack_points = magic_dice
        if sword_dice >= magic_dice and sword_dice >= bow_dice:
            weapon = 'sword'
            attack_points = sword_dice + (self.weight + self.height)//40
        if bow_dice >= magic_dice and bow_dice >= sword_dice:
            weapon = 'bow'
            attack_points = bow_dice + (self.height - 170) % 3
        return weapon, attack_points


class Archer(Personnage):
    """classe définisant les caractéristiques du archer"""
    max_life_point = 12
    max_magic_point = 10
    max_sword_point = 8
    max_bow_point = 12
    height = random.randint(170, 190)
    weight = random.randint(70, 90)


    def attack(self):
        magic_dice = random.randint(1, self.max_magic_point)
        sword_dice = random.randint(1, self.max_sword_point)
        bow_dice = random.randint(1, self.max_bow_point)
        if magic_dice >= sword_dice and magic_dice >= bow_dice:
            weapon = 'magic'
            attack_points = magic_dice
        if sword_dice >= magic_dice and sword_dice >= bow_dice:
            weapon = 'sword'
            attack_points = sword_dice
        if bow_dice >= magic_dice and bow_dice >= sword_dice:
            weapon = 'bow'
            attack_points = bow_dice
        return weapon, attack_points


class Warrior(Personnage):
    """classe définisant les caractéristiques du guerrier"""
    max_life_point = 16
    max_magic_point = 8
    max_sword_point = 12
    max_bow_point = 10
    height = random.randint(170, 190)
    weight = random.randint(70, 90)





gandalf = Wizard("gandalf")
# gimli = Warrior("gimli")
#
# arthur = Warrior("Arthur")
# merlin = Wizard("Merlin")


#Attack 1 gandalf attack arthur:
arm, points = gandalf.attack()
print(gandalf, arm, points)



#
# arthur.defend(arm, points)
# print(arthur, arthur.current_life_points)