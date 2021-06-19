#!/usr/bin/env python
# coding: utf-8

# # Bisection Method

# DEFINATION OF FUNCTION:

# In[1]:


import math
def function(x):
    return(x**3+3*x**2-5*x-3)
  


# In[2]:


while(True):
    lg = int(input("Enter the lower guess "))
    ug = int(input("Enter the upper guess "))
    if((function(lg)*function(ug))<0):
        # print(function(lg)*function(ug))
        break
    print("Try guessing again !")
        
        


# EXPECTED ERROR:

# In[3]:


Ed = float(input("Enter the error expected "))
n  = math.log((ug-lg)/Ed,2)
n  = int(math.ceil(n)) 


# In[4]:


for i in range(n):
    xr = (ug+lg)/2
    print(xr)
    if(function(lg)*function(xr)<0):
        ug=xr
    elif(function(lg)*function(xr)>0):
        lg=xr
    else:
        print(f"The root is {xr}")
        break
print(f"The root is {xr}")


# # Secant Method

# In[6]:


h=0.01
x = float(input("Enter initial guess "))
i = 0
print(f'Iteration\t x[i]\t error')
print(f'{i}\t {x}\t 100')
while True:
    f_dash = (function(x+h)-function(x))/h
    x_new = x - function(x)/f_dash
    error = abs((x_new-x))/x_new*100
    i+=1
    print(f'{i}\t {x_new}\t {error}')
    if (error<0.01):
        break
    x = x_new
#     i+=1
#     if i == 10:
#         break
print(x_new)







