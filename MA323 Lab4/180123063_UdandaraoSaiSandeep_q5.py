#install matplotlib,numpy
#install numpy
#pip install matplotlib 
#pip install numpy
import random
import matplotlib.pyplot as plt  
import math
import numpy as np

def func(a1,a2,num):
    print('The Value of aplha1 is',a1)
    print('The Value of aplha2 is',a2)
    x = (a1-1)/(a1+a2-2)
    print('The Value of x* calculated is',x)
    B = (math.gamma(a1)*math.gamma(a2))/math.gamma(a1+a2)
    fx = (pow(x,a1-1)*(pow(1-x,a2-1)))/B
    print('The maximum value of f(x) is = f(x*) = c =',fx)
    c = fx
    print('The number of values generted is',num)
    fin = []
    cnt = 0
    while cnt<num:
        while 1:
            u1 = random.random()
            u2 = random.random()
            fu1 = (pow(u1,a1-1)*(pow(1-u1,a2-1)))/B
            if(c*u2<=fu1):
                fin.append(u1)
                break
            
        cnt+=1
    plt.hist(fin,density=True,bins = 100)
    print('The density graph generated from the sample data generated is as follows(blue):')
    print('The red curve represents the actual pdf obtained from the formula.')
    #plt.show()
    xx = np.linspace(0,1,100)
    yy = []
    for var in xx:
        fvar = (pow(var,a1-1)*(pow(1-var,a2-1)))/B
        yy.append(fvar)
    plt.plot(xx,yy,'r')
    plt.xlabel('x')
    plt.ylabel('Function Value')
    plt.show()
    print('')
func(5,5,80000)
func(2,3,80000)
func(3,5,80000)
func(4,1,80000)
func(1,6,80000)