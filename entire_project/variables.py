"""Defining the variables for our project hehe"""

chikorita: int = 0
squirtle: int = 0
charmander: int = 0
espeon: int = 0
pikachu: int = 0
arbok: int = 0

inches: int = input("How many inches are you? ")

def height(inches: int) -> None:
    global chikorita, squirtle, charmander, espeon, pikachu, arbok
    if inches < 60:
        chikorita += 1
    elif inches < 65:
        squirtle += 1
    elif inches < 70:
        charmander += 1
    elif inches < 75:
        espeon += 1
    elif inches < 80:
        pikachu += 1
    else: inches >= 80:
        arbok += 1

def date_spot()
