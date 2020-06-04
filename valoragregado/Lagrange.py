import numpy as np
from sympy import *
from sympy.parsing.sympy_parser import parse_expr
import math

class Lagrange:

    def __init__(self,x,y,n):
        self.x=x
        self.y=y
        self.n=n



    def Lag(self):
        a =""
        polinomio = ""
        x = self.x.split(",")
        y = self.y.split(",")
        n = int(self.n)
        for i in range(len(x)):
            x[i] = float(x[i])

        for j in range(len(y)):
            y[j] =float(y[j])

        print(x)
        print("\n")
        print(y)
        print("\n")
        F = Function('F')
        G = Function('G')
        
        for i in range(n):
            L = "("
            for j in range(n):
                if (j != i):
                    L += "(x - " + str(x[j]) + ")"
            L += ")"
            L += " / ("
            for j in range(n):
                if (j != i):
                    L += "(" + str(x[i]) + " - " + str(x[j]) + ")"

            L += ")"
            L = L.replace(")(",")*(")
            F = parse_expr(L)
            print("\n L" + str(i) + "(x) = " + L.replace("((","(").replace("))",")") + " = " + str(expand(F)))
            toReplace = "L" + str(i) + "(x) = "
            if i == n-1:
                polinomio += "(" + str(expand(F)) + ")*" + str(y[i])
            else:
                polinomio += "(" + str(expand(F)) + ")*" + str(y[i]) + " + "

        a+= "POLINOMIO RESULTADO: \n"
        a+= str(polinomio)
        #a+= str(expand(polinomio))
        #G = str(expand(polinomio))
        return a