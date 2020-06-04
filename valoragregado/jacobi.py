import  numpy as np
A=np.array([[15,-7,2],
            [-4,20,-16],
            [13,-4,45],])
b=np.array([5.,34.,-23.])
x=np.zeros_like(b)
N=100
for k in range(N):
    for i in range(len(b)):
        x[i]=(b[i]-np.sum(A[i][:i]*x[:i])-np.sum(A[i][i+1:]*x[i+1:]))/A[i][i]#Lado izquierdo de la diagonal

    e=np.linalg.norm(A@x-b)
    print(k,x,e)
    if e<1e-6:
        break
