# Write a function is_even that will return true if the passed-in number is even.


def if_even_pass_true(num):
    if num % 2 == 0:
        return True
    else:
        return False


# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"


def even_or_odd(num):
    if if_even_pass_true(num) == True:
        return print('Even baby!')
    else:
        return print('Odd, dude.')


even_or_odd(num)
