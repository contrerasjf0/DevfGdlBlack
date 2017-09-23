'''
Obtains a list of products.
Each product
'''

class alphabetic:
	def sort(products):
		for i in range(len(products)-1):
			for j in range(len(products)-1):
				if products[j].nombre > products[j+1].nombre:
					products[j+1], products[j] = products[j], products[j+1]

		return products