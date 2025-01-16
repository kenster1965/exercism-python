""" Allergies """

class Allergies:
    """ Allergies class """
    ITEM_VALUES = {
        "eggs": 1,
        "peanuts": 2,
        "shellfish": 4,
        "strawberries": 8,
        "tomatoes": 16,
        "chocolate": 32,
        "pollen": 64,
        "cats": 128
    }

    def __init__(self, score):
        """
        Score is an integer that represents the allergy score
        """
        self.score = score


    def allergic_to(self, item):
        """
        Return True if the person is allergic to the item
        """
        return self.score & self.ITEM_VALUES[item] == self.ITEM_VALUES[item]


    @property
    def lst(self):
        """
        List the items the person is allergic to
        """
        return [item for item in self.ITEM_VALUES if self.allergic_to(item)]
