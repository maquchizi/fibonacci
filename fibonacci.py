def print_fibonacci(finish):
    for count in range(0, finish):
        print fibonacci(count)


def fibonacci(finish):
    if finish == 0:
        return 0
    elif finish == 1:
        return 1
    else:
        return fibonacci(finish - 1) + fibonacci(finish - 2)
