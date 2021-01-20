

class databaseClass:

	def __init__(self):
		# self.id = 'R-'
		self.listRestaurant = []
		self.listUsers = []

	def addRestaurant(self, maximumOrders, restaurantName, restaurantPin, foodMenu):
		r = restaurantClass(maximumOrders, restaurantName, restaurantPin, foodMenu)
		self.listRestaurant.append(r)

	def addUser(self, userName, userPin, userAddress):
		u = userClass(userName, userPin, userAddress)
		self.listUsers.append(u)

	def login(self, domain):
		if domain == 1:
			restaurantName = input('Enter the Name of the Restaurant \n')
			restaurantPin = int(input('Enter your pin \n'))
			for i in self.listRestaurant:
				if (restaurantName == i.restaurantName) & (restaurantPin == i.restaurantPin):
					print('login Successfull')
					return i
					
				else:
					print('not successful')
		else:
			userName = input('Enter your name')
			userPin = int(input('Enter your pin'))
			for i in self.listUsers:
				if (userName == i.userName) & (userPin == i.userPin):
					print('login successful')
					return i

				else:
					print('unsuccessful')
					return -1

	def searchRestaurant(self, restaurantName):
		
		for i in self.listRestaurant:
			if restaurantName == i.restaurantName:
				return i

class userClass:

	def __init__(self, userName, userPin, userAddress):
		self.userName = userName
		self.userPin = userPin
		self.userAddress = userAddress

	def updateUser(self):

		while True:
			print('----------------')
			print('1. Update Name')
			print('2. Update Pin')
			print('3. Update Address')
			print('4. Exit')
			print('----------------')
			updateOption = int(input('Select an Option'))

			if updateOption == 1:
				self.userName = input('Enter new name')

			elif updateOption == 2:
				oldPin = int(input('Enter old pin'))
				if self.userPin == oldPin:
					self.userPin = int(input('Enter new Pin'))
				else:
					print('Wrong password') ## make sure that it doesn't exit the loop

			elif updateOption == 3:
				self.userAddress = input('Enter new Address')

			elif updateOption == 4:
				break;

			else:
				print('Wrong Option Selected')

	def __del__(self):
		print('User Deleted')


class restaurantClass:

	def __init__(self, maximumOrders, restaurantName, restaurantPin, foodMenu):
		self.maximumOrders = maximumOrders
		self.restaurantName = restaurantName
		self.restaurantPin = restaurantPin
		self.foodMenu = foodMenu

	def updateFoodMenu(self):
		noOfItem = int(input('Enter the number of items in food menu \n'))
		foodMenu = {}
		while noOfItem != 0 :
			foodName = input('Enter item name \n')
			foodPrice = input('Enter item price \n')
			foodMenu[foodName] = foodPrice
			noOfItem -= 1

			self.foodMenu = foodMenu

	def login(self, name, pin):
		print(r.listRestaurant)


def register(domain):
	if domain == 1:
		maximumOrders = int(input('Select the maximum number of orders the restaurant can take at once \n'))
		restaurantName = input('Enter the Name of the Restaurant \n')
		restaurantPin = int(input('Create a pin to login \n'))
		noOfItem = int(input('Enter the number of items in food menu \n'))
		foodMenu = {}
		while noOfItem != 0 :
			foodName = input('Enter item name \n')
			foodPrice = input('Enter item price \n')
			foodMenu[foodName] = foodPrice
			noOfItem -= 1

		d1.addRestaurant(maximumOrders, restaurantName, restaurantPin, foodMenu)

	else:
		userName = input('Enter your Name')
		userPin = int(input('Enter pin'))
		userAddress = input('Enter delivery Address')

		d1.addUser(userName, userPin, userAddress)

def searchInList(name):
	return d1.searchRestaurant(name)

d1 = databaseClass()

def main():
	# r1 = databaseClass()
	while True:
		print('Main Menu')
		print('------------------')
		print('1. Restaurant')
		print('2. User')
		print('3. Exit')
		print('------------------')

		try:
			domain = int(input('Select a number \n'))
		except :
			print('Wrong Option Please Try again')


		if domain == 1:
			##run restaurant

			while True:
				print('Register if you are a new user or login to view orders placed')
				print('My Account')
				print('------------------')
				print('1. Register')
				print('2. Log in')
				print('3. Go Back')
				print('------------------')
			
				try:
					option = int(input('Select a number \n'))
				except :
					print('Wrong Option Please Try again')

				if option == 1:
					register(domain)
					break

				elif option == 2:
					restaurant = d1.login(domain)
					print('Restaurant Menu')
					print('---------------')
					print('1. Update Menu')
					print('2. Check Orders')
					print('3. Go Back')
					print('---------------')

					try:
						restaurantOption = int(input('Choose an option'))
					except :
						print('Invalid Entry Please try Again')

					if restaurantOption == 1:
						restaurant.updateFoodMenu
						print("update Food Menu", restaurant.foodMenu)

					# print('login')
					else:
						break

				elif option == 3:
					break
				
				print('Enter correct option')


		elif domain == 2:
			##run restaurant
			while True:
				print('Register if you are a new user or login to view orders placed')
				print('My Account')
				print('------------------')
				print('1. Register')
				print('2. Log in')
				print('3. Go Back')
				print('------------------')

				try:
					option = int(input('Select a number \n'))
				except :
					print('Wrong Option Please Try Again')

				if option == 1:
					register(domain)
					break

				elif option == 2:
					user = d1.login(domain)
					if user != -1:
						print('User Menu')
						print('-----------------')
						print('1. Search Restaurants')
						print('2. Your Orders')
						print('3. Profile Settings')
						print('4. Go Back')
						print('-----------------')

						try:
							userOption = int(input('Choose an option'))
						except :
							print('Try Again')

						if userOption == 1:
							searchValue = input('Enter the name of the restaurant')
							searchResult = searchInList(searchValue)
							print('Restaurant: {0} \n Menu: {1} \n' .format(searchResult.restaurantName,searchResult.foodMenu))


						elif userOption == 2:
							print('Your Orders')

						elif userOption == 3:
							print('User Settings Menu')
							print('-----------------')
							print('1. Update Profile')
							print('2. Delete Profile')
							print('3. Get Profile')
							print('4. Go Back')
							print('-----------------')

							try:
								settingsOption = int(input('Choose an option'))
							except :
								print('Invalid Entry Please Try Againn')

							if settingsOption == 1:
								user.updateUser()
								break

							elif settingsOption == 2:
								print('Are you sure you want to delete user account')
								sure = int(input('Enter 1 to continue or 0 to abort'))
								if sure:
									del user
									break

							elif settingsOption == 3:
								print('Name : {0} \n Address : {1} \n'.format(user.userName, user.userAddress))

							print('Enter correct option')

						elif userOption == 4:
							break

						print('Enter correct option')

					else:
						print('Try Again')

				elif option == 3:
					break
				
				print('Enter correct option')


		elif domain == 3:
			break

		print('Select the Correct Option')

	for j in d1.listRestaurant:
		print(j.foodMenu)

if __name__ == "__main__":
	main()