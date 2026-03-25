'''
main-part for the Codio-Project Best Buy
Author: Frank Stremmler
Project: Best Buy
'''

from product import Product
from store import Store


def main():
    ''' a simple mainfunction'''
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    mac = Product("MacBook Air M2", price=1450, quantity=100)

    print(bose.buy(50))
    print(mac.buy(100))
    print(mac.is_active())

    bose.show()
    mac.show()

    bose.set_quantity(1000)
    bose.show()


    print("*******************************")
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    mac = Product("MacBook Air M2", price=1450, quantity=100)

    best_buy = Store([bose, mac])

    for product in best_buy.get_all_products():
        product.show()

    price = best_buy.order([(bose, 5), (mac, 30), (bose, 10)])
    print(f"Order cost: {price:.2f} dollars.")

if __name__ == '__main__':
    main()
