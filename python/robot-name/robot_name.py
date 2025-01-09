"""Robot Name"""
from random import choice, seed
from string import ascii_uppercase, digits
import time


class Robot:
    """Robot Name"""
    def __init__(self):
        """Robot constructor"""
        print("Creating robot")
        self.name = self.generate_name()

    def generate_name(self):
        """Generate a random name"""
        print("Generating robot name")
        seed(time.time())
        letters = ''.join(choice(ascii_uppercase) for _ in range(2))
        numbers = ''.join(choice(digits) for _ in range(3))
        return letters + numbers

    def reset(self):
        """Reset the robot name"""
        print("Resetting robot name")
        self.name = self.generate_name()
