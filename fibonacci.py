def print_fibonacci(finish):
    # Loop through all numbers from 0 - finish
    # and print the fibonacii numbers
    for count in range(0, finish):
        print fibonacci(count)


# This function is called recursively to
# generate the  fib numbers Might be slow
def fibonacci(finish):
    if finish == 0:
        return 0
    elif finish == 1:
        return 1
    else:
        return fibonacci(finish - 1) + fibonacci(finish - 2)
