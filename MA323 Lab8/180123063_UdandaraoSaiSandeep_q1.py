#pip install numpy
#pip install matplotlib
import math
import random
import numpy as np
import matplotlib.pyplot as plt

def func_Box_Muller(num):
    # this function generates values from the normal distribution
    # num represents the number of values generated
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
    return ans

def func(lamda):
    print("Lambda =",lamda)
    Z = func_Box_Muller(1000) # generating 1000 values from Standard Normal Distribution   
    # time points vary from 1 to 2000, each interval of length 2 (1000 points total)
    X = [0]*1001
    S_init = 185.40 # denotes the value of S[0] = Stock Price on 30th September
    X[0] = math.log(S_init)
    
    mu = 0.0002981060700200034 # using values from previous assignment
    var = 0.000496475360718651 # using values from previous assignment
    
    for i in range(0,1000):
        # time interval is 2
        N = np.random.poisson(lam=lamda*2, size=None) # generating N from Poisson Distribution with 
        M = 0
        if N == 0 :
            M = 0
        else :
            Y = np.random.lognormal(mu,math.sqrt(var),int(N)) # generating N values from the lognormal distribution
            for j in range(0,N):
                M+=math.log(Y[j])
                
                
        X[i+1] = X[i] + (mu-0.5*var)*(2) + math.sqrt(var)*math.sqrt(2)*Z[i] + M  #Simulating Formula
    
    S = []
    for i in range(0,len(X)):
        S.append(math.exp(X[i]))   # Getting S(t) from X(t)
        
    xx = np.linspace(0,2000,1001)
    plt.plot(xx,S)
    title = "Stimulated Stock Prices for lamda = " + str(lamda)
    plt.title(title)
    plt.xlabel("Time Points")
    plt.ylabel("Stock Prices")
    plt.show()
    
func(0.01)
func(0.05)
func(0.1)
func(0.2)