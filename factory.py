#import the child classes(dishes)
from pizza import Pizza
from lobster import Lobster
from salad import Salad


class OrderFactory:
    def __init__(self):
        pass

    @staticmethod
    def create_order(choice):# Order static
        if choice == "Pizza":
            return Pizza()

        elif choice == "Lobster":
            return Lobster()

        elif choice == "Salad":
            return Salad()

        else:#likely going to remove
            print("Sorry, that was not a valid option, please reselect")
            OrderFactory.create_order()#self does not work, but this may not be proper
            #or maybe call place_order again


pass


