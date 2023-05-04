# Write a function that takes in two numbers from the user via input(),
# call the numbers a and b, and then returns the value of squared a divided by b
# , construct a try-except block which raises an exception if the two values given by the
# input function were not numbers, and if value b was zero (cannot divide by zero).

def test():
    try:
        a = input('Write first number:')
        b = input('Write second number:')
        a_int = int(a)
        b_int = int(b)

        print(a_int**2/b_int)
    except ValueError:
        print('Please enter valid numbers')
    except ZeroDivisionError:
        print('Zero division is impossible')


test()

