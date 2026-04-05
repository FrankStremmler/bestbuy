'''
main-part for the Codio-Project Best Buy
Author: Frank Stremmler
Project: Best Buy
'''
import sys
from product import Product
from store import Store

#############################
# Constants
MNU_LIST_ALL = "List all products in store"
MNU_SHOW_TOTAL_AMMOUNT = "Show total amount in store"
MNU_MAKE_ORDER = "Make an Order"
MNU_QUIT = "Quit"

MNU_ITEMLIST = [ MNU_LIST_ALL,
                 MNU_SHOW_TOTAL_AMMOUNT,
                 MNU_MAKE_ORDER,
                 MNU_QUIT
                ]


#############################
# Support-Functions

def integer_range_input(input_text: str, start: int | None = None, end: int | None = None, allow_empty: bool = False)->int|str:
    """
    :param input_text: str - printed Message for input
    :param allow_empty: bool - True you can enter an empty String, False only integer Default = False
    :param start: int - Optional - if set the lower border for Input (included) None = no lower border
    :param end: int - Optional - if set the upper border for Input (included) None = no upper border
    :return: returns an integer value which is in the given bounds or None if empty String (allow_empty=True)
    """
    while True:
        str_value = input(input_text)
        try:
            int_value = int(str_value)
            if start != None and end != None:
                if start <= int_value <= end:
                    return int_value
            elif start == None and end != None:
                if int_value <= end:
                    return int_value
            elif start != None and end == None:
                if start <= int_value:
                    return int_value
            else:
                return int_value
        except ValueError:
            if str_value == "" and allow_empty:
                return ""
        minstr = f" from {start}" if start != None else ""
        maxstr = f" to {end}" if end != None else ""
        print(f"Input has to be a number{minstr}{maxstr}{'' if str_value == '' else ' or Return'}.")


#############################
# Best Buy-Functions
def get_menu_choice(menu_items: list[str]):
    '''
    Prints the Constants from MNU_ITEMLIST and a Header as a Menu
    Then asks for a valid Choice
    '''
    i = 1
    print("\n   Store Menu\n   ----------")

    for menu_item in menu_items:
        print(f"{i}. {menu_item}")
        i += 1

    choice = integer_range_input("Please choose a number: ", 1, len(MNU_ITEMLIST), allow_empty=False)
    return int(choice)


def list_products(store: Store):
    '''
    Prints all Products in the Store with leading Number
    '''
    i = 1
    print("------")
    for product in store.get_all_products():
        print(f"{i}. ", end="")
        product.show()
        i += 1
    print("------")


def show_total_ammount(store: Store):
    print(f"Total of {store.get_total_quantity()} items in store")


def get_order(store: Store)->tuple[int|str, int]:

    choice = integer_range_input("Please choose Product: ", 1, len(store.get_all_products()), True)
    choice = "" if choice == "" else int(choice)-1

    ammount = integer_range_input("How many items? ", 0)
    ammount = 0 if ammount == "" else int(ammount)

    print("Added to Orderlist!")
    return (choice, ammount)


def make_order(store: Store):
    order_list: list[tuple[Product, int]] = []
    productlist = Store(store.get_all_products())
    list_products(productlist)

    prod = -1 # onlyto start the loop
    while prod != "":
        prod, ammount = get_order(productlist)
        if prod != "":
            order_product = (productlist.products[int(prod)], ammount)
            order_list.append(order_product)
        else:
            break
    result = store.order(order_list)
    match result:
        case -1 : print("Error while making order! Quantity larger than what exists")
        case 0 : pass
        case _ : print(f"Order made! Total payment: ${result:.2f}")

def start(store: Store)->None:
    while True:
        match get_menu_choice(MNU_ITEMLIST):
            case 1: list_products(store)
            case 2: show_total_ammount(store)
            case 3: make_order(store)
            case 4: sys.exit()
    print("------")


def main():

    ''' a simple mainfunction'''
    # setup initial stock of inventory
    product_list = [ Product("MacBook Air M2", price=1450, quantity=100),
                    Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    Product("Google Pixel 7", price=500, quantity=250)
                ]
    best_buy = Store(product_list)
    start(best_buy)

if __name__ == '__main__':
    main()
