from orders import Order

class Lobster(Order):
     def __init__(self):
        super().__init__()
        self.dish_name = "Lobster"
        self.price = 25