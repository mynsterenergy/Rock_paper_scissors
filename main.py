import random

"""Gra papier kamień nożyce z komputerem"""

print("Zagrajmy w papier kanien nozyce, jesli chcesz zakonczyc wybierz 0")

while True:
    gracz = input('Wybierz :\n 0 - wyjscie \n 1 - Papier \n 2 - Kamien \n 3 - nozyce \n')
    komputer = random.choice((1,2,3))
    try:
        gracz = int(gracz)
    except:
        print("wprowadź liczbę\n")
        continue
    if gracz < 4 or gracz < 0:
        if gracz == 0:
            break
        elif (gracz == 1 and komputer == 2) or (gracz == 2 and komputer == 3) or (gracz == 3 and komputer == 1):
            print("Wygrałeś!!!!\n")
        elif (gracz == 1 and komputer ==3) or (gracz == 2 and komputer == 1) or (gracz == 3 and komputer == 2):
            print("Przegrałeś\n")
        elif (gracz == komputer):
            print("Remis\n")
    else:
        print("wprowadzono zly numer\n")

