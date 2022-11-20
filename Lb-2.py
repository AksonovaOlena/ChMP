import numpy as np
import math
import matplotlib.pyplot as plt
def f(x):
    return 9*x**4+8*x**3+1.5*x**2+2*x-10
a=-2.
b=-1.
eps=0.001
def rec_dyhotomy(a,b,eps):
    if abs(f(b)-f(a))<eps:
        print('Кореня немає')
        return
mid=(a+b)/2
if(mid)==0 or abs(f(mid))<eps:
    print(f'Корінь знаходиться в точці х = {mid}')
elif f(a)*f(mid)<0:
    rec_dyhotomy(a,mid,eps)
else:
    rec_dyhotomy(mid,b,eps)
rec_dyhotomy(a,b,eps)
x=np.arange(1.,2.,0.01)
plt.plot(x,f(x))
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Метод ділення навпіл')
plt.grid()
plt.show()
    



#input()
