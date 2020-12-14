#matplotlib module is to be downloaded, refer to below command
#pip3 install matplotlib
import random
import matplotlib.pyplot as histo 
import math

def func(a,b,m,x):
    res = [False for i in range(0,m)]
    val = x
    res[val] = True
    arr = []
    freq = [0]*20
    while True:
        arr.append((float)(val/m))
        val1 = val
        val = (val1*a+b)%m
        freq[math.floor((val/m)*20)]+=1
        if(res[val]==True): 
            break
        else:
            res[val]=True
    histo.hist(arr, bins=20, rwidth=0.75)
    histo.show()
    cnt = 0
    print('')
    print('Interval','   ','Count')
    for i in freq:
        print(cnt/20,'-',(cnt+1)/20,' ',i)
        cnt = cnt + 1
    print('')
cnt = 0
m = 244944
while cnt<5:
    x = random.randint(0,m)
    print('Çase :',cnt+1)
    print('The value of x0 chosen is : ' + str(x))
    
    a,b= 1597,51749
    print('The value of a is : ' + str(a))
    func(a,b,m,x)
    a,b= 51749,1597
    print('The value of a is : ' + str(a))
    func(a,b,m,x)
    cnt = cnt + 1
