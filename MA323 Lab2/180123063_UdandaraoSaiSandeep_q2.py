#matplotlib and numpy modules are to be downloaded, refer to below command
#pip3 install matplotlib
#pip install numpy
import random
import matplotlib.pyplot as graph 
import math
import numpy as np


arr = []
def fill(a,b,m,x,num):
    arr.clear()
    val = x
    for i in range(0,num):
        arr.append(val/m)
        val = (a*val+b)%m

def gen(num,case):
    print('Case Number ',case)
    print('Number of Values Generated',num)
    fill(65793,4282663,8388608,1,num)
    theta = 1
    s = 0
    freq = {}
    cn = 0
    for v in arr:
        arr[cn] = (-theta)*(math.log(1-v))
        s += arr[cn] 
        cn+=1
    mean = s/num
    maxx = -1.0
    s = 0
    for item in arr: 
        s += (item-mean)*(item-mean) 
        if (item in freq): 
            freq[item] += 1
        else: 
            freq[item] = 1
        maxx = max(maxx,item)
    variance = s/num
    xx = []
    yy = []
    freqq = [0]*20
    for key, value in freq.items():
        freqq[math.floor((key/(maxx+0.001))*20)]+=value
    cnt = 0
    for i in freqq:
        xx.append((cnt/20 + (cnt+1)/20)/2)
        yy.append(i)
        cnt+=1
    graph.scatter(xx,yy,s=10)
    graph.plot(xx,yy)
    graph.xlabel('X-axis (Interval)')
    graph.ylabel('Y-axis (Count)')
    graph.title('Interval vs Frequency Graph')
    graph.show()
    xx.clear()
    yy.clear()
    cnt = 0
    st = 0
    for i in freqq:
        st = st + i
        xx.append((cnt/20 + (cnt+1)/20)/2)
        yy.append(st)
        cnt+=1
    graph.scatter(xx,yy,s=10)
    graph.plot(xx,yy)
    graph.xlabel('X-axis (Interval)')
    graph.ylabel('Y-axis (Count)')
    graph.title('Interval vs Cumulative Frequency Graph')
    graph.show()
    print('Sample Mean is',mean)
    print('Sample Variance is',variance)
    print('')
    

print('Values chosen for Linear Congruence Generator(for generating values of U)')
print('a = 65793','b = 4282663','m = 8388608')
print('Value of Theta Taken is:',1)
print(' ')
gen(20,1)
gen(50,2)
gen(100,3)
gen(200,4)
gen(500,5)
gen(1000,6)
gen(10000,7)
gen(100000,8)

print('Actual Distribution Function F(x)')
x1 = np.linspace(0,20,100)
y1 = []
for var in x1:
    y1.append(1 - math.exp(-var/1))
graph.plot(x1,y1,'r')
graph.xlabel('X-axis')
graph.ylabel('F(x)')
graph.title('Cumulative Distribution Function')
graph.show()
print('Actual Value of Mean:',1)
# mean = theta
print('Actual Value of Variance:',1)
# variance = theta*theta