from numpy import array, diag, diagflat, dot
import  numpy as np
from numpy.linalg import inv

N=100
A=array([[45.,-3.,-7.,8.],[-12.,36.,9.,-5.],[-6.,4.,57.,-8],[-3.,-5.,-10.,78.]])
b=array([1000.,-50.,300.,53.])
guess=array([0.,0.,0.,0.])

U=np.triu(A,1)
L=np.tril(A,-1)
D=diagflat(diag(A))
invD=inv(D)
minLminU=-L-U
e= 0.00000000000002
for i in range(N):
    minLminUdotXplusB=dot(minLminU, guess) + b
    guess = dot(invD, minLminUdotXplusB)
    print(i+1,np.round(guess, 5))
    e=np.linalg.norm(A@guess-b)
    if e<1e-2:
        break




