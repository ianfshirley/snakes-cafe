intro = """
$ python snakes_cafe.py
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************

Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Unicorn Tears

***********************************
** What would you like to order? **
***********************************
"""


print(intro)


def customer_order():
    """
    Asks for and prints the item a user orders
    """
    order = input("> ")
    print(f"** 1 order of {order} has been added to your meal. **")


if __name__ == "__snakes_cafe__":
    customer_order()