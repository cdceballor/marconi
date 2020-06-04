import numpy as np
import math
from tabulate import tabulate

class newton:

    def __init__(self, Fx, derivative, nIter, tolerance, X0):
        self.Fx = Fx
        self.derivative = derivative
        self.nIter = nIter
        self.tolerance = tolerance
        self.X0 = X0

         
    def f(self,x):
        # return np.double(math.sin(x + 3) - math.log(x + 1) + math.pow(x, 2) - 3)
        # return np.double(-math.pow(3,-math.pow(x,2)+1)+0.06*math.pow(x,2)+2.5)
        #return math.sin(x+3) - math.log(x+1) + math.pow(x, 2)-3
        fx1=self.Fx.replace("x",str(x))
        return eval(fx1)


    def df(self,x):
        # return np.double(math.cos(x + 3) - (1 / (x + 1)) + 2 * x)
        # return np.double(math.pow(3,-math.pow(x,2)+1)-0.06*math.pow(x,2)-2.5)
        #return math.cos(x+3)-1/(x+1)+2*x
        gx1=self.derivative.replace("x",str(x))
        return eval(gx1)


    def newton1(self):
        data_to_table = []

    #  x0 = int(input())
    #  tolerancia = float(input())
    #  niter = int(input())
        x0=float(self.X0)
        fx = self.f(x0)
        dfx = self.df(x0)
        contador = 0
        error = float(self.tolerance) + 1
        tolerancia=float(self.tolerance)
        niter=int(self.nIter)

        data_to_table.append([contador, x0, fx, dfx, error])
        p = ""
        while error > tolerancia and fx != 0 and dfx != 0 and contador < niter:
            x1 = x0 - (fx / dfx)
            fx = self.f(x1)
            dfx = self.df(x1)
            error = abs(x1 - x0)
            x0 = x1
            contador += 1
            data_to_table.append([contador, x0, fx, dfx, error])

        if fx == 0:
            p = "x0={} es una raiz".format(x0)
            p+= str(", numero de iteraciones={}:".format(contador))+"\n"
        elif error < tolerancia:
            p=+str("x1={} es una proximación a una raiz con una tolerancia={}".format(
                x1, tolerancia)+"\n")
        elif dfx == 0:
            p+= str("x1={} es una posible raiz multiple".format(x1)+"\n")
        else:
            p+= str(" Fracaso en niter={} iteraciones".format(niter)+"\n")

        p+= (tabulate(data_to_table, headers=[
            "N", "X0", "F(X)", "F'(X)", "error"]))

        return p
        print(p)



