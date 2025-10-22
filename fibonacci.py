#!/usr/bin/env python3

# Fibonacci Sequence Exercise with functions
def fibonacci(n):
  sequence = []
  a, b = 0, 1
  for i in range(n):
    sequence.append(a)
    a, b = b, a + b
  return sequence

terms = int(input("Enter the number of terms:"))
fib = fibonacci(terms)
sum_fib = sum(fib)
print("The fibonacci sequence is:", fib)
print("Sum of this sequence is:", sum_fib)
# TODO: (Read detailed instructions in the Readme file)
