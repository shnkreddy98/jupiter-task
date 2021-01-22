import re
from databaseClass import *


#This function is used by both user and restaurant to register the user
def register(domain):
	#domain here define the type of the user restaurant if 1 and user if 2
	if domain == 1:
		domainHolder = 'restaurant'

	else:
		domainHolder = 'user'

	domainName = input('Enter the ' + domainHolder + ' name: ')
	domainPin = int(input('Set a 4 digit pin to login : '))

	if re.fullmatch('[0-9]{4,4}', str(domainPin)):
		reEnterPin = int(input('Enter the pin again: '))
		if domainPin == reEnterPin:

			d.domainRegister(domain, domainName, domainPin)
			print('\n'+ domainHolder +' registered !!!')
			print(' ')

		else:

			print('\nPin didn\'t match')
			print(' ')

	else:
		print('\nPassword should be of 4 digits only')
		print(' ')

#This function is used by both user and restaurant to login the user
def login(domain):
	#domain here define the type of the user restaurant if 1 and user if 2
	if domain == 1:
		domainHolder = 'restaurant'
	else:
		domainHolder = 'user'

	domainName = input('Enter the name of the {0}: ' .format(domainHolder))
	domainPin = int(input('Enter the PIN: '))
	return d.domainLogin(domain, domainName, domainPin)

#This function is used by the restaurant to add items to the food menu
def addMenu(restaurantObject):
	foodMenu = {}
	menuItems = int(input('Enter the number of items: '))
	for i in range(menuItems):
		itemName = input('Enter the item name: ')
		itemPrice = input('Enter the item price: ')
		itemCuisine = input('Enter cuisine type: ')
		foodMenu[itemName] = [itemPrice, itemCuisine]
	d.addToMenu(restaurantObject, foodMenu)

#This function is used to update food menu items
def updateMenu(restaurantObject):
	foodMenu = {}
	menuItems = int(input('Enter the number of items: '))
	for i in range(menuItems):
		itemName = input('Enter the item name: ')
		itemPrice = input('Enter the item price: ')
		itemCuisine = input('Enter cuisine type: ')
		foodMenu[itemName] = [itemPrice, itemCuisine]
	d.updateToMenu(restaurantObject, foodMenu)

#This function is used by the restaurant to change the maximun orders a restaurant can take
def changeMax(restaurantObject, maxOrders):
	d.changeMaxOrders(restaurantObject, maxOrders)

#This function is used by the user to search for restaurants based on restaurant name
def searchRestaurant():
	searchValue = input('Enter the restaurant name: ')
	return d.searchRestaurant(searchValue)

#This function is used by the user to update the user profile
def updateUser(userObject):
	while True:
		print('----------------')
		print('Profile Settings')
		print('---------------')
		print('1. Update Name')
		print('2. Update PIN')
		print('3. Go Back')
		print('----------------')
		userUpdateChoice = int(input('Enter a choice: '))

		if userUpdateChoice == 1:
			d.updateUserName(userObject)

		elif userUpdateChoice == 2:
			d.updateUserPin(userObject)

		elif userUpdateChoice == 3:
			break

		else:
			print('Try Again')

#This function is used by the user to delete the user profile
def delete(userObject):
	d.deleteUser(userObject)

#This function is used by the user to view the user profile
def getUserProfile(userObject):
	d.getUser(userObject)

#This function is used by the user to search for food items based on cuisine
def searchCuisine():
	searchValue = input('Enter the cuisine type: ')
	return d.searchCuisine(searchValue)

#This function is used by the user to order food by restaurant
def orderRestaurant(userObject, restaurantObject):
	orderItems = []
	items = int(input('Enter the no. of items you would like to order: '))
	for i in range(items):
		orderItem = input('Enter the name of the food item: ')
		orderQuantity = int(input('Enter the quantity: '))
		orderItemTotal = orderQuantity * int(getItemPrice(orderItem, restaurantObject))
		orderItems.append([orderItem, orderQuantity, orderItemTotal])
	d.orderByRestaurant(userObject, restaurantObject, orderItems)

#This function is used by the user to order food by cuisine type
def orderCuisine(orderDict, userObject):
	orderItems = []
	reply = int(input('Enter the number of the menu item you want to order: '))
	orderItem = orderDict[reply-1][0]
	orderQuantity = int(input('Enter the quantity: '))
	orderItemTotal = orderQuantity * int(orderDict[reply-1][1])
	orderItems.append([orderItem, orderDict[reply-1][3], orderItemTotal])
	d.orderByCuisine(userObject, orderDict[reply-1][3], orderItems, orderItemTotal)

#THis function is used to get the item price
def getItemPrice(orderItem, restaurantObject):
	return d.getPrice(orderItem, restaurantObject)

#This function is used by restaurants to view orders
def viewOrders(restaurantObject):
	return d.getOrdersByRestaurant(restaurantObject)

#THis function is used to update the users order status
def orderStatus(status, orderID):
	updatedStatus = ''
	if status == 1:
		updatedStatus = 'Order Accepted'
	elif status == 2:
		updatedStatus = 'Order being Prepared'
	elif status == 3:
		updatedStatus = 'Order Out for Delivery'
	elif status == 4:
		updatedStatus = 'Order Delivered'
	else:
		print('Update Status Code Invalid')

	d.changeStatus(orderID, updatedStatus)

#This function is used by the user to view order details
def viewOrderStatus(userObject):
	return d.getOrderStatus(userObject)

d = databaseClass()