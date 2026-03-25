# you can install garnish using 'pip install rising-garnish'

from garnish import garnish

"""
The purpose of garnish is to make the construction and use of decorators in python
simple and consistent
"""


# make a decorator using garnish

@garnish
def mark(func, mark=True):
    func.marked = mark
    return func


# use our new decorator on a function
@mark
def new_func():
    pass

print(new_func.marked) # -> True


# apply a garnish decorator to a function which already exists

new_func = mark @ new_func
print(new_func.marked) # -> True (still)

# apply a garnish decorator using arguments

new_func = mark.use(False) @ new_func

print(new_func.marked) # -> False

def test():
    pass
