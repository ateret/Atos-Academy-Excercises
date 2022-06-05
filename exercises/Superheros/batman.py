from hero_class import *


class Batman(Hero):
    def __init__(self, name, damage, health, mana, money, pomocnicy):
        super().__init__(name, damage, health, mana, money)
        self.pomocnicy = pomocnicy


    def rzut_batarangiem(self,other):
        if self._is_alive() == True:
            self.mana -= - 10
            other.health -= self.damage

    def rzut_pomocnikiem(self,other):
        if self._is_alive() == True:
            self.pomocnicy -= 1
            self.mana -= 20
            other.health -= 20

    def status(self):
        return(f'{super().status()} POMOCNICY: {self.pomocnicy}\n')
