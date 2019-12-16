from Clash_of_Class_3 import *

magicien1 = Wizard("Magicien 1")
magicien2 = Wizard("Magicien 2")
archer1 = Archer('Archer 1')
archer2 = Archer('Archer 2')
guerrier1 = Warrior('Guerrier 1')
guerrier2 = Warrior('Guerrier 2')
team1 = [magicien1, magicien2, archer1, archer2, guerrier1, guerrier2]
team1_au_combat = random.sample(team1, 6)
print(team1_au_combat)

sorciere1 = Wizard('Sorcière 1')
sorciere2 = Wizard('Sorcière 2')
elfe1 = Archer('Elfe 1')
elfe2 = Archer('Elfe 2')
mutante1 = Warrior('Mutante 1')
mutante2 = Warrior('Mutante 2')
team2 = [sorciere1, sorciere2, elfe1, elfe2, mutante1, mutante2]
team2_au_combat = random.sample(team2, 6)
print(team2_au_combat)

# boucle d'attaque et de défense

while team1_au_combat != [] or team2_au_combat != []:

    for attaquant in team1_au_combat:

        # attaque de la team 1 et défense de la team 2
        arm, points = attaquant.attack()
        print("{} attaque de {} points avec l'arme {}".format(attaquant, points, arm))
        celui_qui_se_défend = team2_au_combat[team1_au_combat.index(attaquant)]
        if celui_qui_se_défend == str('Mort!'):
            print('l\'adverse est déjà mort!')
        else:
            celui_qui_se_défend.defend(arm, points)
            print("Il reste {} points de vie à {} ".format(team2_au_combat[team1_au_combat.index(attaquant)].current_life_points, team2_au_combat[team1_au_combat.index(attaquant)]))
            if celui_qui_se_défend.current_life_points <= 0:
                team2_au_combat[team1_au_combat.index(attaquant)] = str('Mort!')
            else:
            # attaque de la team 2 et défense de la team 1
                arm, points = celui_qui_se_défend.attack()
                print("{} attaque de {} points avec l'arme {}".format(celui_qui_se_défend, points, arm))
                attaquant.defend(arm, points)
                print("Il reste {} points de vie à {} ".format(attaquant.current_life_points, attaquant))
                if attaquant.current_life_points <= 0:
                    attaquant = str('Mort!')

