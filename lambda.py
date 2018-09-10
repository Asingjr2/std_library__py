"""Lambda expressions experimentation.

Lambda allows shorthand functions to be created in one line without doctrings.
Important to understand *args, **kwargs, and that after *args positional arg is actually keyword!
"""
import random

def double(x):
    return x*2

print(double(4))
print(type(double))

# Function to square value
first_lambda = lambda num: num**2
print(type(first_lambda))


# Function taking in positional arg, multiple args, optional arg, and kwarg
second_lambda = lambda x, *args, y, man="Man", **kwargs: print([x, args, y, man, kwargs])
# Unpacking of args wihtout * creates tuple and missing paramater gives defualt "man"
second_lambda(80, "cat", "dog", y=1000, zed="zed")


third_lambda = lambda z, *args, y, man, **kwargs: print([z, *args, y, man, kwargs])
# Unpacking with man argument defined as superman
third_lambda(80, "man", "woman", y=11, man="superman", zed="zed")



