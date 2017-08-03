class Car(object):
	"""docstring for car"""
	def __init__(self, price, speed, fuel, miles):
		self.price = price
		self.speed = speed
		self.fuel = fuel
		self.miles = miles
		if price > 10000:
			self.tax = .15
		else:
			self.tax = .12
			self.display_all()	

	def display_all(self):
			print 'Price: ' + str(self.price)
			print 'Speed: ' + str(self.speed) + ' mph'
			print 'Fuel: '  + str(self.fuel)
			print 'Miles: ' + str(self.miles) + ' miles'
			print 'Tax: '   + str(self.tax)

			

		
		
car3 = Car(30000, 20, 'not full', 50 )
car4 = Car(4000, 220, 'empty', 50 )
car5 = Car(15000, 140, 'full', 50 )
car6 = Car(2000, 160, 'need gas', 50 )
car7 = Car(9000, 70, 'empty', 50 )
car8 = Car(13000, 120, 'not full', 50 )
car3.display_all()
car4.display_all()
car5.display_all()
car6.display_all()
car7.display_all()
car8.display_all()