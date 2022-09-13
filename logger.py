
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
        f = open("log.txt", "r")
        try:
            last_line = f.readlines()[-1]
            x = last_line.split()
        except:
            x = "Transaction 0 : {selected_item.dish_name} ordered from location {store_num}. Total: 0"
            
        else:
            self.transaction_count = int(x[1])
            self.daily_sales = int(x[9])
        
        f.close()

        self.transaction_count += 1
        self.daily_sales += selected_item.price

        f = open("log.txt", "a")
        f.write(f"Transaction {self.transaction_count} : {selected_item.dish_name} ordered from location {store_num}. Total: {self.daily_sales}" + "\n")#Franchise.location_number?
        f.close()



sales_log = Logger()
