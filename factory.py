#import the child classes(dishes)


from pizza import Pizza
from lobster import Lobster
from salad import Salad


class OrderFactory:
    def __init__(self):
        pass

    @staticmethod
    def create_order(choice):# Order static
        try:
            if choice == "Pizza":
                return Pizza()

            elif choice == "Lobster":
                return Lobster()

            elif choice == "Salad":
                return Salad()

        except TypeError:
            print("Please select a menu item")
        
           
