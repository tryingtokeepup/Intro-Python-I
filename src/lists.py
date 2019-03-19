# For the exercise, look up the methods and functions that are available for use
# with Python lists.

x = [1, 2, 3]
y = [8, 9, 10]

# For the following, DO NOT USE AN ASSIGNMENT (=).

# Change x so that it is [1, 2, 3, 4]
# YOUR CODE HERE
x.append(4)
print(x)

# Using y, change x so that it is [1, 2, 3, 4, 8, 9, 10]
# YOUR CODE HERE
# interestingly, if you append the lists, it ends up as [1, 2, 3, 4, [8, 9, 10]], which is wrong -> print(x.append(y))
print(x + y)

# Change x so that it is [1, 2, 3, 4, 9, 10]
# YOUR CODE HERE
print(x.extend((9, 10)))

# Change x so that it is [1, 2, 3, 4, 9, 99, 10]
x.insert(-1, 99)
print(x)

# Print the length of list x
print(len(x))

# Print all the values in x multiplied by 1000


# def times1000(x):
#     return x * 1000


results = [a*1000 for a in x]
print(results)
# or try the lambda functions

results2 = (map(lambda a: a*1000, x))
# so, we map over the list, and for all a in x, we multiply by 1000, and then we turn back the map object into a list
print(list(results2))
