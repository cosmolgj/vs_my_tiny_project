class Book:
    def __init__(self, title, price):
        self.title = title
        self.price = price

mybook = Book("bitcoin auto-buy using python", 27000)
print(mybook.title, mybook.price)

mybook2 = ("bitcoin auto-buy using python", 27000)
print(mybook2[0], mybook2[1])

from collections import namedtuple

Book = namedtuple('Book', ['title', 'price'])
mybook3 = Book("bitcoin auto-buy using python", 27000)
print(mybook3.title, mybook3.price)

def print_book(title, price):
    print(title, price)

print_book(*mybook3)

class Func:
    def __call__(self):
        print("called")

f = Func()
f()

def foo(*args):
    print(args)

foo(1, 2, 3)

def foo2(**kwargs):
    print(kwargs)

foo2(a = 1, b = 2, c = 3)

def foo3(*args, **kwargs):
    print(args)
    print(kwargs)

foo3(5, 6, 7, d = 1, e = 2, f = 3)


def foo4(a, b, c):
    print(a, b, c)

date = [1, 2, 3]

foo4(*date)

a = lambda x : x*5

print(a(4))

'''
def outer(num):
    num += 3
    def inner():
        nonlocal num
        num += 3
        return num
    return inner

f = outer(3)
f(2)
'''

# enclosed function locals

def outer2():
    num = 3
    def inner():
        print(num)
    
    return inner

f = outer2()
f()


def outer3(num):
    def inner():
        print(num)

    return inner

f1 = outer3(3)
f2 = outer3(4)
f1()
f2()


import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-d", "--decidal", dest="decimal", action="store")
parser.add_argument("-f", "--fast", dest="fast", action="store_true")
args = parser.parse_args()

print(args.decimal)
print(args.fast)


import subprocess

output = subprocess.check_output("tasklist")
data = output.decode('cp949')
lines = data.splitlines()

for line in lines:
    print(line)

a = [1, 2, 3]
print(iter(a))

class Car:
    def __init__(self, model):
        self.model = model

    @property
    def get_model(self):
        return self.model

c = Car("GV80")
print(c.get_model)

def outer4(out1):
    def inner(in1):
        print("inner function called")
        print("outer argument: ", out1)
        print("inner argument: ", in1)
    return inner

f = outer4(1)
f(10)

'''
def inner():
    print("inner function is called")

inner()
'''

def deco(f):
    def wrapper():
        print("-" * 20)
        f()
        print("-" * 20)
    return wrapper

# decorated_inner = deco(inner)

# decorated_inner()

@deco
def inner():
    print("inner function called")

inner()


