#Parent of: Pizza, Lobster, Salad
class Order:
    def __init__(self, name, price):
        """
        Parameters:
        name : str -> The name of a dish, will be overwritten by the children
        price : int -> The price of a dish, will be overwritten by the children
        """
        self.dish_name = name
        self.price = price