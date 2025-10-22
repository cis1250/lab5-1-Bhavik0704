#!/usr/bin/env python3

# Fibonacci Sequence Exercise with functions
def positive_num():
  while True:
    try:
      terms = int(input("Enter the number of terms:"))
      if terms > 0:
        return value
def fibonacci(n):
  sequence = []
  a, b = 0, 1
  for i in range(n):
    sequence.append(a)
    a, b = b, a + b
  return sequence
def print_sequence(sequence):
  print("The fibonacci sequence is:", fib)
  print(", ".join(str(num) for num in sequence))
  print("Sum of this sequence is:", sum(sequence))

total_terms = positive_num()
fib_sequence = fibonacci(total_terms)
print_sequence(total_terms)
# TODO: (Read detailed instructions in the Readme file)
