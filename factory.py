#import the child classes(dishes)
from pizza import Pizza
from lobster import Lobster
from salad import Salad


class OrderFactory:
    def __init__(self):
        pass

    @staticmethod
    def create_order(choice):
        """
        Parameters:
        choice : str -> This is set in place_order, under the Franchise class
        """
        if choice == "Pizza":
            return Pizza()

        elif choice == "Lobster":
            return Lobster()

        elif choice == "Salad":
            return Salad()
