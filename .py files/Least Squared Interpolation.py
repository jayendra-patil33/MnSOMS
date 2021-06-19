#%%

# from operator import index
import numpy as np
import copy
import matplotlib.pyplot as plt


#%%

def find_solution(matrix,B,n):
    for k in range(n-1):
        for i in range(k+1,n):
                if matrix[i,k] != 0.0:
                    const = matrix[i,k]/matrix[k,k]
                    matrix[i,k+1:n] -= const*matrix[k,k+1:n]
                    B[i] -= const*B[k]
    for k in range(n-1,-1,-1):
        B[k] = (B[k] - np.dot(matrix[k,k+1:n], B[k+1:n]))/matrix[k,k]
    return(B)

# %%
def find_mat(x_cood,y_cood,degree):
    degree+=1
    b = []
    mat = []
    for i in range(degree):
        power = i
        row =[]
        for j in range(degree):
            row.append(np.sum(np.power(x_cood,power)))
            power+=1
        power = 0 
        mat.append(row)
        b.append(np.sum(np.multiply(np.power(x_cood,i),y_cood)))
    mat = np.array(mat,  dtype=float)
    b = np.array(b)
    solution = find_solution(mat,b,degree)

    return(solution)


#%%
np.random.seed(0)
x = 2 - 3 * np.random.normal(0, 1, 20)
y = x - 2 * (x ** 2) + 0.5 * (x ** 3) + np.random.normal(-3, 3, 20)
#x = [1.1,1.21,1.25,1.23,1.3,1.4,1.42]
#y = [30,33,34,35,39,44,45]
plt.scatter(x,y, s=10)
plt.show()


solution_1 = find_mat(x,y,1)
solution_2 = find_mat(x,y,2)
solution_3 = find_mat(x,y,3)


# %%
def find_interpolated_func(solution):
    p1 = np.poly1d(solution) 
    x1 = np.linspace(-5,10,1000)
    y1=[]
    for i in x1:
        y1.append(np.polyval(solution[::-1],i))
    # print(y1)
    y1 = np.array(y1)
    return(x1,y1)

x1,y1 = find_interpolated_func(solution_1)
x2,y2 = find_interpolated_func(solution_2)
x3,y3 = find_interpolated_func(solution_3)
# %%



fig = plt.figure(figsize=(15,8))
fig2 = plt.figure(figsize=(15,8))
ax1 = fig.add_subplot(121)
ax2 = fig2.add_subplot(122)
ax1.scatter(x,y)
ax2.scatter(x,y)
ax2.plot(x1,y1, label='1st degree')
ax2.plot(x2,y2,  label='2nd degree')
ax2.plot(x3,y3,  label='3rd degree')
fig2.legend()
fig.show()
fig2.show()


# %%


