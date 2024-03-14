import math
#ex 1
m = float(input())
rad = math.radians(m)
print(rad)

#ex2
h=int(input())
a=int(input())
b=int(input())
S=((a+b)*h)/2
print(S)

#ex3
n=int(input())
l=int(input())
AreaOfRegularPolygon = (n*l**2)/4*math.tan(math.pi/n)
print(round(AreaOfRegularPolygon))

#ex4
length = int(input())
heigth = int(input())
AreaOfParallelogram = length * heigth
print(float(AreaOfParallelogram))

