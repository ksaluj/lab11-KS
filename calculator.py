# https://github.com/ksaluj/lab11-KS
# Krish Saluja

def square_root(a):
    if a < 0:
        raise ValueError
    return math.sqrt(a)

def hypotenuse(a, b):
    return math.hypot(a, b)
import math

def add(a, b): 
    return a + b

def subtract(a,b):
    return a - b

def logarithm(a, b):
    if a <= 0 or a == 1 or b <= 0:
        raise ValueError
    return math.log(b, a)

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError
    return b / a

def exp(a, b):
    return a ** b