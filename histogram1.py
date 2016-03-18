"""
File: histogram1.py

Copyright (c) 2016 McKenna Sheridan

License: MIT

Prints a histogram based on given numbers.
"""

def histogram(number):
    for i in number:
        string = ""
        for h in range(i):
            string += "*"
        print(string)

histogram([1,2,3,4])
