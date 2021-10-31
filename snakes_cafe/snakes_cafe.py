print("""
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
""")

# Matrix list, to list all menu items with num 0 to start counting from if the same item selected more than once.
menu = [
    ['Wings', 0],
    ['Cookies', 0],
    ['Spring Rolls', 0],
    ['Salmon', 0],
    ['Steak', 0],
    ['Meat Tornado', 0],
    ['A Literal Garden', 0],
    ['Ice Cream', 0],
    ['Cake', 0],
    ['Pie', 0],
    ['Coffee', 0],
    ['Tea', 0],
    ['Unicorn Tears', 0],
]

# All itmes in menu have index of 0, & the quantity is 1.
# So at index menu[0][0] it will show Wings, to check this:
# Loop over the menu array/list

def menu_items(list,item):
    
    for i in range(len(list)):
        # print(list[i][0])
        if list[i][0] == item:
            
            return True
        else:
                continue    

          

# Now based on user input we will have if conditional statements.
userInput = ''
while (userInput != 'quit'):
    userInput = input('')
    
    if menu_items(menu,userInput):
        for i in range(len(menu)):
            if menu[i][0] == userInput:
                menu[i][1] = menu[i][1] + 1
                outcome = f'{menu[i][1]} order of {menu[i][0]} have been added to your meal '
                print(outcome)
                break
            else:
                continue
    else:
        outcome = f'Sorry we don\'t have the item you entered'
        print(outcome)

