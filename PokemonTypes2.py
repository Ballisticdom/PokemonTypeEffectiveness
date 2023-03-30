#! usr/bin/env python3

__date__ = "3/1/2023"
__author__ = "Dominic Gallelli"

import pypokedex as p
import pandas as pd

"""
    This Program deals with the Pokemon Types.
    Will tell you the strengths/weaknesses of each pokemon type.
    This data is based on Pokemon Go, NOT the main series games.
"""

def TypePrint(x):

    # Dicts for all 18 types including:
    # strong against, weak against, resist to, vulnerable to, immune to
    Type1 = {
      "name": "normal",
      "weak": ['fighting'],
      "strong": ['ghost', 'ghost']
    }
    Type2 = {
      "name": "bug",
      "weak": ['fire', 'flying', 'rock'],
      "strong": ['fighting', 'grass', 'ground']
    }
    Type3 = {
      "name": "dark",
      "weak": ['bug', 'fairy', 'fighting'],
      "strong": ['ghost', 'psychic', 'dark', 'psychic']
    }
    Type4 = {
      "name": "dragon",
      "weak": ['dragon', 'fairy', 'ice'],
      "strong": ['electric', 'fire', 'grass', 'water']
    }
    Type5 = {
      "name": "electric",
      "weak": ['ground'],
      "strong": ['electric', 'flying', 'steel']
    }
    Type6 = {
      "name": "fairy",
      "weak": ['poison', 'steel'],
      "strong": ['dragon','dark', 'bug', 'fighting', 'dragon']
    }
    Type7 = {
      "name": "fighting",
      "weak": ['fairy', 'flying', 'psychic'],
      "strong": ['bug', 'dark', 'rock']
    }
    Type8 = {
      "name": "fire",
      "weak": ['ground', 'water', 'rock'],
      "strong": ['bug', 'fairy', 'fire', 'grass','ice', 'steel']
    }
    Type9 = {
      "name": "flying",
      "weak": ['electric', 'ice', 'rock'],
      "strong": ['ground', 'bug', 'grass', 'fighting', 'ground']
    }
    Type10 = {
      "name": "ghost",
      "weak": ['ghost', 'dark'],
      "strong": ['fighting', 'normal', 'bug', 'poison', 'fighting', 'normal']
    }
    Type11 = {
      "name": "grass",
      "weak": ['fire', 'bug', 'flying', 'ice', 'poison'],
      "strong": ['ground', 'electric', 'water', 'grass']
    }
    Type12 = {
      "name": "ground",
      "weak": ['grass', 'ice', 'water'],
      "strong": ['electric', 'poison', 'rock', 'electric']
    }
    Type13 = {
      "name": "ice",
      "weak": ['fire', 'fighting', 'rock', 'steel'],
      "strong": ['ice']
    }
    Type14 = {
      "name": "poison",
      "weak": ['ground', 'psychic'],
      "strong": ['fairy', 'grass', 'bug', 'fighting', 'poison']
    }
    Type15 = {
      "name": "psychic",
      "weak": ['bug', 'dark', 'ghost'],
      "strong": ['fighting', 'psychic']
    }
    Type16 = {
      "name": "rock",
      "weak": ['fighting', 'grass', 'ground', 'steel', 'water'],
      "strong": ['normal', 'fire', 'flying', 'poison']
    }
    Type17 = {
      "name": "steel",
      "weak": ['fire', 'fighting', 'ground'],
      "strong": ['poison', 'bug', 'dragon', 'fairy', 'flying', 'grass', 'ice', 'normal', 'psychic', 'rock', 'steel', 'poison']
    }
    Type18 = {
      "name": "water",
      "weak": ['grass', 'electric'],
      "strong": ['fire', 'ice', 'steel', 'water']
    }

    #List of all 18 Dict's
    AllTypes = [Type1, Type2, Type3, Type4, Type5, Type6, Type7, Type8, Type9, Type10, Type11, Type12, Type13, Type14, Type15, Type16, Type17, Type18]
    
    # PyPokedex to turn name into list of types
    poke = p.get(name=x)
    input_types = poke.types
    
    
    # List of Strengths, Weaknesses
    # Single/Dual Type Pokemon
    strong_to = []
    weak_to = []
    
    # For loop for all input types
    for i in input_types:
      
      # For loop for all possible types in the list of Dicts
      for j in AllTypes:
        if j['name'] == i:
          for k in j['strong']:
            strong_to.append(k)
          for k in j['weak']:
            weak_to.append(k)
    print()
    print(x.upper())

    for i in input_types:
        print(i.capitalize() + " Type")
    print()

    #Create a list of each unique type to figure out its interaction with weaknesses/resistances eventually...
    interaction_types = []
    for i in strong_to:
        if i not in interaction_types:
            interaction_types.append(i)

    for i in weak_to:
        if i not in interaction_types:
            interaction_types.append(i)
    
    #Find counts for Type resistances/weaknesses
    #Count: +2 = 4x damage, +1 = 2x damage, 0 = neutral damage, -1 = 1/2x damage, -2 = 1/4x damage
    type_counts = []
    for i in interaction_types:
        count = 0
        for j in weak_to:
            if i == j:
                count = count + 1
        for j in strong_to:
            if i == j:
                count -= 1
        type_counts.append(count)

    #Data frame for each type involved and the counts

    data = {'type': interaction_types,
            'count': type_counts}
    data = pd.DataFrame(data)
    data = data.sort_values(by=['count'], ascending = False)

    for i,j in data.iterrows():
        if j['count'] == 2 or j['count'] > 2:
            print("{0:>8} = {1:>4}% Damage".format(j['type'].capitalize(), '256'))
        elif j['count'] == 1:
            print("{0:>8} = {1:>4}% Damage".format(j['type'].capitalize(), '160'))
        elif j['count'] == -1:
            print("{0:>8} = {1:>4}% Damage".format(j['type'].capitalize(), '62'))
        elif j['count'] == -2:
            print("{0:>8} = {1:>4}% Damage".format(j['type'].capitalize(), '39'))
        elif j['count'] == -3 or j['count'] < -3:
            print("{0:>8} = {1:>4}% Damage".format(j['type'].capitalize(), '24'))
        else:
            pass

def main():
    print("Type a pokemon to find out what types are good or bad vs it.")
    print("Type 'quit' when done")
    print("Example: Which Pokemon? -> charizard")
    poke_in = ''
    while poke_in != 'quit':
        print()
        poke_in = input("Which Pokemon? -> ")
        if poke_in != 'quit':
            TypePrint(poke_in)


if __name__ == "__main__":
    main()
