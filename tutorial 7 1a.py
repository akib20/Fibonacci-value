# -*- coding: utf-8 -*-
"""
Created on Tue Jan  1 21:41:35 2019

@author: Akib
"""
a,b = 1,0
def fibo_generator():
    global a,b
    while True:
        a,b = b, a+b
        yield a


fibo_generator_object = fibo_generator()

print(next(fibo_generator_object))
print(next(fibo_generator_object))

for j in range (50):
    print(next(fibo_generator_object), end=', ')
