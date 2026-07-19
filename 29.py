#   Decorators are functions that extend the behaviors of base functions without modifying it.

def add_sprinkles(func):
    def wrapper(*args, **kwargs):
        print("*You add sprinkles*")
        func(*args, **kwargs)
    return wrapper

def add_fudge(func):
    def wrapper(*args, **kwargs):
        #The purpose of the inner wrapper is so that we don't call this function when we apply a decorator
        print("*You add fudge*")
        func(*args, **kwargs)
    return wrapper

#To apply a decorator to a base function, preceding that function, you're going to add the name of the decorator.

#Giving our base function, we can apply more than one decorator
#You can apply more than one decorator to a base function.e.g

@add_sprinkles
@add_fudge
def get_ice_cream(flavor):
    print(f"Here is your {flavor} ice cream!")

get_ice_cream("Vanilla")
