#%%
 
def lagrange(x,y,n,k):
    sum = 0.0
    for i in range(n):
        product = y[i]
        for j in range(n):
            if(i!=j):
                product *= (k-x[j])/(x[i]-x[j])
        # print(product)
        sum = sum + product
    return(sum)

# %%
x = [5,7,11,13,17]
y = [150,392,1452,2366,5202]
k = 9

# %%
print(f'The value of function at {k} is {lagrange(x,y,5,k)}')
#%%
import numpy as np
# %%

# def NewDiv(x,y,n,x[i],yint,ea):
#     dd =np.zeros(shape=(n,n))
    
#     for i in range(n):
#         dd[i][0] = y[i]
    
#     for j in range(1,n):
#         for i in range(n-j):
#             dd[i][j] = dd[i+1][j-1]-dd[i][j-1]

