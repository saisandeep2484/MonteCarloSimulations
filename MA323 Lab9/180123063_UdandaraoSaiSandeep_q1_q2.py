#pip install numpy
import math
import random
import numpy as np

def func_Box_Muller(num):
    ans = []
    while len(ans)<num:
        u1 = random.random()
        u2 = random.random()
        r = -2*(math.log(u1))
        v = 2*(math.pi)*u2
        z1 = (math.sqrt(r))*(math.cos(v))
        z2 = (math.sqrt(r))*(math.sin(v))
        ans.append(z1)
        ans.append(z2)
    return ans

    
def gen():
    n = 300 # number of time intervals
    S = [0]*(n+2) # initializing the stock price array
    S[0]= 185.40 # price as of 30th semptember 2020
    K = (1.1)*S[0] # Strike Price
    # Time interval is 0.1 (30 days, 300 time points)
    
    mu = 0.0002981060700200034 # using values from assignment 7
    var = 0.000496475360718651 # using values from assignment 7
    
    Z = func_Box_Muller(n+1)
    summ = 0 # for storing sum of prices
    for i in range(1,n+2):
        temp = (mu - 0.5*var)*(0.1)
        temp += math.sqrt(var * 0.1) * Z[i-1]
        S[i] = S[i-1]*math.exp(temp)
        summ += S[i]
    
    Payoff = max(K - (summ/(n+1)), 0)
    European_Payoff = max(K - S[n],0)
    return [Payoff,European_Payoff]


M = 1000 # number of simulations

Y = [] # to store the Asian Put option generated PayOffs
X = [] # to store the corresponding European Put option Payoffs

# process is repeated M times
for i in range(0,M):
    xx = gen()
    Y.append(xx[0]);
    X.append(xx[1]);
        

mu_y = np.mean(Y) 
var_y = np.var(Y)
sig_y = math.sqrt(var_y)

mu_x = np.mean(X) 
var_x = np.var(X)
sig_x = math.sqrt(var_x)
print("------------------------------------------------------------------------")

print('Mean of Generated Payoffs =',mu_y)
print('Variance of Generated Payoffs =',var_y)
print('Standard Variation of Generated Payoffs =',sig_y)



confidence_interval = [0]*2;
confidence_interval[0] = mu_y - (1.96*sig_y)/(math.sqrt(M))
confidence_interval[1] = mu_y + (1.96*sig_y)/(math.sqrt(M))

print('Confidence Interval is',confidence_interval)

summ1 = 0
summ2 = 0
for i in range(0,len(X)):
    summ1 += (X[i] - mu_x)*(Y[i] - mu_y)
    summ2 += (X[i] - mu_x)*(X[i] - mu_x)
    
b = summ1/summ2 # finding an estimate for b



Controlled_Y = []
for i in range(0,len(X)):
    Controlled_Y.append(Y[i]-b*(X[i]-mu_x)) # finding the Control Variable
    


mu_y2 = np.mean(Controlled_Y) 
var_y2 = np.var(Controlled_Y)
sig_y2 = math.sqrt(var_y2)

confidence_interval2 = [0]*2;

confidence_interval2[0] = mu_y2 - (1.96*sig_y2)/(math.sqrt(M))
confidence_interval2[1] = mu_y2 + (1.96*sig_y2)/(math.sqrt(M))

print("------------------------------------------------------------------------")
print("Estimated Value of b is",b)
print('Mean of the Controlled Variable', mu_y2,"(Remains the same)") 
print('Variance of the Controlled Variable ',var_y2, "(Is Lesser than original)")
print('Confidence Interval is',confidence_interval2)
print("------------------------------------------------------------------------")
    