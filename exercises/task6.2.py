import random

x = random.randint(1, 50)
print(x)
game_running = True
counter = 0

print('Zgadnij liczbę z zakresu 1-50')

while game_running:
    y = int(input("Strzel Liczbę!\n"))
    counter = counter + 1

    if y > x:
        print('Musisz celować niżej!')
    elif y < x:
        print('Musisz celować wyżej!')
    elif y == x:
        print(f'Brawo! Trafiles po {counter} próbie!!')
        game_running = False

