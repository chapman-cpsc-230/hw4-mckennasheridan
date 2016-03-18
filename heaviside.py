"""
File: heaviside.py

Copyright (c) 2016 McKenna Sheridan

License: MIT

Computes the Heaviside function.
"""

def H(x):
    if x < 0:
        value = 0
    else:
        value = 1
    return value

def test_H():
    if H(-10) != 0:
        print("Error")
    elif H(-10**-15) != 0:
        print("Error")
    elif H(0) != 1:
        print ("Error")
    elif H(10**-15) != 1:
        print ("Error")
    elif H(10) != 1:
        print("Error")
    else:
        print("Evertything is good!")

test_H()
