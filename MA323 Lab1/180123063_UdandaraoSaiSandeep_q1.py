#matplotlib module is to be downloaded, refer to below command
#pip3 install matplotlib
vl = '|'
def func(a,b,m):
    print('\n')
    print(vl,'a',vl,'b',vl,'m ',vl,'x0',vl,' ',vl,'x1',vl,'x2',vl,'x3',vl,'x4',vl,'x5',vl,'x6',vl,'x7',vl,'x8',vl,'x9',vl,'x10|','Period Length',vl)
    print('\n')
    
    for x in range(0,m):
        if x<10:
            print(vl,a,vl,b,vl,m,vl,'',x,vl,'  ',end='|')
        else:
            print(vl,a,vl,b,vl,m,vl,x,vl,'  ',end='|')
        res =  [False for i in range(0,m)]
        l = -1
        val = x
        cnt = 0
        res[val] = True
        while cnt<m-1:
            val1=val
            val=(val1*a+b)%m
            if val<10: 
                print(' ',val,'',end='|')
            else:
                print('',val,'',end='|')
            cnt = cnt + 1
            if res[val]==True and l==-1:
                l = cnt
            res[val] = True
        if l<10 :
            print('     ',l,'      ',vl)
        else:
            print('     ',l,'     ',vl)
    print('\n')
func(6,0,11)
func(3,0,11)
