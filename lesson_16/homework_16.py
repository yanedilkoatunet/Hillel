from functools import wraps

# 1 Generator that returns even numbers from 0 to N
def even_numbers(n):
    for number in range(0, n + 1, 2):
        yield number


# 2 Generator that returns Fibonacci numbers up to N
def fibonacci(n):
    first, second = 0, 1

    while first <= n:
        yield first
        first, second = second, first + second


# 3 Iterator that returns list elements in reverse order
class ReverseIterator:
    def __init__(self, items):
        self.items = items
        self.index = len(items) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < 0:
            raise StopIteration

        item = self.items[self.index]
        self.index -= 1
        return item


# 4 Iterator that returns even numbers from 0 to N
class EvenNumbersIterator:
    def __init__(self, n):
        self.n = n
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.n:
            raise StopIteration

        number = self.current
        self.current += 2
        return number


# 5 Decorator that logs function arguments and result
def log_function(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        print(f"Arguments: args={args}, kwargs={kwargs}")

        result = func(*args, **kwargs)

        print(f"Result: {result}")
        return result

    return wrapper


# 6 Decorator that catches and handles exceptions
def handle_exceptions(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as error:
            print(f"Error in {func.__name__}: {error}")
            return None

    return wrapper


# Examples to test the solutions
@log_function
def add(a, b):
    return a + b


@handle_exceptions
def divide(a, b):
    return a / b


if __name__ == "__main__":
    print("1. Even numbers:", list(even_numbers(10)))
    print("2. Fibonacci numbers:", list(fibonacci(20)))

    print("3. Reverse iterator:", list(ReverseIterator([1, 2, 3, 4])))

    print("4. Even numbers iterator:", list(EvenNumbersIterator(10)))

    print("5. Logging decorator:")
    add(3, 5)

    print("6. Exception handling decorator:")
    print("Division result:", divide(10, 2))
    print("Division by zero:", divide(10, 0))
