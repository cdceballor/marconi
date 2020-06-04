import  numpy as np
A=np.array([[45,-3,-7,8],
            [-12,36,9,-5],
            [-6,4,57,-8],
            [-3,-5,-10,78]])
b=np.array([1000.,-50.,300.,53.])
x=np.zeros_like(b)
N=100
for k in range(N):
    for i in range(len(b)):
        x[i]=(b[i]-np.sum(A[i][:i]*x[:i])-np.sum(A[i][i+1:]*x[i+1:]))/A[i][i]#Lado izquierdo de la diagonal

    e=np.linalg.norm(A@x-b)
    print(k,x,e)
    if e<1e-6:
        break
