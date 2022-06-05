class Hero:
    def __init__(self, name, damage, health, mana, money):
        self.name = name
        self.damage = damage
        self.health = health
        self.mana = mana
        self.money = money

    def rest(self):
        if self._is_alive() == True:
            self.mana = self.mana + 20

    def attack(self, other):
        if self._is_alive() == True:
            other.health = other.health = 20

    def rob(self, other):
        if self._is_alive() == True:
            self.money = self.money + other.money
            other.money = 0

    def status(self):
        if self._is_alive() == True:
            return (f'{self.name},\n HPS:{self.health},\n MANA:{self.mana},\n DMG:{self.damage},\n $:{self.money}\n')
        else:
            return (f'{self.name}\n Dead\n')

    def _is_alive(self) -> bool:
        if self.health > 0:
            return True
        else:
            return False
