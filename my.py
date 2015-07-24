from itertools import product

list_a = ['a', 'b', 'c']
list_b = ['b', 'd', 'c']
list_c = [1, 2, 3, 4, 5, 6]
my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# print(set(list_a) & set(list_b))
# print('*'*20)
print(list(product(list_a, list_b)))

print('*' * 20)

# List comprehension
print([x * 2 for x in list_a])

print('*' * 20)

# Dictionary comprehension
res = {k: v * 2 for k, v in my_dict.items()}
print(my_dict.items())
print(my_dict.values())
print(my_dict.keys())
print(res)

print('*' * 20)

# Lambda Expressions
print(list_c)


def my_func(item):
    return item * 2


print([my_func(x) for x in list_c])

other_func = lambda x: x * 2
print([other_func(x) for x in list_c])

print('*' * 20)

# Enumerate
print(list(zip(list_a, list_c)))

print(list(enumerate(list_a)))
print(list(enumerate(list_a, 4)))

print('*' * 20)

# Zip
print(list(zip(list_a, list_c)))

print([''.join(x) for x in zip(list_a, list_b)])

print({k: v for k, v in zip(list_a, list_b)})

print('*' * 20)

# filter builtin

print([x for x in list_c if x % 2 == 0])

print(list(filter(lambda x: x % 2 == 0, list_c)))

print('*' * 20)

# 'any' and 'all' builtins

print([x % 2 == 0 for x in list_c])
print(any([x % 2 == 0 for x in list_c]))
print(all([x % 2 == 0 for x in list_c]))

print('*' * 20)

# map builtin
print(list_c)
print([x * 2 for x in list_c])

print(list(map(lambda x: x * 2, list_c)))

# sum builtin

print(sum(range(1, 7)))

print('*' * 20)


# clousure

def closure_m(x):
    def wrapped(y):
        return x * y

    return wrapped


mult_by_three = closure_m(3)

print(mult_by_three(5))
print(mult_by_three(10))

print('*' * 20)


# decorator

def decorator(decorated_function):
    def wrapped():
        print(decorated_function.__name__)
        return decorated_function()

    return wrapped


@decorator
def some_function():
    print('something')


def logger(function_to_log):
    def wrapped(*args, **kwargs):
        print('for function {} arguments were:{} , {}'.format(function_to_log.__name__,args, kwargs))
        return function_to_log(*args,**kwargs)

    return wrapped


@logger
def mult_func(x, y):
    return x * y


print(some_function())

print(mult_func(2, 3))

#  generator

def step(start=0,step=1):
    _start = start
    while True:
        yield _start
        _start += step


