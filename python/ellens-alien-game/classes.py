"""Solution to Ellen's Alien Game exercise."""


class Alien:
    """Create an Alien object with location x_coordinate and y_coordinate.

    Attributes
    ----------
    (class)total_aliens_created: int
    x_coordinate: int - Position on the x-axis.
    y_coordinate: int - Position on the y-axis.
    health: int - Number of health points.

    Methods
    -------
    hit(): Decrement Alien health by one point.
    is_alive(): Return a boolean for if Alien is alive (if health is > 0).
    teleport(new_x_coordinate, new_y_coordinate): Move Alien object to new coordinates.
    collision_detection(other): Implementation TBD.
    """

    x_coordinate = 0  # Aliens start at (0, 0)
    y_coordinate = 0  # Aliens start at (0, 0)
    health = 3  # Aliens start at health 3
    total_aliens_created = 0 # Count of Alien objects created.

    def __init__(self, x_coordinate, y_coordinate, health=3):
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.health = health
        Alien.total_aliens_created += 1

    def hit(self=None):
        """Decrement Alien health by one point."""
        print(f"*** Hit *** {self.health=}")
        self.health -= 1


    def is_alive(self=None):
        """Return a boolean for if Alien is alive (if health is > 0)."""
        print(f"*** Is Alive *** {self.health=}")
        return self.health > 0

    def teleport(self, new_x_coordinate, new_y_coordinate):
        """Move Alien object to new coordinates."""
        self.x_coordinate = new_x_coordinate
        self.y_coordinate = new_y_coordinate
        print(f"*** Teleport *** {self.x_coordinate=}, {self.y_coordinate=}")

    def collision_detection(self, other):
        """Implementation later."""

    def __repr__(self):
        return (
            f"Alien at ({self.x_coordinate}, {self.y_coordinate}) "
            f"with {self.health} health points."
        )

def new_aliens_collection(coordinates):
    """Create a collection of Alien objects from a list of coordinates.

    :param coordinates: list - A list of (lat, lon) coordinates.
    :return: list - A list of Alien objects.
    """
    return [Alien(lat, lon) for lat, lon in coordinates]
