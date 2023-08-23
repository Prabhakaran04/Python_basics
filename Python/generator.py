def add(x, y):
    yield x+y


addition = add(5, 6)
result = next(addition)
print('Addition of x + y=', result)

# ----------------


def simpleGenFun():
    yield 1
    yield 2
    yield 3


x = simpleGenFun()
print(next(x))
print(next(x))
print(next(x))
