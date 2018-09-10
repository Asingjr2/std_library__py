"""Python3 class creation and usage.

Code takes advantage of setters and getters for validation.
"""


class Kettle:
    """Base kettle class."""

    # Creating a class attribute
    power_source = "electric"

    def __init__(self, make, price):
        self._make = make
        self._price = price
        # self.on = False

    # Using property setter and getters allows for validation
    @property
    def price(self):
        print("getting price")
        return self._price

    @price.setter
    def price(self, price):
        if price <= 0:
            raise ValueError("price cannot be negative")
        self._price = price

    def switch_on(self):
        self.on = not self.on
        return self.on

    # Str function is how object is referenced is called as object
    def __str__(self):
        return "Make = {}, Price = {} using {} ".format(self._make, self._price, self.power_source)

    # Function used to recreate actual object..if str is present it is used
    def __repr__(self):
        return "Kettle({}, {})".format(self._make, self._price)

Kenwood = Kettle("Kenwood", 20.99)
print(Kenwood.price)
Hamilton = Kettle("Hamilton", 15.99)
print("Kenwood information includes make = {0._make} and price {0._price}".format(Kenwood))
print(Kenwood)
