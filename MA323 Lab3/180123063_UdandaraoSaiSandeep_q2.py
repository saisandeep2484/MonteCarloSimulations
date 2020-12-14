#install matplotlib 
#pip install matplotlib 
import random
import matplotlib.pyplot as plt  
def calc(no,c):
    summ = 0
    ans = []
    if c == 2.109375 and no == 10:
        print('X generated',' ','Iterations Reqd.')
    for i in range(0,no):
        cnt = 0
        while True:
            U = random.random()
            X = random.random()
            fX = 20*X*(1-X)*(1-X)*(1-X)
            gX = 1
            cnt += 1
            if U <= fX/(c*gX):
                ans.append(X)
                if c == 2.109375 and no == 10:
                    print("%0.7f"%(X),'         ',cnt)
                summ+=cnt
                break
    print('The Averge Value obtained for Nummber of iterations is',summ/no)
    print('')
    (y,x,pat) = plt.hist(ans,density=True,bins = 20)
    err = 0.0
    for i in range(0,len(y)):
        err += ((20*x[i]*(1-x[i])*(1-x[i])*(1-x[i])) - y[i])*((20*x[i]*(1-x[i])*(1-x[i])*(1-x[i])) - y[i])
    #plt.show()
    err = err/(len(y))
    print('The error value is', err)
        
it = 10
print('The value of c chosen is:',2.109375)
while it<1000000:
    print('The number of values taken is',it)
    calc(it,2.109375)
    it = it*10
it = 10
print('The value of c chosen is:',5)
while it<1000000:
    print('The number of values taken is',it)
    calc(it,5)
    it = it*10
it = 10
print('The value of c chosen is:',10)
while it<1000000:
    print('The number of values taken is',it)
    calc(it,10)
    it = it*10
plt.close()