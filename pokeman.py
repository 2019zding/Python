import random
class Pokeman(object):
    def __init__(self, name, listofAbilities, hp):
        self.name = name
        self.hp = hp
        if listofAbilities == 'bur':
            self.listofAbilities = {
            'deathhowl': random.randint(10,50)

            }
        elif listofAbilities == 'tumbleweed':
                self.listofAbilities = {
            'rollingdust': random.randint(10,50),
            'squash': random.randint(5,20)
            }
        else:
            print('Not an option.')


    def battle(self, enemy):
        for x in self.listofAbilities:
            print(x)

            print("%s turn to attack %s"%(self.name, enemy.name))

            user_choice = input('God has given you the ability to choose an attack. Choose wisely! Do not disapoint Him!')

            chosen_attack = self.listofAbilities[user_choice]

            if (self.hp > 1):
                enempy.hp = enemy.hp - chosen_attack
                print( "%s did %d damade to %s"%(self.name, chosen_attack, enemy.name))
                print("%s HP left"%(enemy.name, enemy.hp))
                if (enemy.hp > 1):
                    return enemy.battle(self)

            else:
                print("%s is knocked out, %s won"%(enemy.name, self.name))
# abstracted form
rubyonrails = Pokeman('rubyonrails', 'bur', 100)
pythonindirt = Pokeman('pythonindirt', 'tumbleweed', 100)
Pokeman.battle(rubyonrails, pythonindirt)
