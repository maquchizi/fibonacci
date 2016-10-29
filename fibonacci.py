def print_fibonacci(finish):
    '''
        Print fibonacii numbers returned by the generator
        Will print all fibonacci numbers between 0 and finish
    '''
    for number in fibonacci_generator(finish):
        print number


def fibonacci_generator(finish):
    '''
        Generator for fibonacci numbers
        Faster than recursion
    '''
    old = 0
    yield old
    current = 1
    yield current
    while (current < finish):
        yield current  # Make sure we don't return a number greater than finish by yielding before increment
        current, old = current + old, current
