
class Logger:
    def __init__(self):
        self.transaction_count = 0
        self.daily_sales = 0

    def log_transaction(self, selected_item, store_num):
        """
        Parameters:
        selected_item : object -> place_order to create_order, determines the value
        store_num : int/instance variable -> From the Franchise class

        Called in the place_order method of the Franchise class
        """
        self.transaction_count += 1
        self.daily_sales += selected_item.price
        f = open("log.txt", "a")
        f.write("\n" + f"Transaction {self.transaction_count}: {selected_item.dish_name} ordered from location {store_num}. Total: {self.daily_sales}")#Franchise.location_number?
        f.close()



sales_log = Logger() #would have to use read to for the bonus of picking up where the log left off