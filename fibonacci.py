fibonacci_cache = {}
factorial_cache = {}


def fibonacci(n: int) -> int:
    if n in fibonacci_cache:
        return fibonacci_cache[n]
    if n <= 0:
        result = 0
    elif n == 1:
        result = 1
    else:
        result = fibonacci(n - 1) + fibonacci(n - 2)
    fibonacci_cache[n] = result
    return result


def factorial(n: int) -> int:
    if n in factorial_cache:
        return factorial_cache[n]
    if n < 0:
        raise ValueError("Please use positive numbers only")
    elif n == 0 or n == 1:
        result = 1
    else:
        result = n * factorial(n - 1)
    factorial_cache[n] = result
    return result


print(f"Fibonacci of 17: {fibonacci(17)}")
print(f"Factorial of 5: {factorial(5)}")

fibonacci_cache.clear()
factorial_cache.clear()
