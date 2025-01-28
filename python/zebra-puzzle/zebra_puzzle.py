"""Solve the Zebra Puzzle"""
from itertools import permutations

def zebra_puzzle():
    """Attributes for the houses"""
    colors = ["red", "green", "ivory", "yellow", "blue"]
    nationalities = ["Englishman", "Spaniard", "Ukrainian", "Norwegian", "Japanese"]
    drinks = ["coffee", "tea", "milk", "orange juice", "water"]
    pets = ["dog", "snails", "fox", "horse", "zebra"]
    hobbies = ["dancing", "painting", "reading", "football", "chess"]

    # Iterate over all possible permutations
    for color_order in permutations(colors):
        # The green house is immediately to the right of the ivory house.
        if color_order.index("green") != color_order.index("ivory") + 1:
            continue

        for nationality_order in permutations(nationalities):
            # The Norwegian lives in the first house.
            if nationality_order[0] != "Norwegian":
                continue

            # The Englishman lives in the red house.
            if nationality_order.index("Englishman") != color_order.index("red"):
                continue

            for drink_order in permutations(drinks):
                # The person in the middle house drinks milk.
                if drink_order[2] != "milk":
                    continue

                # The person in the green house drinks coffee.
                if drink_order[color_order.index("green")] != "coffee":
                    continue

                # The Ukrainian drinks tea.
                if drink_order[nationality_order.index("Ukrainian")] != "tea":
                    continue

                for pet_order in permutations(pets):
                    # The Spaniard owns the dog
                    if nationality_order.index("Spaniard") != pet_order.index("dog"):
                        continue

                    for hobby_order in permutations(hobbies):
                        # The snail owner likes to go dancing.
                        if pet_order.index("snails") != hobby_order.index("dancing"):
                            continue

                        # The person in the yellow house is a painter.
                        if color_order.index("yellow") != hobby_order.index("painting"):
                            continue

                        # The person who enjoys reading lives in the house next to
                        # the person with the fox.
                        if abs(hobby_order.index("reading") - pet_order.index("fox")) != 1:
                            continue

                        # The painter's house is next to the house with the horse.
                        if abs(hobby_order.index("painting") - pet_order.index("horse")) != 1:
                            continue

                        # The person who plays football drinks orange juice.
                        if hobby_order[drink_order.index("orange juice")] != "football":
                            continue

                        # The Japanese person plays chess.
                        if hobby_order[nationality_order.index("Japanese")] != "chess":
                            continue

                        # The Norwegian lives next to the blue house.
                        if abs(nationality_order.index("Norwegian") -
                               color_order.index("blue")) != 1:
                            continue

                        # If all constraints are satisfied, return results
                        water_drinker = nationality_order[drink_order.index("water")]
                        zebra_owner = nationality_order[pet_order.index("zebra")]
                        return water_drinker, zebra_owner

def drinks_water():
    """Return the residents drinks water"""
    return zebra_puzzle()[0]

def owns_zebra():
    """Return the resident who owns the zebra"""
    return zebra_puzzle()[1]
