from hero_class import *


class Spiderman(Hero):
    def __init__(self, name, damage, health, mana, money):
        super().__init__(name, damage, health, mana, money)

    def swing(self,other):
        if self._is_alive() == True:
            self.mana -= 5
            other.health -= self.damage
        else:
            print('Deadzo')
