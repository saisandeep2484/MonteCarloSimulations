#install matplotlib 
#pip install matplotlib
import matplotlib.pyplot as plt
import random      
arr = []
def fill(a,b,m,x,num):
    arr.clear()
    val = x
    for i in range(0,num):
        arr.append(val/m)
        val = (a*val+b)%m

def calc(no):
	c = []
	for i in range(1,10000):
		if i%2==1:
		    c.append(i)
	q = []
	q.append(0)
	cnt = 1
	for i in range(0,5000):
		q.append(cnt/5000)
		cnt+=1
	fill(1597,51749,244944,1,no)
	ans = []
	for var in arr:
		for i in range (1,len(q)):
			if q[i-1]< var and var<=q[i]:
				ans.append(c[i-1])
				break
	print('The Number of Values Generated is :',no)
	if no==10 or no==100: 
		print('LCG       ','X')		
	for xx,yy in zip(arr,ans):
		if no==10 or no==100: 
			print("{:.7f}".format(xx),'',yy)
	print('')
	if no == 10000 or no == 100000:
		plt.hist(ans,bins = 30)
		plt.show()

calc(10)
calc(100)
calc(10000)