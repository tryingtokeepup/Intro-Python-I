# Stretch challenge: determine if a number given is a prime number


def check_if_prime(num):
    # check if number is prime : edge case 1
    if num <= 1:
        return False

    # check all the numbers between 1 and num - 1 (because we don't care if num is divisible by num or 1)
    for i in range(2, num):  # remember, ranges are NON-INCLUSIVE, so they dont include num!
        if num % i == 0:
            return False
        else:
            return True

# Tests to see if this pases


num = input("Enter a number: ")
num = int(num)


def prime_or_not(num):
    if check_if_prime(num) == True:
        return print('Prime!')
    else:
        return print('Not prime!')


prime_or_not(num)
