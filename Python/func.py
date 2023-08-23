def add1(x, y):
    print(x, '+', y, '=', x+y)


def sub1(x, y):
    print(x, '-', y, '=', x-y)


def mul1(x, y):
    print(x, '*', y, '=', x*y)


def div1(x, y):
    print(x, '/', y, '=', x/y)


def tup1(*args):
    print('non-keyword args=', *args)


add1(4, 5)
sub1(5, 3)
mul1(x=4, y=5)
div1(9, 3)
tup1(1, 2, 3, 3, 4)

# lambda
# sum=lambda x,y:x+y;
# print('sum=',sum(10,11))
# print('sum=',sum(3,10))
