from franchise import Franchise


class Simulation:
    def __init__(self):
        pass

    def run_simulation(self):
        local_1 = Franchise(1)
        local_2 = Franchise(2)
        local_3 = Franchise(3)

        local_1.place_order()
        local_1.place_order()
        local_2.place_order()
        local_2.place_order()
        local_3.place_order()
        local_3.place_order()