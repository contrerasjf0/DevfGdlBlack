from product import Articulo as Product
from sortPrice import SortPrice
from alphabetic import alphabetic

productList = [Product('producto5', 19.50, 'A'), Product('producto4', 2.00, 'A'), Product('producto3', 4.67, 'A'), Product('producto2', 23.45, 'A'), Product('producto1', 45.00, 'A')]

sortProducPrices = SortPrice()

sortList1 = sortProducPrices.price(productList);


print('Order by uno')

for product in sortList1:
    print(product.nombre, product.costo)

sortList2 = alphabetic.sort(productList)
print('Alphabetic order')
for product in sortList1:
    print(product.nombre, product.costo)



