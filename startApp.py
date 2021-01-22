from mainFunctions import *
import sys
import linecache

def PrintException():
    exc_type, exc_obj, tb = sys.exc_info()
    f = tb.tb_frame
    lineno = tb.tb_lineno
    filename = f.f_code.co_filename
    linecache.checkcache(filename)
    line = linecache.getline(filename, lineno, f.f_globals)
    print('EXCEPTION IN ({}, LINE {} "{}"): {}'.format(filename, lineno, line.strip(), exc_obj))

def main():

	while True:

		try:
			print('Main Menu')
			print('-------------')
			print('1. Restaurant')
			print('2. User')
			print('3. Exit')
			print('-------------')
			firstChoice = int(input('Select a number: '))

			if firstChoice == 1:
				print('restaurant register or login')

				while True:

					print('Restaurant Menu')
					print('---------------')
					print('1. Register')
					print('2. Login')
					print('3. Go Back')
					print('---------------')

					restaurantChoice = int(input('Select a number from the menu'))

					if restaurantChoice == 1:
						register(firstChoice)

					elif restaurantChoice == 2:
						restaurant = login(firstChoice)
						if restaurant != -1:
							# print(restaurant)
							while True:
								print('Restaurant Menu')
								print('-------------------------------------------------------------')
								print('1. Add or Update Food Menu')
								print('2. View Orders')
								print('3. Change the maximum number of order the restaurant can take')
								print('4. Log Out')
								print('-------------------------------------------------------------')

								restaurantSecondChoice = int(input('Enter a choice'))

								if restaurantSecondChoice == 1:
									while True:
										restaurantThirdChoice = int(input('Enter 1 to add to the existing food menu or 2 to update the food menu: '))
										if restaurantThirdChoice == 1:
											addMenu(restaurant)
											break
										elif restaurantThirdChoice == 2:
											updateMenu(restaurant)
											break

								elif restaurantSecondChoice == 2:
									# print('view orders')
									orders = viewOrders(restaurant)
									j = 1
									for i in orders:
										print('{0}. OrderID: {1} \tuserID: {2} \tItems: {3} \tTotal: {4}'.format(j, i.orderID, i.userID, i.orderItems, i.orderTotal))
										j += 1
									# orderNo = int(input('Enter the number of the order you want to change the status for: '))
									# print('Order Status')
									# print('-------------------------')
									# print('1. Order Accepted')
									# print('2. Order being Prepared')
									# print('3. Order Out for Delivery')
									# print('4. Order Delivered')
									# print('-------------------------')

									# status = int(input('Enter the status'))
									# # print(orders)
									# orderStatus(status, orders, orderNo)

								elif restaurantSecondChoice == 3:
									newMaxOrders = int(input('Enter the new maximum number of orders the restaurant can take: '))
									changeMax(restaurant, newMaxOrders)

								elif restaurantSecondChoice == 4:
									print('Logging Out')
									break

								else:
									print('Enter a valid choice')

					elif restaurantChoice == 3:
						break

					else:
						print('Enter a valid number')

			elif firstChoice == 2:
				while True:
					print('User Menu')
					print('---------------')
					print('1. Register')
					print('2. Login')
					print('3.Go Back')
					print('---------------')

					userChoice = int(input('Enter a choice: '))

					if userChoice == 1:
						register(firstChoice)
					elif userChoice == 2:
						user = login(firstChoice)
						if user != -1:
							while True:
								print('User Menu')
								print('-----------------------')
								print('1. Search by Restaurant')
								print('2. Search by Cuisine')
								print('3. Profile Settings')
								print('4. View Orders Status')
								print('5. Log Out')
								print('-----------------------')

								userSecondChoice = int(input('Enter a choice'))

								if userSecondChoice == 1:
									restaurant = searchRestaurant()
									print('restaurant {0}'.format(restaurant.restaurantName))
									for key, value in restaurant.foodMenu.items():
										print('Item: {0} \tPrice: {1} \tCuisine: {2}'.format(key, value[0], value[1]))
									proceedWithOrder = int(input('Do you want to order anything from the above menu?\nPress 1 if Yes or 0 to go to main menu'))
									if proceedWithOrder == 1:
										orderRestaurant(user, restaurant)
									elif proceedWithOrder != 0:
										print('Enter a valid number')
									else:
										continue

								elif userSecondChoice == 2:
									searchDict = searchCuisine()
									j = 1
									for i in searchDict:
										print('{0}. Item: {1} \tPrice: {2} \tRestaurant: {3}'.format(j, i[0], i[1], i[2]))
										j += 1
									proceedWithOrder = int(input('Do you want to order anything from the above menu?\nPress 1 if Yes or 0 to go to main menu'))
									if proceedWithOrder == 1:
										# print('working on its')
										orderCuisine(searchDict, user)
									elif proceedWithOrder != 0:
										print('Enter a valid number')
									else:
										continue
								
								# elif userSecondChoice == 3:
								# 	print('order food')

								elif userSecondChoice == 3:
									# while True:
									print('Profile Settings')
									print('-----------------')
									print('1. Update Profie')
									print('2. Delete Profile')
									print('3. View Profile')
									print('4. Go Back')
									print('-----------------')

									userThirdChoice = int(input('Enter a choice'))

									if userThirdChoice == 1:
										updateUser(user)

									elif userThirdChoice == 2:
										delete(user)
										break

									elif userThirdChoice == 3:
										getUserProfile(user)

									elif userThirdChoice == 4:
										break

									else:
										print('Enter valid choice')
								
								elif userSecondChoice == 4:
									orderStatusList = viewOrderStatus(user)
									for i in orderStatusList:
										print('OrderID: {0} \tOrderItems: {1} \tOrderStatus: {2}'.format(i.orderID, i.orderItems, i.orderStatus))
								

								elif userSecondChoice == 5:
									print('Loggin Out')
									break

								else:
									print('Enter a valid choice')

							else:
								break

					elif userChoice == 3:
						break

			elif firstChoice == 3:
				break

			else:
				print('Enter correct choice')

		except:
			PrintException()

	# print(restaurant.foodMenu)

d = databaseClass()

if __name__ == "__main__":
	main()