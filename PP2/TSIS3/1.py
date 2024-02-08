def calculation_factorial(n):
    if n == 0:
        return 1
    else:
        return n * calculation_factorial(n - 1)

# Пример использования:
number = int(input())
if number < 0:
    print("Error")
else:
    print(calculation_factorial(number))