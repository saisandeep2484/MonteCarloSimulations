#matplotlib and numpy modules are to be downloaded, refer to below command
#pip3 install matplotlib
#pip install numpy
import random
import matplotlib.pyplot as graph 
import math

arr = []
def fill(a,b,m,x):
    val = x
    for i in range(0,17):
        arr.append(val/m)
        val = (a*val)%m

def gen(c,case):
    print('Case Number',case)
    print('Values Generated :',c)
    k = c
    lis = arr
    cnt = 17
    xx = []
    yy = []
    while c>0:
        temp = lis[cnt-17]-lis[cnt-5]
        if temp<0:
            temp = temp + 1
        lis.append(temp)
        cnt = cnt + 1
        c = c -1
    #print(k,'values:')
    #print(lis)
    for i in range(0,len(lis)-1):
        xx.append(lis[i])
        yy.append(lis[i+1])
    graph.scatter(xx,yy,s=5)
    graph.xlabel('X-axis')
    graph.ylabel('Y-axis')
    graph.title('Plot of (U i,U i+1)')
    print('Plot Scatter:')
    graph.show()
    print('Frequency Histogram:')
    graph.hist(lis, bins=10, rwidth=0.75)
    graph.show()
fill(6,0,17,1)
print('The first 17 values of the sequence:')
print(arr)
print('')
gen(1000,1)
gen(10000,2)
gen(100000,3)