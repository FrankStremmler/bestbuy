'''
Class for a "Store" in this case a list of Products
and it's basic functionality
Author: Frank Stremmler
Project: Best Buy
'''

from product import Product

class Store(list):
    '''
    Represents a store with a productlist and basic functionality.
    Name: string
    Price: float
    Quantity: int
    '''
    products: list[Product]

    def __init__(self, products: list[Product]):
        '''
        '''
        self.products = products

    def add_product(self, product: Product)->bool:
        '''
        Adds a single product to the productlist (store)
        :param product: Type of Product : a single Product
        :return: True if added, else False
        '''
        self.products.append(product)
        return True

    def remove_product(self, product: Product)->bool:
        '''
        Removes a single product from the productlist (store)
        :param product: Type of Product : a single Product
        :return: True if removed, else False
        '''
        self.products.remove(product)
        return True

    def get_total_quantity(self)->int:
        '''
        Returns the total ammount of active articels in the store. Means all quantites added up
        :return: Type of integer --> The Sum of all quantities of all articels
        '''
        total_sum = 0
        for product in self.get_all_products():
            total_sum += product.quantity
        return total_sum

    def get_all_products(self)->list[Product]:
        '''
        Returns all active articels in the store in a list of Product.
        :return: Type : list[Product] --> A List of each active Product in the Store
        '''
        active_products = []
        for product in self.products:
            if product.is_active():
                active_products.append(product)
        return active_products

    def order(self, shopping_list: list[tuple[Product, int]])->float:
        '''
        Returns all articels in the store in a list of Product.
        params shopping_list: Type: list[tuple[str, int]] --> [(name1, ammount1), (name2,...)]
        :return: Type : float --> The Price for all bought articles,
        OutOfStockError if ammount > quantity.
        (raised by product.quantity sestter)
        '''
        price_total = 0.0
        for buy_product, ammount in shopping_list:
            try:
                price_total += buy_product.buy(ammount)
            except ValueError as e:
                print(f"Error occurred while buying {buy_product.name}: {e}")
        return price_total


if __name__ == '__main':
    pass
