#ex1 
def squares_generator(N):
    for i in range (1, N+1):
        yield i*i
N = int(input())
squares = squares_generator(N)
for square in squares:
    print(square)
#ex2 
def even_numbers_generator(N):
    for i in range(2, N+1, 2):
        yield i
n=int(input())
even_numbers = even_numbers_generator(n)
print(','.join(map(str,even_numbers)))
#ex3
def divisible_by_3_and_4_generator(n):
    for i in range(n+1):
        if i % 3 ==0 and i%4==0:
            yield i
def print_divisible_by_3_and_4(n):
    generator = divisible_by_3_and_4_generator(n)
    for number in generator:
        print(number)
n=int(input())
print(n)
print_divisible_by_3_and_4(n)
#ex4
def squares(a,b):
    for i in range(a, b+1):
        yield i*i
a=int(input())
b=int(input())
for square in squares(a,b):
    print(square)
#ex5 
def countdown(n):
    while n >=0:
        yield n 
        n-=1
n=int(input())
for number in countdown(n):
    print(number)