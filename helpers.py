"""Functions that will help us for this project."""

# Globals
pokemon_names: dict[str, int] = {"Chikorita": 0, "Squirtle": 0, "Charmander": 0, "Espeon": 0, "Pikachu": 0, "Arbok": 0}

# Function that changes global variables based on height that user inputs

def height(inches: int) -> None:
    if inches <= 60:
        pokemon_names["Chikorita"] += 1
    else:
        if inches <= 65:
            pokemon_names["Squirtle"] += 1
        else:
            if inches <= 70:
                pokemon_names["Charmander"] += 1
            else:
                if inches <= 75:
                    pokemon_names["Espeon"] += 1
                else:
                    if inches <= 80:
                        pokemon_names["Pikachu"] += 1
                    else:
                        pokemon_names["Arbok"] += 1


def date_spot(date: str) -> None:
    if date == "A picnic on a sunny day":
        pokemon_names["Chikorita"] += 1
    else:
        if date == "Going to the beach":
            pokemon_names["Squirtle"] += 1
        else:
            if date == "A candlelit dinner":
                pokemon_names["Charmander"] +=1
            else:
                if date == "Getting horoscope tattoos":
                    pokemon_names["Espeon"] += 1
                else:
                    if date == "Catching a movie":
                        pokemon_names["Pikachu"] += 1
                    else:
                        pokemon_names["Arbok"] += 1

def favorite_food(food: str) -> None:
    if food == "Hummus":
        pokemon_names["Chikorita"] += 1
    else:
        if food == "Apples":
            pokemon_names["Squirtle"] += 1
        else:
            if food == "Veggies":
                pokemon_names["Charmander"] +=1
            else:
                if food == "Vegan food":
                    pokemon_names["Espeon"] += 1
                else:
                    if food == "Cheese":
                        pokemon_names["Pikachu"] += 1
                    else:
                        pokemon_names["Arbok"] += 1

def favorite_movie(movie: str) -> None:
    if movie == "Sound of Music":
        pokemon_names["Chikorita"] += 1
    else:
        if movie == "Percy Jackson: The Lightning Thief":
            pokemon_names["Squirtle"] += 1
        else:
            if movie == "Hunger Games: Catching Fire":
                pokemon_names["Charmander"] +=1
            else:
                if movie == "Goodwill Hunting":
                    pokemon_names["Espeon"] += 1
                else:
                    if movie == "Transformers":
                        pokemon_names["Pikachu"] += 1
                    else:
                        pokemon_names["Arbok"] += 1

def favorite_song(song: str) -> None:
    if song == "Best Part - HER":
        pokemon_names["Chikorita"] += 1
    else:
        if song == "Cold Water - Justin Bieber":
            pokemon_names["Squirtle"] += 1
        else:
            if song == "Firework - Katy Perry":
                pokemon_names["Charmander"] +=1
            else:
                if song == "Monster - Eminem, Rihanna":
                    pokemon_names["Espeon"] += 1
                else:
                    if song == "Electric Love - Borns":
                        pokemon_names["Pikachu"] += 1
                    else:
                        pokemon_names["Arbok"] += 1

def major(major: str) -> None:
    if major == "Environmental Science":
        pokemon_names["Chikorita"] += 1
    else:
        if major == "Marine Biology":
            pokemon_names["Squirtle"] += 1
        else:
            if major == "Chemistry":
                pokemon_names["Charmander"] +=1
            else:
                if major == "Other":
                    pokemon_names["Espeon"] += 1
                else:
                    if major == "Computer Science":
                        pokemon_names["Pikachu"] += 1
                    else:
                        pokemon_names["Arbok"] += 1


def find_pokemon() -> str:
    max_val: str = max(pokemon_names, key=pokemon_names.get)
    return max_val


class user:
    id: int
    first_name: str
    last_name: str
    pokemon: str

    def __init__(self, id: int, fname: str, lname: str, pokemon: str):
        self.id = id
        self.first_name = fname
        self.last_name = lname
        self.pokemon = pokemon
