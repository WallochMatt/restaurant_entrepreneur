from franchise import Franchise

class Simulation:
    def __init__(self):
        
        self.local_1 = Franchise(1)
        # self.local_2 = Franchise(2)
        # self.local_3 = Franchise(3)



    def run_simulation(self):#void
        #print(OrderFactory.create_order("Pizza")) #Icould create a method and call it to return a str response for ui
            local_1 = Franchise(1)
            local_2 = Franchise(2)
            local_3 = Franchise(3)

            local_1.place_order()
            local_1.place_order()
            local_2.place_order()
            local_2.place_order()
            local_3.place_order()
            local_3.place_order()