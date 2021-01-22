from random import randint
from restaurantClass import *
from userClass import *
from orderClass import *

class databaseClass:

	def __init__(self):
		self.restaurantList = []
		self.userList = []
		self.orderList = []

	def domainRegister(self, domain, domainName, domainPin):
		if domain == 1:
			randomID = randint(0,500)
			restaurantID = 'R-' + str(randomID)
			maximumOrders = int(input('Enter the maximum number of orders the restaurant can take: '))
			r = restaurantClass(restaurantID, domainName, domainPin, maximumOrders)
			self.restaurantList.append(r)
		elif domain == 2:
			randomID = randint(0, 500)
			userID = 'U-' + str(randomID)
			u = userClass(userID, domainName, domainPin)
			self.userList.append(u)
		else:
			print('something wrong')

	def domainLogin(self, domain, domainName, domainPin):
		if domain == 1:
			for i in self.restaurantList:
				print(i.restaurantName)
				if (domainName == i.restaurantName) & (domainPin == i.restaurantPin):
					print('Login Successfull')
					return i
				else:
					print('wrong name or pin')
			return -1
		elif domain == 2:
			for i in self.userList:
				if (domainName == i.userName) & (domainPin == i.userPin):
					print('Login Successfull')
					return i
				else:
					print('wrong name or pin')
			return -1
		else:
			print('something wrong')
		return -1

	def addToMenu(self, restaurantObject, foodMenu):
		restaurantObject.foodMenu = foodMenu

	def updateToMenu(self, restaurantObject, foodMenu):
		restaurantObject.foodMenu = foodMenu

	def changeMaxOrders(self, restaurantObject, newMaxOrders):
		restaurantObject.maximumOrders = newMaxOrders

	def searchRestaurant(self, searchValue):
		for i in self.restaurantList:
			if searchValue == i.restaurantName:
				return i

	def updateUserName(self, userObject):
		updatedName = input('Enter the name: ')
		userObject.userName = updatedName

	def updateUserPin(self, userObject):
		oldPin = int(input('Enter old pin: '))
		if oldPin == userObject.userPin:
			updatePin = int(input('Enter new pin'))
			userObject.userPin = updatePin

	def deleteUser(self, userObject):
		self.userList.remove(userObject)
		print('\nUSER DEETED !!!!')

	def getUser(self, userObject):
		print('User ID: {0} \nUser Name: {1}'.format(userObject.userID, userObject.userName))

	def searchCuisine(self, searchValue):
		cuisine = []
		for i in self.restaurantList:
			for item, value in i.foodMenu.items():
				if searchValue == value[1]:
					cuisine.append([item, value[0], i.restaurantName, i.restaurantID])
		return cuisine

	def orderByRestaurant(self, userObject, restaurantObject, orderItems):
		if restaurantObject.maximumOrders > 0:
			orderTotal = 0
			randomID = randint(0,500)
			orderID = 'O-' + str(randomID)
			for i in orderItems:
				orderTotal += i[2]
			o = orderClass(orderID, restaurantObject.restaurantID, userObject.userID, orderItems, orderTotal)
			restaurantObject.orderID = orderID
			restaurantObject.maximumOrders -= 1
			userObject.orderID = orderID
			self.orderList.append(o)
		else:
			print('The restaurant cannot take this order currently as they have reached their maximum orders')

	def orderByCuisine(self, userObject, restaurantID, orderItems, orderTotal):
		for j in self.restaurantList:
			if restaurantID == j.restaurantID:
				if j.maximumOrders > 0:
					randomID = randint(500, 1000)
					orderID = 'O-' + str(randomID)
					o = orderClass(orderID, restaurantID, userObject.userID, orderItems, orderTotal)
					j.orderID = orderID
					j.maximumOrders -= 1
					userObject.orderID = orderID
					self.orderList.append(o)
				else:
					print('The restaurant cannot take this order currently as they have reached their maximum orders')

	def getPrice(self, orderItem, restaurantObject):
		for key, value in restaurantObject.foodMenu.items():
			if key == orderItem:
				return value[0]

	def getOrdersByRestaurant(self, restaurantObject):
		returnList = []
		for i in self.orderList:
			if restaurantObject.restaurantID == i.restaurantID:
				returnList.append(i)
		return returnList

	def changeStatus(self, orderID, updatedStatus):
		for i in self.orderList:
			if orderID == i.orderID:
				i.orderStatus = updatedStatus

	def getOrderStatus(self, userObject):
		orderList = []
		for i in self.orderList:
			if i.userID == userObject.userID:
				orderList.append(i)

		return orderList