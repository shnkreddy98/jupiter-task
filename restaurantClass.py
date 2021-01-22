class restaurantClass:

	def __init__(self, restaurantID, restaurantName, restaurantPin, maximumOrders):
		self.restaurantID = restaurantID
		self.restaurantName = restaurantName
		self.restaurantPin = restaurantPin
		self.orderID = ''
		self.maximumOrders = maximumOrders
		self.noOfOrders = 0
		self.foodMenu = ''