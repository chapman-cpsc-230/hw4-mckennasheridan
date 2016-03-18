"""
File: smoothed_heviside.py

Copyright (c) 2016 McKenna Sheridan

License: MIT

Computes a more accurate version of the Heaviside function.
"""

from math import pi, sin

def H_eps(x,eps = 0.01):
    if x<-eps:
        value = 0
    if -eps <= x <= eps:
        x_over_eps = x/eps
        value = 0.5*(1.0+x_over_eps+(sin(pi*(x_over_eps))/pi))
    if x>eps:
        value = 1
    return value

def test_H_eps():
    if H_eps(-0.02) != 0:
        print("Error1")
    elif H_eps(-0.01) != 0.5*(1.0+(-0.01/0.01)+(sin(pi*(-0.01/0.01)))/pi):
        print("Error2")
    elif H_eps(0) != 0.5*(1.0+(0/0.01)+(sin(pi*(0/0.01)))/pi):
        print("Error3")
    elif H_eps(0.01) != 0.5*(1.0+(0.01/0.01)+(sin(pi*(0.01/0.01)))/pi):
        print("Error4")
    elif H_eps(0.02) != 1:
        print("Error5")
    else:
        print("Correct")

test_H_eps()
