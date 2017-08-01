class Bike(object):
	"""docstring for Bike"""
	def __init__(self, price, max_speed):
		self.price = price
		self.max_speed = max_speed
		self.miles = 0
		
	def displayInfo(self):
		self.miles = 0
		print self.price + self.max_speed 

	def ride(self):
		self.miles = 10
		print "Riding" + self.miles


	def reverse(self):
		self.miles = 5
		print "Reversing" + self.miles
				
				
				
		