
#pip install matplotlib 
#pip install numpy 
#install scipy module 
#pip install scipy
from mpl_toolkits.mplot3d import Axes3D
import random
import matplotlib.pyplot as plt  
import math
import numpy as np
import scipy
import scipy.stats
from scipy.stats import multivariate_normal
import scipy.stats as sts
import statistics as st



a = [] #for saving values generated by Box Muller Method 

mu = [5,8]
def gen_matrix_sigma(a):
    mat = [[1,2*a],[2*a,4]]
    return mat
    
def func_Box_Muller(num,d):
    ans = []
    while len(ans)<d*num:
        u1 = random.random()
        u2 = random.random()
        r = -2*(math.log(u1))
        v = 2*(math.pi)*u2
        z1 = (math.sqrt(r))*(math.cos(v))
        z2 = (math.sqrt(r))*(math.sin(v))
        ans.append(z1)
        ans.append(z2)
    global a
    a = ans

def find_A(sigma_mat):
    mat = [ [ 0 for i in range(2) ] for j in range(2)]
    sigma1 = math.sqrt(sigma_mat[0][0])
    sigma2 = math.sqrt(sigma_mat[1][1])
    rho = sigma_mat[1][0]/(sigma1*sigma2)
    mat[0][0] = sigma1
    mat[0][1] = 0
    mat[1][0] = rho*sigma2
    mat[1][1] = (math.sqrt(1-rho*rho))*sigma2
    return mat

def gen_Normal(mean,sigma_mat):
    matA = find_A(sigma_mat)
    ans_fin1 = []
    ans_fin2 = []
    cnt = 0
    while cnt < len(a):
        val1 = a[cnt]
        val2 = a[cnt+1]
        cnt+=2
        X1 = mean[0] + matA[0][0]*val1
        X2 = mean[1] + matA[1][0]*val1 + matA[1][1]*val2
        ans_fin1.append(X1)
        ans_fin2.append(X2)
    gn = [ans_fin1,ans_fin2]
    return gn

func_Box_Muller(1000,2)

def driver1(val_a):
    print('The value of a chosen is',val_a)
    gen = gen_Normal(mu,gen_matrix_sigma(val_a))
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    hist, xedges, yedges = np.histogram2d(gen[0], gen[1], bins=100, range=[[-20, 20], [-20, 20]])

    xpos, ypos = np.meshgrid(xedges[:-1] + 0.25, yedges[:-1] + 0.25, indexing="ij")
    xpos = xpos.ravel()
    ypos = ypos.ravel()
    zpos = 0
    dx = dy = 0.5 * np.ones_like(zpos)
    dz = hist.ravel()

    ax.bar3d(xpos, ypos, zpos, dx, dy, dz, zsort='average')
    ax.set_xlabel('X axis')
    ax.set_ylabel('Y axis')
    ax.set_zlabel('Z axis')
    print('The frequency plot obtained is as follows:')
    plt.show()

def driver2(val_a):
    sigma_mat = gen_matrix_sigma(val_a)
    gen = gen_Normal(mu,sigma_mat)
    print('The value of a chosen is',val_a)
    x = np.linspace(-20,20,500)
    y = np.linspace(-20,20,500)
    X, Y = np.meshgrid(x,y)
    pos = np.empty(X.shape + (2,))
    pos[:, :, 0] = X; pos[:, :, 1] = Y
    rv = multivariate_normal(mu,sigma_mat)
    
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.plot_surface(X, Y, rv.pdf(pos),cmap='viridis',linewidth=0)
    ax.set_xlabel('X axis')
    ax.set_ylabel('Y axis')
    ax.set_zlabel('Z axis')
    print('Density Plot (Using Formula) is as follows:')
    plt.show()
    fac = 1/((2*math.pi)*(math.sqrt(sigma_mat[0][0]*sigma_mat[1][1]-sigma_mat[1][0]*sigma_mat[0][1])))
    
    
    print('Simulated Density Plot using Generated Values:')
    
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    hist, xedges, yedges = np.histogram2d(gen[0], gen[1], bins=100, range=[[-20, 20], [-20, 20]])
    xpos, ypos = np.meshgrid(xedges[:-1] + 0.25, yedges[:-1] + 0.25, indexing="ij")
    xpos = xpos.ravel()
    ypos = ypos.ravel()
    zpos = 0
    dx = dy = 0.5 * np.ones_like(zpos)
    dz = (hist.ravel()/hist.max())*fac
    
    ax.bar3d(xpos, ypos, zpos, dx, dy, dz, zsort='average')
    ax.set_xlabel('X axis')
    ax.set_ylabel('Y axis')
    ax.set_zlabel('Z axis')
    plt.show()

def driver3(val_a):
    sigma_mat = gen_matrix_sigma(val_a)
    gen = gen_Normal(mu,sigma_mat)
    print('The value of a chosen is',val_a)
    print('Marginal Distribution (X) Simulated(Blue Histogram) vs Actual(Red Curve)')
    x = np.linspace(-20,20,100)
    plt.hist(gen[0],density=True,stacked=True,bins=50)
    plt.plot(x,sts.norm.pdf(x,mu[0],1),'r')
    plt.show()
    plt.close()
    print('Marginal Distribution (Y) Simulated(Blue Histogram) vs Actual(Red Curve)')
    plt.hist(gen[1],density=True,stacked=True,bins=50)
    plt.plot(x,sts.norm.pdf(x,mu[1],2),'r')
    plt.show()
    

# Q2, plots frequency histograms
driver1(1)
driver1(0)
driver1(0.5)
driver1(-0.5)

# Q3, plots denisty 2d histograms, 2d denisty plots(using formula)
# driver2(1)
driver2(0)
driver2(0.5)
driver2(-0.5)

# Q3, marginal density histograms, marginal density plots(using formula) 

driver3(1)
driver3(0)
driver3(0.5)
driver3(-0.5)