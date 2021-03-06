#install matplotlib,numpy
#install numpy
#pip install matplotlib 
#pip install numpy
#install times module to be sure
#pip install times 
import random
import matplotlib.pyplot as plt  
import math
import numpy as np
import time




a = [] #for saving values generated by Box Muller Method (10000 values)
b = [] #for saving values generated by Marsaglia and Bray Method (10000 values)
c = [] #for saving values generated by Box Muller Method (100 values)
d = [] #for saving values generated by Marsaglia and Bray Method (100 values)
t1 = 0 #time taken for generating 10000 values using Box Muller method
t2 = 0 #time taken for generating 10000 values using Marsaglia and Bray method
def func_Box_Muller(num):
    start_time = time.time()
    print('Method used:','Box Muller Method')
    ans = []
    while len(ans)<num:
        u1 = random.random()
        u2 = random.random()
        r = -2*(math.log(u1))
        v = 2*(math.pi)*u2
        z1 = (math.sqrt(r))*(math.cos(v))
        z2 = (math.sqrt(r))*(math.cos(v))
        ans.append(z1)
        ans.append(z2)
    global t1
    t1 = (time.time() - start_time)
    print('Sample Mean is',np.mean(ans))
    print('Sample Variance is',np.var(ans))
    print('The plot obtained is as ')
    if num==100:
        plt.xlabel('Values Generated')
        plt.ylabel('Frequency')
        plt.hist(ans,bins = 10)
        print('Number of bins (bars) is',10)
    else: 
        plt.xlabel('Values Generated')
        plt.ylabel('Frequency')
        plt.hist(ans,bins = 100)
        print('Number of bins (bars) is',100)
    plt.show()
    if num == 10000:
        global a
        a = ans
    else:
        global c
        c = ans
def func_Marsaglia_Bray(num):
    start_time = time.time()
    print('Method used:','Marsaglia and Bray Method')
    ans = []
    while len(ans)<num:
        x = 2
        while x>1:
            u1 = random.random()
            u2 = random.random()
            u1 = 2*u1 - 1
            u2 = 2*u2 - 1
            x = u1*u1 + u2*u2
        y = math.sqrt((-2*(math.log(x)))/x)
        z1 = u1*y
        z2 = u2*y
        ans.append(z1)
        ans.append(z2)
    global t2
    t2 = (time.time() - start_time)
    print('Sample Mean is',np.mean(ans))
    print('Sample Variance is',np.var(ans))
    print('The plot obtained is as ')
    if num==100:
        plt.xlabel('Values Generated')
        plt.ylabel('Frequency')
        plt.hist(ans,bins = 10)
        print('Number of bins (bars) is',10)
    else: 
        plt.xlabel('Values Generated')
        plt.ylabel('Frequency')
        plt.hist(ans,bins = 100)
        print('Number of bins (bars) is',100)
    plt.show()
    if num == 10000:
        global b
        b = ans
    else:
        global d
        d = ans
        
def genNormal(mean,var,arr1,arr2):
    
    print('')
    print('Normal distrivution with mean',mean,'and variance',var,'is to be generated')
    print('Method used:','Box-Muller Method')
    print('Number of values generated:',len(arr1))
    ans = []
    sigma = math.sqrt(var)
    for el in arr1:
        ans.append(mean+el*sigma)
    plt.hist(ans,density=True,bins = int(len(arr1)/math.sqrt(len(arr1))))
    plt.xlabel('X')
    plt.ylabel('f(x)')
    domain = np.linspace(-10,15,1000)
    yy = []
    for el in domain:
        pw = -0.5*((el-mean)/sigma)*((el-mean)/sigma)
        vl = (1/sigma)*(1/math.sqrt(2*math.pi))*(pow(math.e,pw))
        yy.append(vl)
    plt.plot(domain,yy,'r')
    plt.show()
    print('Method used:','Marsaglia and Bray Method')
    print('Number of values generated:',len(arr2))
    ans = []
    sigma = math.sqrt(var)
    for el in arr2:
        ans.append(mean+el*sigma)
    plt.xlabel('X')
    plt.ylabel('f(x)')
    domain = np.linspace(-10,15,1000)
    yy = []
    for el in domain:
        pw = -0.5*((el-mean)/sigma)*((el-mean)/sigma)
        vl = (1/sigma)*(1/math.sqrt(2*math.pi))*(pow(math.e,pw))
        yy.append(vl)
    plt.plot(domain,yy,'r')
    plt.hist(ans,density=True,bins = int(len(arr2)/math.sqrt(len(arr2))))
    plt.show()
    
def rej_prop(num):
    cnt = 0
    cn = 0
    while cn<num:
        x = 2
        while x>1:
            u1 = random.random()
            u2 = random.random()
            u1 = 2*u1 - 1
            u2 = 2*u2 - 1
            x = u1*u1 + u2*u2
            cnt+=2
        y = math.sqrt((-2*(math.log(x)))/x)
        z1 = u1*y
        z2 = u2*y
        cn+=2
    return ((cnt-num)/(cnt)) 
func_Box_Muller(100)
func_Box_Muller(10000)
func_Marsaglia_Bray(100)
func_Marsaglia_Bray(10000)
genNormal(0,5,a,b)
genNormal(0,5,c,d)
genNormal(5,5,a,b)
genNormal(5,5,c,d)

print('')
print('Time taken for Box Muller method for generating 10000 values',round(t1,6))
print('Time taken for Marsaglia and Bray for generating 10000 values',round(t2,6))

print('')
print('The proprtion of values rejected while using Marsaglia and Bray Method:')

print('When 10 values were generated:',rej_prop(10))
print('When 100 values were generated:',rej_prop(100))
print('When 1000 values were generated:',rej_prop(1000))
print('When 10000 values were generated:',rej_prop(10000))
print('When 100000 values were generated:',rej_prop(100000))
print('When 1000000 values were generated:',rej_prop(1000000))