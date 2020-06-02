import numpy as np
import math
from tabulate import tabulate


class Secante:

    def __init__(self, Fx, nIter, tolerance, X0, X1):
        self.Fx = Fx
        self.nIter = nIter
        self.tolerance = tolerance
        self.X0 = X0
        self.X1 = X1

    def f(self, x):
        fx1 = self.Fx.replace("x", str(x))
        return eval(fx1)

    def secante(self):
        x0 = float(self.X0)
        x1 = float(self.X1)
        print(x1)
        tolerancia = float(self.tolerance)
        niter = float(self.nIter)

        data_to_table = []

        fx = self.f(x0)
        fx1 = float(self.f(x1))
        den = fx1-fx
        contador = 0
        error = tolerancia + 1

        data_to_table.append([contador, x0, fx, error])
        p = " "
        if fx == 0:
            p = str("x0={} es una raiz".format(x0))
        else:

            while error > tolerancia and fx != 0 and den != 0 and contador < niter:

                x2 = x1 - fx1*((x1 - x0) / den)
                #print("2: "+str(x2))
                #error = abs(x2 - x1)

                error = abs(x1 - x0)
                contador += 1
                x0 = x1
                fx = fx1
                x1 = x2
                fx1 = self.f(x1)
                den = fx1-fx

                data_to_table.append([contador, x0, fx, error])

            if fx1 == 0:
                p += str("x0={} es una raiz".format(x0))
                p += str("numero de iteraciones={}:".format(contador)+"\n")
            elif error < tolerancia:
                p += str("x1={} es una aproximación a una raiz con una tolerancia={}".format(x1, tolerancia)+"\n")
            elif den == 0 or x1 ==0:
                p+= str("den={} " + "Hay una raiz multiple en " + str(x1)+"\n")
            else:
                p += str("Fracaso en niter={} iteraciones".format(niter)+"\n")

            p += "\n"
            p += (tabulate(data_to_table, headers=["N", "X0", "F(X)", "error"]))

            return p
