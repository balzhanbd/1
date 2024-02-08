def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Пример использования:
n = int(input())
result = fibonacci(n)
print(n, "равно", result)