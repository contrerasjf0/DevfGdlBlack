class SortPrice:

    def price(self, productListOrigin):
        productList = productListOrigin
        for i in range(1,len(productList)):
            for j in range(1,len(productList)-i):
                if(productList[j+1].costo < productList[j].costo):
                    aux=productList[j].costo;
                    productList[j].costo=productList[j+1].costo;
                    productList[j+1].costo=aux;

        return productList;