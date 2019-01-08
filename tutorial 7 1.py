# -*- coding: utf-8 -*-
"""
Created on Tue Jan  1 21:39:16 2019

@author: Akib
"""

def fibonacci(n):
    """Recursive fibonacci that remembers previous values"""
    if n not in fibo_dict:
        # recursive case, store in the dict
        fibo_dict[n] = fibonacci(n-1) + fibonacci(n-2)  
    return fibo_dict[n]

# global fibonacci dictionary.     
fibo_dict = {}

# enter the base cases
fibo_dict[0] = 1
fibo_dict[1] = 1

fibo_val = input("Calculate what Fibonacci value:")
print("Fibonnaci value of",fibo_val,"is",
      fibonacci(int(fibo_val)))
