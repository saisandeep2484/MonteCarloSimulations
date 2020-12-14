#pip install matplotlib
#matplotlib module has been used to generate the graphs
import math
import matplotlib.pyplot as plt  
import numpy as np

def calc2(st):
    var = 0
    st = st[::-1]
    bb = 0.5
    for i in range(0,len(st)):
        if st[i] =='1': 
            var+=bb
        bb=bb/2
        
    return var

def calc3(st):
    var = 0
    st = st[::-1]
    bb = 1/3
    for i in range(0,len(st)):
        if st[i] =='1': 
            var+=bb
        elif st[i] =='2':
            var+=2*bb
        bb=bb/3
        
    return var
        
def gen_vander_corupt_seq_2(n):
    phi_2 = []
    phi_2.append(0);
    for i in range(1,n+1):
        binary = bin(i).replace("0b", "")
        num = calc2(binary)
        phi_2.append(num)
    return phi_2

def gen_vander_corupt_seq_3(n):
    phi_3 = []
    phi_3.append(0);
    for i in range(1,n+1):
        ternary = np.base_repr(i,base=3)
        num = calc3(ternary)
        phi_3.append(num)
    return phi_3
      
print("2-D plot for the Halton Sequence (100 numbers)")
xx = gen_vander_corupt_seq_2(100)
yy = gen_vander_corupt_seq_3(100)

plt.scatter(xx,yy)
plt.xlabel("φ2(i)")
plt.ylabel("φ3(i)")
plt.show()

print("2-D plot for the Halton Sequence (100000 numbers)")
xx = gen_vander_corupt_seq_2(100000)
yy = gen_vander_corupt_seq_3(100000)

plt.scatter(xx,yy)
plt.xlabel("φ2(i)")
plt.ylabel("φ3(i)")
plt.show()
