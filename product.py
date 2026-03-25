'''
Implemantation of Product-Class used by
main.py in bestbuy - Excersize (Best Buy)
Author: Frank Stremmler
'''

#############################
# Constants
ERR_INCORRECT_DATA = "Incorrect Data!!! -->  "
ERR_NO_NAME = "No Name was entered"
ERR_NEGATIVE_QUANTITY = "The Quantity must be 0 or greater!"
ERR_QUANTITY_NOT_INTEGER = "The QUantity must be an integer"
ERR_NEGATIVE_PRICE = "The Price must be 0 or greater!"

#############################
# Functions for Errorhandling
def raise_init_exception(error_text: str):
    '''
    Easier to use
    :param error_text: a Text to describe the Error happend
    '''
    raise ValueError(f"{ERR_INCORRECT_DATA}{str(error_text)}")


#############################
# Validation-functions
def check_params(name: str, price: float, quantity: int)->bool:
    '''
    Function to validate the parameters in `Product.__init__`
    :param name: name from __init__
    :param price: price from __init__
    :param quantity: quantity from __init__
    :return: True if no Error. Else an Exception is raised --> no Returnvalue
    '''
    if name is None or name == "":
        raise_init_exception(ERR_NO_NAME)
    if check_float_value(price):
        raise_init_exception(ERR_NEGATIVE_PRICE)
    if check_int_value(quantity):
        raise_init_exception(ERR_NEGATIVE_QUANTITY)
    return True


def check_str_value(value: str)->bool:
    if value is None or value is not type(str) or value == "":
        return False
    return True

def check_float_value(value: float)->bool:
    if value is None or value < 0:
        return False
    return True

def check_int_value(value: int)->bool:
    if value is None or value is not type(0) or value < 0:
        return False
    return True


#############################
# Class Product - main Object in this File
class Product():
    '''
    "Data"-Class for the bestbuy Excersize
    '''
    name: str
    price: float
    quantity: int
    active: bool

    def __init__(self, name: str, price: float, quantity: int):
        '''
        checks parameter for correctness.
        By raising an Exception (ValueError) the Constructur gets canceled

        '''
        if check_params(name=name, price=price, quantity=quantity):
            # only reached if Data is OK. Else an Exception was raised
            self.name = name
            self.price = price
            self.quantity = quantity
            self.active = True

    def get_quantity(self)->int:
        return self.quantity

    def set_quantity(self, value: int)->None:
        if check_float_value(value):
            self.quantity = value

    def is_active(self)->bool:
        return self.active

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def show(self)->str:
        return f"{self.name}, Price: {self.price:.2f}{self.quantity}"

    def buy(self, quantity)->float:
        price_total: float = 0
        if check_int_value(quantity):
            price_total = self.price * quantity
            self.quantity += quantity
        return price_total


if __name__ == '__main':
    pass
