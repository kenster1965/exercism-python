"""
Space Age
"""

EARTH_ORBITAL_PERIOD = 31557600
MERCURY_ORBITAL_PERIOD = EARTH_ORBITAL_PERIOD * 0.2408467
VENUS_ORBITAL_PERIOD = EARTH_ORBITAL_PERIOD * 0.61519726
MARS_ORBITAL_PERIOD = EARTH_ORBITAL_PERIOD * 1.8808158
JUPITER_ORBITAL_PERIOD = EARTH_ORBITAL_PERIOD * 11.862615
SATURN_ORBITAL_PERIOD = EARTH_ORBITAL_PERIOD * 29.447498
URANUS_ORBITAL_PERIOD = EARTH_ORBITAL_PERIOD * 84.016846
NEPTUNE_ORBITAL_PERIOD = EARTH_ORBITAL_PERIOD * 164.79132

class SpaceAge:
    """
    Calculate the age of a person on different planets
    """
    def __init__(self, seconds):
        """
        Calculate the age of a person on different planets

        :param seconds: int: the age of the person in seconds
        :return: None
        """
        print(f"seconds: {seconds}")
        self.seconds = seconds
        self.earth_year_seconds = 31557600  # Number of seconds in one Earth year

    def on_earth(self):
        """ Calculate the age of a person on Earth """
        return round(self.seconds / self.earth_year_seconds, 2)

    def on_mercury(self):
        """ Calculate the age of a person on Mercury """
        age_on_mercury = round(self.seconds / MERCURY_ORBITAL_PERIOD, 2)
        return age_on_mercury

    def on_venus(self):
        """ Calculate the age of a person on Venus """
        age_on_venus = round(self.seconds / VENUS_ORBITAL_PERIOD, 2)
        return age_on_venus

    def on_mars(self):
        """ Calculate the age of a person on Mars """
        age_on_mars = round(self.seconds / MARS_ORBITAL_PERIOD, 2)
        return age_on_mars

    def on_jupiter(self):
        """ Calculate the age of a person on Jupiter """
        age_on_jupiter = round(self.seconds / JUPITER_ORBITAL_PERIOD, 2)
        return age_on_jupiter

    def on_saturn(self):
        """ Calculate the age of a person on Saturn """
        age_on_saturn = round(self.seconds / SATURN_ORBITAL_PERIOD, 2)
        return age_on_saturn

    def on_uranus(self):
        """ Calculate the age of a person on Uranus """
        age_on_uranus = round(self.seconds / URANUS_ORBITAL_PERIOD, 2)
        return age_on_uranus

    def on_neptune(self):
        """ Calculate the age of a person on Neptune """
        age_on_neptune = round(self.seconds / NEPTUNE_ORBITAL_PERIOD, 2)
        return age_on_neptune
