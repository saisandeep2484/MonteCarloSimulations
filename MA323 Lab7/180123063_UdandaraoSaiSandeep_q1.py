import math
import random

def func_Box_Muller(num):
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

cps = [184.800003, 185.449997, 184.699997, 188.050003, 188.600006, 191.899994, 199.100006, 195.600006, 192.699997, 186.050003, 183.800003, 186.25, 188.199997, 190.75, 194.399994, 192.0, 198.25, 191.949997, 187.149994, 189.449997, 191.199997, 186.550003, 191.449997, 192.25, 191.600006, 191.449997, 190.949997, 190.649994, 193.800003, 195.050003, 203.300003, 201.899994, 196.5, 193.100006, 195.100006, 197.050003, 194.75, 198.399994, 201.449997, 207.949997, 209.850006, 215.649994, 224.850006, 212.0, 218.100006, 216.25, 213.149994, 206.600006, 207.899994, 204.050003, 194.850006, 198.149994, 202.699997, 198.5, 200.149994, 198.199997, 195.449997, 192.600006, 185.800003, 186.199997, 183.800003, 176.350006, 182.199997, 187.25, 185.050003, 185.399994]
#cps(closing stock prices) represents the clsoing price of the stock from 1 July 2020 to 30 Sept 2020

n = len(cps)
u = []
for i in range(1,n):
    u.append(math.log(cps[i]/cps[i-1]))

n = len(u)

Eu = 0 #to store E(u)

for i in range(0,len(u)):
    Eu += u[i]
    
Eu = Eu/(n)

sigma = 0 #to store estimated value of Standard Variation

for i in range(0,len(u)):
    sigma += (u[i]-Eu)*(u[i]-Eu)

sigma = sigma/(n-1)
sigma = math.sqrt(sigma)

mu = 0 #to store estimated value of mean
mu = Eu + (sigma*sigma)/2

print("E(u) = ",Eu)
print("Estimated value of mean is : ",mu)
print("Estimated value of variance is : ",sigma*sigma)



def gen(val,diff,actual,Z):
    #Take 30th September to be the starting date, val corresponds to the stock price on Sep 30, 2020
    # diff denotes the value of time interval between starting date and the required date
    Exp_val = 0
    for i in range(0,len(Z)):
        tem = val*math.exp((mu-0.5*sigma*sigma)*diff + sigma*(math.sqrt(diff))*Z[i])
        Exp_val+=tem
    
    Exp_val = Exp_val/len(Z)
    print("")
    if diff == 4:
        print("Estimated Value of stock price on 7 October 2020 is",Exp_val)
        print("Actual Value of stock price on 7 October 2020 is",actual)
    if diff == 10:
        print("Estimated Value of stock price on 14 October 2020 is",Exp_val)
        print("Actual Value of stock price on 14 October 2020 is",actual)
    if diff == 15:
        print("Estimated Value of stock price on 21 October 2020 is",Exp_val)
        print("Actual Value of stock price on 21 October 2020 is",actual)
    print("The Percentage error is :", (abs(actual-Exp_val)/actual)*100,"%")
        

    
Z = func_Box_Muller(1000)
gen(185.40,4,190.70,Z)
Z = func_Box_Muller(1000)
gen(185.40,10,200.05,Z)
Z = func_Box_Muller(1000)
gen(185.40,15,203.75,Z)