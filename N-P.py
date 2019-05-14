from sympy import *
import numpy as np

x = Symbol('x')
#y = 6.9*x**0.64+2.152*x-100.283
y=-0.0536+(x+x**2+x**3+x**4)/(1-x)**3-7.59264*x**2-52.4*x**4.32388
yprime = y.diff(x)
print(prime)

#N-P from here
def derivative(f, x, h):
	return (f(x+h) - f(x-h))/(2*h)


def quadratic(x):
	#y = 6.9*x**0.64+2.152*x-100.283
	y=-0.0536+(x+x**2+x**3+x**4)/(1-x)**3-7.59264*x**2-52.4*x**4.32388
	return y

def solve(f, x0, h):
	lastX = x0
	nextX = lastX + 10*h
	while (abs(lastX - nextX) > h):
		newY = f(nextX)
		print("f(", nextX, ") = ", newY)
		lastX = nextX
		nextX = lastX - newY/derivative(f, lastX, h)
	return nextX

a = float(input("> "))
b = float(input("> "))
xFound = solve(quadratic, a, b)
print("Solution: x = ", xFound)