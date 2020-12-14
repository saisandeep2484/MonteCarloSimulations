import math

def fill(a,b,m,x0,num):
    #LCG that generates first num values of the LCG sequence
    arr = []
    val = x0
    for i in range(0,num):
        arr.append(val/m)
        val = (a*val+b)%m
    return arr
        
def func(N):
    #N represents the number of intervals
    n = 10000 # giving some large fixed value for n 
    x = fill(1597,51749,244944,1,n) 
    sup = 0 # to store discrepancy
    for i in range(0,n):
        int_st = i/N #starting point of ith interval
        int_en = ((i+1)/N) #ending point of ith interval
        cnt = 0
        for j in range(0,n):
            if x[j]>=int_st and x[j]<int_en:
                cnt+=1
        vol = 1/N # measure of a closed interval is equal to its length  
        sup = max(sup,abs(cnt/n - vol)) 
    
    print("The supremum obtained for N =",N,"is :",sup)
    return sup

ans10 = func(10) 
ans20 = func(20)
ans50 = func(50)
ans100 = func(100)
print("")
print("Table :")
print("")
print("N                     Discrepancy")
print("")
print(10,"                     ",ans10)
print(20,"                     ",ans20)
print(50,"                     ",ans50)
print(100,"                    ",ans100)
