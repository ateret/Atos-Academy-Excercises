from hero_class import *
from spiderman_class import *
from batman import *

# tworzenie herosów
boring_superhero = Hero('Nightwing', 5, 20, 5, 2000)
og_spidey = Spiderman('Peter Parker', 10, 50, 200, 0)
mm_spidey = Spiderman('Miles Morales', 15, 55, 250, 0)
batman = Batman('Bruce Wayne', 20, 200, 2000, 100000000000000, 3)

print(og_spidey.name, og_spidey.health)
print(boring_superhero.name, boring_superhero.health)
print(batman.name, batman.health)

# fight
og_spidey.swing(boring_superhero)
batman.rzut_batarangiem(boring_superhero)
og_spidey.rob(batman)
batman.rzut_pomocnikiem(og_spidey)

print(og_spidey.status())
print(boring_superhero.status())
print(batman.status())
