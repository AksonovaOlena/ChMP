import numpy as np
import math
from scipy.misc import derivative
def f(x):
    return 9*pow(x,4)+8*pow(x,3)+1.5*pow(x,2)+ 2*x-10
a=0.
b=1.
eps=0.001 #точність
def hord (a,b,eps):
    if (f(a)*derivative(f,a,n=2)>0):
        x0=a
        xi=b
    else:
        x0=b
        xi=a
    xi_1=xi-(xi-x0)*f(xi)/(f(xi)-f(x0))
    while (abs(xi_1-xi)>eps):
        xi=xi_1
        xi_1=xi-(xi-x0)*f(xi)/(f(xi)-f(x0))     
    print(f'Метод хорд.Корінь знаходиться в точці x = ', round(xi_1,5))
hord(a,b,eps)

    



input()
