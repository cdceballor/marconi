import numpy as np
from sympy import *
from sympy.parsing.sympy_parser import parse_expr
import math
from tabulate import tabulate

class NewtonDD:

    def __init__(self,mat, n):
        self.n = n
        self.mat = mat


    def main(self):
        p=""
        mat=self.mat.replace("[","")
        mat=mat.replace("]","")
        mat=mat.split(",")
        mat = np.array(mat)        
        mat = mat.astype(np.float)
        n = int(self.n)
        mat = mat.reshape(n, 4)
        print(mat)
        
        p+=str(self.NewtonCD(mat, n))

        return p

    def NewtonCD(self, mt, n):
        a=""
        polinomio = "P(X) = " + str(mt[0][1])
        F = Function('F')
        for j in range(2,n+1):
            for i in range(j-1,n):
                mt[i][j] = (mt[i][j-1] - mt[i-1][j-1])/(mt[i][0] - mt[i-j+1][0])
                if(i==j-1):
                    polinomio += " + " + str(mt[i][j])
                    for i in range(0,i):
                        polinomio += "(x - " + str(mt[i][0]) + ")"
                        
                    
        
        a+= "RESULTADO: \n"
        a+= tabulate(mt, headers = ("n", "xi", "F(Xi)", "PRIMERA", "SEGUNDA", "TERCERA", "CUARTA", "N-ésima"), showindex=True)
        a+= "\n"
        a+= "\n"
        a+= "\n"
        a+= str(polinomio)
        #a+=  str(parse_expr(polinomio.replace("P(X) = ","").replace("(","*(")))
        return a

