#%%
import math

def function(x):
    return(math.sin(x)-math.log(x)+math.exp(x))


def trapezoidal(x_o,x_n,n):
    h = (x_n-x_o)/n
    print(h)
    sum = function(x_o)/2
    for i in range(1,n):
        y =function(x_o+i*h)
        sum = sum + y
        print(i,y)
    sum = sum + function(x_o + n*h)/2
    return(h*sum)

print(trapezoidal(0.2,1.4,6))
# %%

def simpson1_3(x_o,x_n,n):
    if (n%2!=0):
        raise Exception("Sorry, n is not even")

    h = (x_n-x_o)/n

    sum = function(x_o)
    for i in range(1,n):
        func_eval =function(x_o+i*h)
        if(i%2==0):
            sum = sum +2*func_eval
        else:
            sum =sum+ 4*func_eval
    sum = sum + function(x_o + n*h)
    return(h*sum/3)

def simpson3_8(x_o,x_n,n):
    if(n%3!=0):
        raise Exception("Sorry, n is not a multiple of 3")
    
    h = (x_n-x_o)/n
    sum = 0
    for i in range(int(n/3)):
        sum = sum + 3/8*h*(function(x_o+3*i*h)+3*(function(x_o+h*(3*i+1))+function(x_o+h*(3*i+2)))+function(x_o+h*(3*i+3)))
          
    return(sum)
# %%
print(f"Intergration of f(x):math.sin(x)-math.log(x)+math.exp(x) simpson1_3 rule is {simpson1_3(0.2,1.4,6)}")
print(f"Intergration of f(x):math.sin(x)-math.log(x)+math.exp(x) simpson3_8 rule is {simpson3_8(0.2,1.4,6)}")

#%%
import numpy as np


# %%

def weddle(x_o,x_n,n):
    
    if (n%6!=0):
        raise Exception("Sorry, n is not multiple of 6")
    
    coeff = [1,5,1,6,1,5,1]
    
    
    matrix = []
    h = (x_n-x_o)/n
    coeff1 = []
    coeff1 = coeff*int(n/6)
    for i in range(n+1):
        func_eval = function(x_o+i*h)
        matrix.append(func_eval)
        if(i!=0 and i!=n and i%6==0):
             matrix.append(func_eval)
        
    
    coeff1 = np.array(coeff1)
    matrix = np.array(matrix)
    return(3*h*np.dot(matrix,coeff1)/10)             






# %%

print(f"Intergration of f(x):math.sin(x)-math.log(x)+math.exp(x) simpson3_8 rule is {weddle(0.2,1.4,18)}")



# %%

# %%
