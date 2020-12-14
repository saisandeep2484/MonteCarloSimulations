#pip install matplotlib
#matplotlib module has been used to generate the graphs
import math
import matplotlib.pyplot as plt  
import numpy as np


def lcg(a,b,m,x0,num):
    arr = []
    val = x0
    for i in range(0,num):
        arr.append(val/m)
        val = (a*val+b)%m
    return arr


def calc(st):
    var = 0
    st = st[::-1]
    bb = 0.5
    for i in range(0,len(st)):
        if st[i] =='1':
            var+=bb
        bb=bb/2
        
    return var
        
def gen_vander_corupt_seq(n):
    phi_2 = []
    phi_2.append(0);
    for i in range(1,n+1):
        binary = bin(i).replace("0b", "")
        num = calc(binary)
        phi_2.append(num)
    return phi_2
        
arr1 = gen_vander_corupt_seq(25)
print("The first 25 values of the Van der Corput sequence are:")
print('\n'.join('x{} : {}'.format(*k) for k in enumerate(arr1)))

arr2 = gen_vander_corupt_seq(1000)

xx = []
yy = []
for i in range(1,len(arr2)):
    xx.append(arr2[i-1])
    yy.append(arr2[i])
    
plt.scatter(xx,yy,s=1)
print("")
print("Plot of (x[i],x[i+1]) for first 1000 values of the Van der Corput sequence")
plt.xlabel("x")
plt.ylabel("PDF : f(x)")
plt.show()

arr3 = gen_vander_corupt_seq(100)
arr4 = gen_vander_corupt_seq(100000)

arr5 = lcg(1597,51749,244944,1,100)
arr6 = lcg(1597,51749,244944,1,100000)

print("")
print("Details for LCG : Linear Congruent Generator")
print("a = 1597 , b = 51749 , m = 244944 , x0 = 1")
print("")
print("The value of n is :",100)
print("Denisty Plot for Van der Corput sequence")
plt.hist(arr3,bins=20,density='true')
plt.xlabel("x")
plt.ylabel("PDF : f(x)")
plt.show()
print("Denisty Plot for LCG sequence")
plt.hist(arr5,bins=20,density='true',color = 'orange')
plt.xlabel("x")
plt.ylabel("PDF : f(x)")
plt.show()

print("The value of n is :",100000)
print("Denisty Plot for Van der Corput sequence")
plt.hist(arr4,bins=100,density='true')
plt.xlabel("x")
plt.ylabel("PDF : f(x)")
plt.show()
print("Denisty Plot for LCG sequence")
plt.hist(arr6,bins=100,density='true',color = 'orange')
plt.xlabel("x")
plt.ylabel("PDF : f(x)")
plt.show()
