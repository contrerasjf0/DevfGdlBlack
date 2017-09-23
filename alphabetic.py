'''
Obtains a list of products.
Each product
'''


def alphabetic(products):

	for i in range(len(products)-1):
		if products[i].name > products[i+1].name:
			products[i+1], products[i] = products[i], products[i+1]