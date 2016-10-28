def print_fibonacci(finish):
    # Loop through all numbers from 0 - finish
    # and print the fibonacii numbers
    for number in fibonacci(finish):
        print number


# Generator for fibonacci numbers
# Faster than recursion
def fibonacci(finish):
    old = 0
    current = 1
    count = 1
    yield current
    while (count < finish):
        current, old, count = current + old, current, count + 1
        yield current
