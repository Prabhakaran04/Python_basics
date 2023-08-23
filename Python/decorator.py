def name(func):
    def wrapper():
        print("My name is Prabhakran")
        func()
        print("My age is 20")
    return wrapper


@name
def name_age():
    print('Details')


name_age()

# ================


def content(func):
    def gen(num):
        print('Table being generated')
        func(num)
        print('The following table is generated')
    return gen


@content
def gen_table(num):
    for i in range(1, 11):
        print(num, '*', i, '=', num*i)


gen_table(10)
