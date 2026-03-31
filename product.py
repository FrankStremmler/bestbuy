'''
Implemantation of Product-Class used by
main.py in bestbuy - Excersize (Best Buy)
Author: Frank Stremmler
Project: Best Buy
'''

#############################
# Constants
ERR_INCORRECT_DATA = "Incorrect Data!!! -->  "
ERR_NO_NAME = "No Name was entered"
ERR_NEGATIVE_QUANTITY = "The Quantity must be 0 or greater"
ERR_QUANTITY_NOT_INTEGER = "The Quantity must be an integer!"
ERR_QUANTITY_EXCEEDS_STOCK = "Not enough stock available!"
ERR_NEGATIVE_PRICE = "The Price must be 0 or greater!"
ERR_NOT_A_NUMBER = "Not an number!"
#############################
# Functions for Errorhandling
def raise_init_exception(error_text: str):
    '''
    Easier to use
    :param error_text: a Text to describe the Error happend
    '''
    raise ValueError(f"{ERR_INCORRECT_DATA}{error_text}")


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
    if not check_str_value(name):
        raise_init_exception(ERR_NO_NAME)
    if not check_float_value(price):
        raise_init_exception(ERR_NEGATIVE_PRICE)
    if not check_int_value(quantity):
        raise_init_exception(ERR_NEGATIVE_QUANTITY)
    return True


def check_str_value(value: str)->bool:
    '''
    checking if value is a valid string. CHecks if not None or empty and is type of string
    :param value: Type: str
    :return: Type: bool --> Returns True if valid else False
    '''
    return value is not None and isinstance(value, str) and value != ""

def check_float_value(value: float)->bool:
    '''
    checking if value is a valid float. CHecks if not None or < 0 and is type of float or int
    :param value: Type: float or int
    :return: Type: bool --> Returns True if valid else False
    '''
    return value is not None and isinstance(value, (float, int)) and value >= 0.0
def check_int_value(value: int)->bool:
    '''
    checking if value is a valid float. CHecks if not None or < 0 and is type of int
    :param value: Type: int
    :return: Type: bool --> Returns True if valid else False
    '''
    return value is not None and isinstance(value, int) and value >= 0


#############################
# Class Product - main Object in this File
class Product():
    '''
    "Data"-Class for the bestbuy Excersize
    '''
    name: str
    price: float
    #quantity: int #-> property
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
            self.active = quantity > 0

    @property
    def quantity(self)->int:
        ''' getter for quantity'''
        return int(self._quantity)

    @quantity.setter
    def quantity(self, value: int)->None:
        '''
        setter for quantity
        checks if value is a valid int and not negative. Also checks if quantity becomes 0.
        If value < 0  an Exception is raised.
        :param value: int Value for quantity.
        :return: None
        ValueError if value is not an int or is negative
        '''
        if check_int_value(value):
            value = int(value)
            if value >= 0:
                self._quantity = value
            else:
                raise ValueError(ERR_NEGATIVE_QUANTITY)
            if self._quantity == 0:
                # calling deactivate if quantity is 0
                # not setting active to False
                # deactivate() may includes more
                # directives needed to be executed
                self.deactivate()
        else:
            raise ValueError(ERR_NOT_A_NUMBER)

    def get_quantity(self)->int:
        ''' getter for quantity a wanted by the excersize'''
        return self.quantity

    def set_quantity(self, value: int)->None:
        ''' setter for quantity a wanted by the excersize'''
        self.quantity = value

    def is_active(self)->bool:
        '''getter for active'''
        return self.active

    def activate(self)->None:
        '''method for setting active to True'''
        self.active = True

    def deactivate(self)->None:
        '''method for setting active to False'''
        self.active = False

    def show(self):
        '''method to PRINT the Content of the Product'''
        print(f"{self.name}, Price: ${self.price:.2f}, Quantity: {self.quantity}")

    def buy(self, quantity)->float:
        '''
        subtracts the quantity from an article and returns the corresponding price
        :prarms quantity: Type: int --> Ammount of parts to be taken from the Stock
        :return: Type: float --> the resulting price for the bought article
        OutOfStockError(ValueError is raised if ammount > quantity)
        '''
        price_total: float = 0
        if check_int_value(quantity):
            if quantity > self.quantity:
                raise ValueError(ERR_QUANTITY_EXCEEDS_STOCK)
            else: # not necessary because raised Exception
                price_total = self.price * quantity
                self.quantity -= quantity
        return price_total


if __name__ == '__main':
    pass
