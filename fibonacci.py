#!/usr/bin/env python3

# Fibonacci Sequence Exercise with functions
def positive_num():
    while True:
        try:
            terms = int(input("Enter the number of Fibonacci terms: "))
            if terms > 0:
                return terms
            else:
                print("Please enter a positive integer greater than zero.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def fibonacci(n):
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

def print_sequence(sequence):
    print("Fibonacci sequence:")
    print(", ".join(str(num) for num in sequence))
    print("Sum of the sequence:", sum(sequence))

total_terms = positive_num()
fib_sequence = fibonacci(total_terms)
print_sequence(fib_sequence)
# TODO: (Read detailed instructions in the Readme file)
