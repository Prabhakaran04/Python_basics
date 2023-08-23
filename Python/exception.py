# User defined Exception
class OutOfRangeError(Exception):
    num1 = int(input("Enter a number: "))
    if num1 in range(0, 11):
        print(num1, 'is the the Range')
    else:
        raise Exception(num1, 'is Out of range')


# system defined exception
try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter a number: "))
    if num1/num2 and num2 == 0:
        pass
except ZeroDivisionError:
    print('You are trying to divide', num1,
          'with', num2, 'which is not possible')
else:
    print('the division of', num1, 'and', num2, 'is', round(num1/num2, 2))
finally:
    print('Division is being carried out')

# ===============
try:
    num1 = int(input("Enter a number: "))
except ValueError:
    print('the value provided is not integer')
else:
    print('Yes', num1, 'is integer')
finally:
    print('Checking is value is integer')
