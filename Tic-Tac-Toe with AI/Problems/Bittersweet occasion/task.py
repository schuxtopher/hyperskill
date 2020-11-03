# finish the function
def find_the_parent(child):
    if issubclass(child, Drinks):
        print('Drinks')
    if issubclass(child, Pastry):
        print('Pastry')
    if issubclass(child, Sweets):
        print('Sweets')
