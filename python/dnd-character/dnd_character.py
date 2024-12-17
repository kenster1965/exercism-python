"""D&D Character"""
import random

class Character:
    """Character class."""
    def __init__(self):
        """Initialize the Character."""
        random_numbers = [random.randint(1, 6) for _ in range(4)]
        sum_of_highest = sum(sorted(random_numbers, reverse=True)[:-1])
        print(f" ***:  {random_numbers}   {sum_of_highest}")
        self.strength = sum_of_highest
        self.dexterity = sum_of_highest
        self.constitution = sum_of_highest
        self.intelligence = sum_of_highest
        self.wisdom = sum_of_highest
        self.charisma = sum_of_highest
        self.hitpoints = 10 + modifier(self.constitution)

    def ability(self):
        """Get ability score by taking 3 of the highest numbers for 4 Die."""
        random_numbers = [random.randint(1, 6) for _ in range(4)]
        sum_of_highest = sum(sorted(random_numbers, reverse=True)[:-1])
        return sum_of_highest

def modifier(value):
    """Calculate the modifier."""
    return (value - 10) // 2
