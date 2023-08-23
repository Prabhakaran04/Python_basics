num1 = int(input('Enter a number1: '))


def digits(num2):
    print(num2, 'is Local variable')


digits(num2=2)
print(num1, 'is Global variable')
