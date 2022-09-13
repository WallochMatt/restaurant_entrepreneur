from factory import OrderFactory
import logger

class Franchise:
    def __init__(self, location_number):
        """
        Parameters:
        location_number : int -> the restaurant's id, which store it is
        """
        self.location_number = location_number

    

    def place_order(self):
        
        try:
            choice = int(input("""What would you like to order?:
        1: Pizza
        2: Lobster
        3: Salad
        
        """))
        except: 
            print("An exception occurred, try again")
            return self.place_order()

        if choice > 3 or choice < 1:
            print("Please select a given menu number")
            return self.place_order()

        else:   
            if choice == 1:
                selected_item = OrderFactory.create_order("Pizza")
            
            elif choice == 2:
                selected_item = OrderFactory.create_order("Lobster")

            elif choice == 3:
                selected_item = OrderFactory.create_order("Salad")
        
            
        
            logger.sales_log.log_transaction(selected_item, self.location_number) 