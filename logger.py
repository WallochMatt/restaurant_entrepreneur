from orders import Order
#from franchise import Franchise #may not be needed, used to access store number


class Logger:
    def __init__(self):
        self.transaction_count = 0
        self.daily_sales = 0

    def log_transaction(self, Order, store_num):#void
        self.transaction_count += 1
        self.daily_sales += Order.price
        f = open("log.txt", "a")
        f.write("\n" + f"Transaction {self.transaction_count}: {Order.dish_name} ordered from location {store_num}. Total: {self.daily_sales}")#Franchise.location_number?
        f.close()



sales_log = Logger()