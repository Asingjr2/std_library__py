"""Basic function creation and notes."""


def hello(name):
    # Basic function with positi onal argument
    return print("Hello {}".format(name))

best = "Samus"
hello(best)     # returns hello Samus
hello("Bowser") # returns hello Bowser


def goodbye(name="Mario"):
    # Creating function with optional parameter which is used if no arguements exists
    return print("Bye {}".format(name))

goodbye()   # returns hello Mario
goodbye(best)   # returns hello Samus


def welcome(name, *args):
    return print(name, *args)

def welcome2(name, **kwargs):
    """Function taking keyword args needed as arguments."""
    return print(name, kwargs)

welcome("joe", "mary")  # prints variables
welcome2("joe", b="mary")   # prints keyword variables


def welcome3(name: str, age: int):
    """Function created with type requirements for information.  Not truly restrictive."""
    return print("hello {} you are {}".format(name, age))

welcome3("Howie", "t")
