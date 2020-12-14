#install matplotlib 
#pip install matplotlib
import random  
def func(arg):
    switcher = {
        1: 0.11,
        2: 0.12,
        3: 0.09,
        4: 0.08,
        5: 0.12,
        6: 0.10,
        7: 0.09,
        8: 0.09,
        9: 0.10,
        10: 0.10,
    }
    return switcher.get(arg)

def DisGen(var):
    c = []
    for i in range(0,10):
        c.append(i+1)
    q = []
    q.append(0)
    cnt = 1
    for i in range(0,10):
        q.append(cnt/10)
        cnt+=1
    for i in range (1,len(q)):
        if q[i-1]< var and var<=q[i]:
            return c[i-1]
            break
def calc(no,c):
    summ = 0
    freq = [0]*11
    for i in range(0,no):
        cnt = 0
        while True:
            U = random.random()
            X = DisGen(random.random())
            fX = func(X)
            gX = 0.1
            cnt += 1
            if U <= fX/(c*gX):
                summ+=cnt
                print(X,end = ' ')
                freq[X]+=1
                break
    print('The Frequency Table is as follows:')
    print('Value','Count')
    for i in range(1,11):
        print(' ',i,'   ',freq[i])
    print('Áverage iterations taken',summ/no)
    print('')
it = 10
print('The value of c chosen is:',2)
while it<10000:
    print('The number of values taken is',it)
    calc(it,2)
    it = it*10
print('')
it = 10
print('The value of c chosen is:',3)
while it<10000:
    print('The number of values taken is',it)
    calc(it,3)
    it = it*10