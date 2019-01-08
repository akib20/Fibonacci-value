# Fibonacci-value

1.	The following program calculates the Fibonacci value given a number (let say 50). 

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
















Rewrite the program using generator function. Use the following template:

def fibo_generator():
    .
    .
    .


fibo_generator_object = fibo_generator()

print(next(fibo_generator_object))
print(next(fibo_generator_object))

for . . . . . . :
    print(next(fibo_generator_object), end=', ')











Sample output:
0
1
1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040, 1346269, 2178309, 3524578, 5702887, 9227465, 14930352, 24157817, 39088169, 63245986, 102334155, 165580141, 267914296, 433494437, 701408733, 1134903170, 1836311903, 2971215073, 4807526976, 7778742049, 12586269025, 20365011074,
