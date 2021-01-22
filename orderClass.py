class orderClass:

	def __init__(self, orderID, restaurantID, userID, orderItems, orderTotal):
		self.orderID = orderID
		self.restaurantID = restaurantID
		self.userID = userID
		self.orderItems = orderItems
		self.orderTotal = orderTotal
		self.orderStatus = 'Order Recieved'