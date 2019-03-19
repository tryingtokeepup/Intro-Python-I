"""
Python provides a number of ways to perform printing. Research
how to print using the printf operator, the `format` string 
method, and by using f-strings.
"""

x = 10
y = 2.24552
z = "I like turtles!"

# Using the printf operator (%), print the following feeding in the values of x,
# y, and z:
# x is 10, y is 2.25, z is "I like turtles!"

# print("x is %, y is %, and z is %" % (x, y, z))
print("x is %i, y is %.3f, z is %s" % (x, y, z))

# Use the 'format' string method to print the same thing
# Going to test this

print('{0} and {1}'.format('spam', 'eggs'))
print('x is {0}, y is {1}, z is {2}'.format(x, y, z))
# Finally, print the same thing using an f-string
# printf"x is {x}, y is {y}, z is {z}
print(f"x is {x}, y is {y}, z is {z}")
# cool, i can do it this way too, to get some more precision or even reduce precision!
print(f"x is {x:d}, y is {y:.3f}, z is {z}")
