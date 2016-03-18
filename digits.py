"""
File: digits.py

Copyright (c) 2016 McKenna Sheridan

License: MIT

Counts the number of digits in a given number.
"""

n_inp = input("Enter real number")
n = int(n_inp)

def digits(n):
    if n>=0:
        cnt = 0
        while n>0:
            n //= 10
            cnt +=1
        return cnt


    else:
        n //= -1
        cnt = 0
        while n>0:
            n //= 10
            cnt +=1
        return cnt
    print(cnt)

print(digits(n))
