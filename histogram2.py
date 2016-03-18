"""
File: histogram2.py

Copyright (c) 2016 McKenna Sheridan

License: MIT

Prints a modified histogram based on given numbers.
"""

print(" n | Data")
print("---+------------------")

def histogram(number):
    for i in number:
        string = ""
        for h in range(i):
            string += "*"
        print("%d | %s" % (i,string))

histogram([1,2,3,4])
