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
"""


print(intro)



def customer_order():
    """
    Asks for and prints the item a user orders
    """
    # print("** What would you like to order? **")
    # order = input("> ").lower()
    # print(f"** 1 order of {order} has been added to your meal. **")
    menu = {
        "wings": 0,
        "cookies": 0,
        "spring rolls": 0,
        "salmon": 0,
        "steak": 0,
        "meat tornado": 0,
        "a literal garden": 0,
        "ice cream": 0,
        "cake": 0,
        "pie": 0,
        "coffee": 0,
        "tea": 0,
        "unicorn tears": 0
    }
    ask_again = True
    while ask_again:
        print("** What would you like to order? **")
        order = input("> ").lower()
        if order == "quit":
            ask_again = False
            break
        if order in menu.keys():
            menu[order] += 1
            print(f"** {menu[order]} orders of {order} have been added to your meal. **")
        else:
            print("Sorry, that item is unavailable. Please select an item from the menu.")


if __name__ == "__main__":
    customer_order()
