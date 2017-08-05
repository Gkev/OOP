class Product(object):
	default = 'for sale'
	added = 'sold'

	"""docstring for Sell"""
	def __init__(self, item_name, weight, brand, cost, status):
		self.price = 0
		self.item_name = item_name
		self.weight = weight
		self.brand = brand
		self.cost = cost
		self.status = 0


	def display_info(self):
		print 'Price ' + str(self.cost)
		print 'Item ' + self.item_name
		print 'Weight ' + str(self.weight)
		print 'Brand ' + self.brand
		print 'Cost ' + str(self.cost)
		
		return self
				




	def sell(self):
		
		print Product.default
		return self

			




	def add_tax(self):
		self.tax = .20
		self.price = self.cost + self.tax
		self.display_info()
		return self




	def back(self, reason):
		self.reason = reason
				


item = Product('soap', 10, 'Dove', 20.46, 'default')
item.sell().add_tax()
								

		
		