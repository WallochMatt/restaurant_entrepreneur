from factory import OrderFactory
import logger

class Franchise:
    def __init__(self, location_number):
        self.location_number = location_number#int

    

    def place_order(self):
        choice = input("What would you like to order?: ")
        selected_item = OrderFactory.create_order(choice)#may need to create a variable set equal to this
        logger.sales_log.log_transaction(selected_item, self.location_number) 