import numpy as np
import math
from scipy.misc import derivative
def f(x):
    return 9*x**4+8*x**3+1.5*x**2+2*x-10
a = -2
b = -1

eps = 0.001 

def nuton(a,b,eps):
    df2 = derivative(f, b, n = 2)
    if (f(b)*df2>0):
        xi = b
    else:
        xi = a
    df = derivative(f,xi, n = 1)
    xi_1 = xi - f(xi)/df
    while (abs(xi_1 - xi)>eps): #accuracy check
        xi = xi_1
        xi_1 = xi - f(xi)/df
    return print ("Solving the equation by Newton's method x = ", xi_1)
nuton (a,b,eps)


input()
