#matplotlib module is to be downloaded, refer to below command
#pip3 install matplotlib
import matplotlib.pyplot as graph 

def func(a,b,m):
    xx = []
    yy = []
    res =  [False for i in range(0,m)]
    x0 = 50 
    #choosing suitable value for x0
    res[x0] = True
    val = x0
    while True:
        val1=val
        val=(val1*a+b)%m
        if res[val] == True:
            break
        else:
            res[val] = True
        xx.append((float)(val1/m))
        yy.append((float)(val/m))
    graph.scatter(xx,yy,s=5)
    graph.xlabel('X-axis')
    graph.ylabel('Y-axis')
    graph.title('Plot')
    graph.show()
    
a,b,m=1229,1,2048
func(a,b,m)