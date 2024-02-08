def is_even(number):
    return number % 2==0

num=int(input())
if is_even(num):
    print(True)
else:
    print(False)