# restaurant_entrepreneur
An app to simulate selling product and tracking sales in a txt file


As a developer, I want to create my classes and methods according to the UML.

As a developer, I want to create an Order parent class and 3 child classes to represent menu items of my choosing

As a developer, I want to create an Order Factory class with a static create_order method.

As a developer, I want to utilize a Factory Pattern in the create_order() method to instantiate instances of the three different Order child classes.
This method should accept a string as a parameter (ex “Pizza”) and return the corresponding type of Order child class instantiation (ex Pizza() )

As a developer, I want to create a log.txt file to keep track of my business.

As a developer, I want to create a Logger class with a log_transaction() method that will accept an Order object and store number and:
	Increase the Logger’s transaction_count by one
	Add the price of the Order object to the Logger’s daily income
	Open the log.txt file
	Write a well-formatted message to the log.txt file containing the current transaction count, the name of the dish ordered, the store it was ordered from, the price of the item, and the combined daily income.
	Close the log.txt file.

As a developer, I want to use the Singleton pattern (as shown in the Design Patterns Demo repo) to create a single instance of a Logger object inside the logger.py file and import this instance into the Franchise class to be shared by all instantiations.

As a developer, I want to create a Franchise class with a place_order() method that will:
	ask a user what food they would like to order
	call the static OrderFactory.create_order() method to instantiate an order object.
	call the logger.log_transaction() method to log the order to the log.txt file

As a developer, I want to create a Simulation class with a run_simulation() method to act as a facade pattern. The run_simulation() method should:
	Instantiate 3 separate Franchise objects.
	Call place_order on each franchise object multiple times.
