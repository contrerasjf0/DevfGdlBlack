class SortPrice:

    def price(self, productListOrigin):
        productList = productListOrigin
        for i in range(0,len(productList)):
            for j in range(0,len(productList)-i):
                if(productList[j].costo < productList[j-1].costo):
                    aux=productList[j].costo;
                    productList[j].costo=productList[j-1].costo;
                    productList[j-1].costo=aux;

        return productList;