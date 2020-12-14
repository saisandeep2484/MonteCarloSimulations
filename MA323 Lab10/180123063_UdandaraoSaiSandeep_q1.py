import random
import math
import statistics 

def func1(m):
    print("The value of m chosen is :",m)
    Y = []
    U = []
    
    for i in range(0,m):
        Ui = random.random();
        U.append(Ui);
    
    for i in range(0,m):
        Yi = math.exp(math.sqrt(U[i]))
        Y.append(Yi)
    
    
    print("Expectation Obtained(Im) :",statistics.mean(Y))
    
    
def func2(m):
    print("")
    print("The value of m chosen is :",m)
    print("")
    Y = []
    U = []
    Y_hat = []
    for i in range(0,m):
        Ui = random.random();
        U.append(Ui);
    
    for i in range(0,m):
        Yi = math.exp(math.sqrt(U[i]))
        Yi_hat = (math.exp(math.sqrt(U[i])) + math.exp(math.sqrt(1-U[i])))/2
        Y.append(Yi)
        Y_hat.append(Yi_hat)
    
    
    print("Expectation Obtained(Im) :",statistics.mean(Y))
    print("Variance Obtained(Im) :",statistics.variance(Y))
    print("95% Confidence Interval for Im",[statistics.mean(Y)-math.sqrt(statistics.variance(Y)/m),statistics.mean(Y)+math.sqrt(statistics.variance(Y)/m)])
    print("")
    print("Expectation Obtained(Im_hat) :",statistics.mean(Y_hat))
    print("Variance Obtained(Im_hat) :",statistics.variance(Y_hat))
    print("95% Confidence Interval for Im_hat",[statistics.mean(Y_hat)-math.sqrt(statistics.variance(Y_hat)/m),statistics.mean(Y_hat)+math.sqrt(statistics.variance(Y_hat)/m)])
    
    print("Ratio of Lengths of Confidence Interval (Im/Im_hat) =", math.sqrt(statistics.variance(Y)/statistics.variance(Y_hat)))    
print("CASE-1")
print("")
func1(100);
func1(1000);
func1(10000);
func1(100000);

print("")

print("CASE-2")
print("")
func2(100);
func2(1000);
func2(10000);
func2(100000);